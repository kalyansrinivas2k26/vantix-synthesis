
from pathlib import Path
import json,re,hashlib,sys

ROOT=Path(__file__).resolve().parents[1]
errs=[]

required=[
'README.md','.gitignore','LICENSE','SECURITY.md','CONTRIBUTING.md','CHANGELOG.md',
'PORTFOLIO_STATUS_PROJECTS_1_4.md','GITHUB_ABOUT_ACTION.md','FINAL_HANDOFF.md',
'INDEPENDENT_REVIEW_PROMPT.md','UPLOAD_READY.md','source-manifest.json','SHA256SUMS.txt',
'.github/workflows/validate.yml',
'contracts/v1.0.0/source-signal.schema.json',
'contracts/v1.0.0/correlation-record.schema.json',
'contracts/v1.0.0/human-decision.schema.json',
'contracts/v1.0.0/synthesis-output.schema.json',
'fixtures/source-signals.synthetic.json','fixtures/adversarial-cases.json',
'prompts/synthesis-explanation-prompt.md','prompts/synthesis-critique-prompt.md',
'workflows/VANTIX-Synthesis-Cross-Project-Governed-Correlation-v0.1-public.json',
'workflows/VANTIX-Synthesis-Adversarial-Regression-v0.1-public.json',
'tests/offline_exact_node_tests.js','scripts/checksums.py','scripts/validate_graph.py',
'evidence/offline-exact-node-test-results.json','evidence/adversarial-regression-v0.1.html',
'validation/NEGATIVE_TEST_EVIDENCE.md',
'docs/EXECUTIVE_BRIEF.md','docs/ARCHITECTURE.md','docs/CORRELATION_TAXONOMY.md','docs/CORRELATE_WITHOUT_COMPRESSING.md',
'docs/EVIDENCE_MODEL.md','docs/DECISION_RIGHTS.md','docs/OWASP_AI_SECURITY_MAPPING.md',
'docs/PMP_AI_GOVERNANCE_MAPPING.md','docs/AGILE_TRACEABILITY.md','docs/SIX_SIGMA_MEASUREMENT.md',
'docs/TEST_CATALOGUE.md','docs/EVIDENCE_PROVENANCE.md','docs/EVIDENCE_INDEX.md',
'docs/QUALITY_SCORECARD.md','docs/RISK_REGISTER.md','docs/DECISION_REGISTER.md',
'docs/GITHUB_PRESENTATION_CHECKLIST.md','docs/FREEZE_GAP_MATRIX.md','docs/DEMO_SCRIPT.md',
'docs/PLAIN_LANGUAGE_SUMMARY.md'
]
for rel in required:
    if not (ROOT/rel).exists(): errs.append('missing required:'+rel)

# stale duplicate canonicals
for pat in ['FINAL_HANDOFF_v*.md','INDEPENDENT_REVIEW_PROMPT_v*.md','README-PROPOSED.md']:
    for p in ROOT.glob(pat): errs.append('stale duplicate canonical:'+p.name)

# JSON parse
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errs.append(f'json parse:{p.relative_to(ROOT)}:{e}')

# identity
readme=(ROOT/'README.md').read_text(encoding='utf-8')
if not readme.startswith('# VANTIX Synthesis'): errs.append('README identity invalid')
if 'Portfolio Preview v0.1' not in readme[:1500]: errs.append('release wording missing')
if 'universal enterprise risk score' not in readme: errs.append('no-universal-score boundary missing')

# source manifest exact sources and frozen commit bindings
mp=ROOT/'source-manifest.json'
if mp.exists():
    m=json.loads(mp.read_text())
    expected_bindings={
        'P1_FLOW_INTEGRITY':'dd75ea5',
        'P2_AGILE_DELIVERY':'a4137f8',
        'P3_CONTROL_VALUE':'6e605dd',
        'P4_ATTESTOR':'8fdf848',
    }
    sources=m.get('sources',[])
    got={x.get('project') for x in sources}
    if got!=set(expected_bindings): errs.append('source manifest project set mismatch')
    if m.get('finalCommitBinding')!='FROZEN_SOURCE_COMMITS':
        errs.append('source manifest commit binding status mismatch')
    got_bindings={x.get('project'):x.get('finalCommitSha') for x in sources}
    if got_bindings!=expected_bindings:
        errs.append('source manifest frozen commit binding mismatch')

# workflow counts
mainp=ROOT/'workflows/VANTIX-Synthesis-Cross-Project-Governed-Correlation-v0.1-public.json'
advp=ROOT/'workflows/VANTIX-Synthesis-Adversarial-Regression-v0.1-public.json'
if mainp.exists():
    d=json.loads(mainp.read_text())
    if len(d.get('nodes',[]))!=19: errs.append('main workflow node count')
    if d.get('active') is True: errs.append('main public workflow active')
if advp.exists():
    d=json.loads(advp.read_text())
    if len(d.get('nodes',[]))!=9: errs.append('adversarial workflow node count')
    if d.get('active') is True: errs.append('adversarial public workflow active')

# fixture six classes are produced by offline evidence + 24 cases
op=ROOT/'evidence/offline-exact-node-test-results.json'
if op.exists() and mainp.exists() and advp.exists():
    ev=json.loads(op.read_text())
    if ev.get('evidenceClass')!='OFFLINE_EXACT_NODE_CODE_EXECUTION' or ev.get('n8nRuntimeExecution') is not False:
        errs.append('offline evidence class invalid')
    if ev.get('testCount')!=8 or ev.get('passCount')!=8 or ev.get('failCount')!=0:
        errs.append('offline evidence not 8/8')
    if ev.get('adversarialSummary',{}).get('passed')!=24:
        errs.append('adversarial summary not 24/24')
    if ev.get('mainWorkflowSha256')!=hashlib.sha256(mainp.read_bytes()).hexdigest():
        errs.append('main workflow evidence hash mismatch')
    if ev.get('adversarialWorkflowSha256')!=hashlib.sha256(advp.read_bytes()).hexdigest():
        errs.append('adversarial workflow evidence hash mismatch')

# secret scan
pats=[
    re.compile(r'AIza[0-9A-Za-z_-]{20,}'),
    re.compile(r'sk-[0-9A-Za-z_-]{20,}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'''(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*["'][A-Za-z0-9_-]{16,}''',re.I)
]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.name=='SHA256SUMS.txt' or '__pycache__' in p.parts: continue
    if p.suffix.lower() not in {'.md','.json','.py','.js','.mjs','.yml','.yaml','.html','.txt','.sh','.env'}: continue
    txt=p.read_text(encoding='utf-8',errors='ignore')
    if any(q.search(txt) for q in pats): errs.append('possible secret:'+p.relative_to(ROOT).as_posix())

# markdown links & anchors
link_re=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
def slug(h):
    s=re.sub(r'<[^>]+>','',h.strip().lower())
    s=re.sub(r'[^\w\s-]','',s)
    return re.sub(r'\s+','-',s)
anchors={}
for p in ROOT.rglob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore')
    anchors[p.resolve()]={slug(m.group(1)) for m in re.finditer(r'^#{1,6}\s+(.+?)\s*$',txt,re.M)}
for p in ROOT.rglob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore')
    for target in link_re.findall(txt):
        target=target.strip().split()[0].strip('<>')
        if target.startswith(('http://','https://','mailto:')): continue
        if target.startswith('#'):
            if target[1:].lower() not in anchors[p.resolve()]: errs.append(f'broken anchor:{p.relative_to(ROOT)}->{target}')
            continue
        pathpart,_,anchor=target.partition('#')
        q=(p.parent/pathpart).resolve()
        try:q.relative_to(ROOT.resolve())
        except ValueError:
            errs.append(f'link escapes repo:{p.relative_to(ROOT)}->{target}'); continue
        if not q.exists():
            errs.append(f'broken link:{p.relative_to(ROOT)}->{target}'); continue
        if anchor and q.suffix.lower()=='.md' and anchor.lower() not in anchors.get(q,set()):
            errs.append(f'broken cross anchor:{p.relative_to(ROOT)}->{target}')

# score
sp=ROOT/'docs/QUALITY_SCORECARD.md'
if sp.exists():
    t=sp.read_text()
    rows=re.findall(r'^\| [^|*][^|]* \| (\d+) \| (\d+) \|',t,re.M)
    weights=sum(int(a) for a,b in rows); score=sum(int(b) for a,b in rows)
    if weights!=100: errs.append(f'score weights={weights}')
    if score!=94: errs.append(f'score={score},expected94')
    m=re.search(r'\| \*\*Total\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*',t)
    if not m: errs.append('score total row missing')
    elif int(m.group(1))!=weights or int(m.group(2))!=score:
        errs.append('score printed total mismatch')

# prohibited wording
for p in ROOT.rglob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore').lower()
    for banned in ['mckinsey-standard','mckinsey-style','independent audit','no competitor does this','production-ready']:
        if banned in txt: errs.append(f'banned wording:{p.relative_to(ROOT)}:{banned}')

if errs:
    print('SYNTHESIS REPOSITORY VALIDATION FAILED')
    for e in errs: print('-',e)
    sys.exit(1)

print('SYNTHESIS REPOSITORY VALIDATION PASSED')
print('- required artifacts, JSON, identity and source manifest passed')
print('- workflow/evidence hashes, 8/8 offline tests and 24/24 adversarial summary passed')
print('- secret scan, Markdown links/anchors and score arithmetic passed')
