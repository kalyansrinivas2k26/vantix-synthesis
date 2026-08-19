
const fs=require('fs'), crypto=require('crypto');

const mainPath=process.argv[2];
const advPath=process.argv[3];
const outPath=process.argv[4];

function inputApi(items){
  const a=Array.isArray(items)?items:[];
  return {all:()=>a,first:()=>a[0]||{json:{}},last:()=>a[a.length-1]||{json:{}},item:a[0]||{json:{}}};
}
function load(path){
  const wf=JSON.parse(fs.readFileSync(path,'utf8'));
  const nodes=Object.fromEntries(wf.nodes.map(n=>[n.name,n]));
  function run(name,items){
    const code=nodes[name]?.parameters?.jsCode;
    if(!code) throw new Error('no_code:'+name);
    return new Function('$input',code)(inputApi(items));
  }
  return {wf,nodes,run};
}
const main=load(mainPath), adv=load(advPath);
const tests=[];
function test(id,fn){
  try{ tests.push({id,status:'PASS',details:fn()}); }
  catch(e){ tests.push({id,status:'FAIL',error:String(e.stack||e)}); }
}

let mainState=[];
test('SYN-OFF-01_main_exact_node_chain',()=>{
  const order=main.wf.nodes.map(n=>n.name).filter(n=>n!=='01 Manual Trigger - Synthesis Portfolio Preview' && n!=='19 Create Downloadable Executive Report');
  for(const name of order) mainState=main.run(name,mainState);
  const s=mainState[0].json;
  if(!s.finalAudit?.sourceAuthorityPreserved || !s.aiValidation?.valid || !s.humanDecisionValidation?.valid) throw new Error('main_audit_not_valid');
  return {correlations:s.correlations.length,route:s.executiveRoute,sourceAuthorityPreserved:true};
});

test('SYN-OFF-02_all_six_taxonomy_classes',()=>{
  const got=mainState[0].json.correlations.map(x=>x.class).sort();
  const exp=['compounding','contradictory','duplicate','related','repeated','unresolved'].sort();
  if(JSON.stringify(got)!==JSON.stringify(exp)) throw new Error('taxonomy:'+got.join(','));
  return {classes:got};
});

test('SYN-OFF-03_no_universal_source_override',()=>{
  const s=mainState[0].json;
  if(!s.correlations.every(x=>x.sourceAuthorityPreserved===true)) throw new Error('source_authority_override');
  if(s.enterpriseRiskScore!==undefined) throw new Error('universal_risk_score_present');
  return {sourceAuthorityPreserved:true,universalRiskScorePresent:false};
});

test('SYN-OFF-04_six_sigma_boundary',()=>{
  const m=mainState[0].json.measurement;
  if(m.unit!=='validated correlation record'||m.opportunitiesPerUnit!==5||m.capabilityClaim!==false) throw new Error('measurement_boundary_invalid');
  return {unit:m.unit,opportunitiesPerUnit:m.opportunitiesPerUnit,capabilityClaim:m.capabilityClaim,syntheticDPMO:m.dpmo};
});

test('SYN-OFF-05_human_identity_boundary',()=>{
  const v=mainState[0].json.humanDecisionValidation;
  if(v.authenticatedIdentity!==false) throw new Error('identity_overclaim');
  return {authenticatedIdentity:false,decision:mainState[0].json.humanDecision.decision};
});

let advState=[];
test('SYN-OFF-06_adversarial_24_of_24',()=>{
  const order=adv.wf.nodes.map(n=>n.name).filter(n=>n!=='01 Manual Trigger - Synthesis Adversarial');
  for(const name of order) advState=adv.run(name,advState);
  const s=advState[0].json;
  if(s.summary?.status!=='PASSED'||s.summary.passed!==24||s.summary.total!==24) throw new Error('adversarial_not_24_24');
  return {status:s.summary.status,passed:s.summary.passed,total:s.summary.total};
});

test('SYN-OFF-07_adversarial_ids_complete',()=>{
  const ids=advState[0].json.results.map(x=>x.id);
  if(new Set(ids).size!==24) throw new Error('duplicate_or_missing_test_id');
  for(const prefix of ['SRC-','PROV-','COR-','AI-','AUTH-','XDOM-']){
    if(!ids.some(x=>x.startsWith(prefix))) throw new Error('missing_group:'+prefix);
  }
  return {testIdCount:ids.length};
});

test('SYN-OFF-08_synthetic_boundary_visible',()=>{
  const h=mainState[0].json.executiveHtml||'';
  const a=advState[0].json.executiveHtml||'';
  if(!h.includes('SYNTHETIC PORTFOLIO PREVIEW')) throw new Error('main_boundary_missing');
  if(!a.includes('No live source project, Salesforce org, model provider, customer action, or authenticated human action occurred.')) throw new Error('adv_boundary_missing');
  return {mainBoundary:true,adversarialBoundary:true};
});

const result={
  evidenceClass:'OFFLINE_EXACT_NODE_CODE_EXECUTION',
  n8nRuntimeExecution:false,
  mainWorkflowSha256:crypto.createHash('sha256').update(fs.readFileSync(mainPath)).digest('hex'),
  adversarialWorkflowSha256:crypto.createHash('sha256').update(fs.readFileSync(advPath)).digest('hex'),
  testCount:tests.length,
  passCount:tests.filter(x=>x.status==='PASS').length,
  failCount:tests.filter(x=>x.status==='FAIL').length,
  adversarialSummary:advState[0]?.json?.summary||null,
  tests
};
if(outPath) fs.writeFileSync(outPath,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
if(result.failCount) process.exit(1);
