
from pathlib import Path
import json, sys

ROOT=Path(__file__).resolve().parents[1]
main=json.loads((ROOT/'workflows/VANTIX-Synthesis-Cross-Project-Governed-Correlation-v0.1-public.json').read_text())
adv=json.loads((ROOT/'workflows/VANTIX-Synthesis-Adversarial-Regression-v0.1-public.json').read_text())
errs=[]

if len(main.get('nodes',[]))!=19: errs.append(f'main_node_count:{len(main.get("nodes",[]))}!=19')
if len(adv.get('nodes',[]))!=9: errs.append(f'adv_node_count:{len(adv.get("nodes",[]))}!=9')

def targets(wf,name):
    out=[]
    for group in wf.get('connections',{}).get(name,{}).get('main',[]):
        out += [e.get('node') for e in group]
    return out

expected=[
    ('07 Deterministic Correlation Classifier','08 Validate Correlation Taxonomy & Evidence'),
    ('09 Bounded AI Explanation - Synthetic Replay','10 Independent AI Critique - Synthetic Replay'),
    ('10 Independent AI Critique - Synthetic Replay','11 Validate AI Outputs Deterministically'),
    ('11 Validate AI Outputs Deterministically','12 Determine Executive Route'),
    ('12 Determine Executive Route','13 Prepare Human Decision Contract'),
    ('14 Human Decision - Synthetic Fixture','15 Validate Human Decision Boundary')
]
for a,b in expected:
    if b not in targets(main,a): errs.append(f'missing_edge:{a}->{b}')

# AI cannot directly reach executive route/human fixture/report
consequential={
    '12 Determine Executive Route',
    '14 Human Decision - Synthetic Fixture',
    '19 Create Downloadable Executive Report'
}
for ai in ['09 Bounded AI Explanation - Synthetic Replay','10 Independent AI Critique - Synthetic Replay']:
    bad=set(targets(main,ai)) & consequential
    if bad: errs.append(f'ai_direct_consequential:{ai}->{sorted(bad)}')

# only validated AI output should directly feed executive route
incoming=[]
for src in main.get('connections',{}):
    if '12 Determine Executive Route' in targets(main,src):
        incoming.append(src)
if incoming != ['11 Validate AI Outputs Deterministically']:
    errs.append('executive_route_incoming:'+repr(incoming))

# no live AI provider nodes
for wf,name in [(main,'main'),(adv,'adv')]:
    types=' '.join(n.get('type','') for n in wf.get('nodes',[])).lower()
    if any(x in types for x in ['openai','gemini','anthropic']):
        errs.append(name+':live_ai_node_detected')

# dangling edges
for wf,name in [(main,'main'),(adv,'adv')]:
    names={n.get('name') for n in wf.get('nodes',[])}
    for src in wf.get('connections',{}):
        if src not in names: errs.append(f'{name}:unknown_source:{src}')
        for dst in targets(wf,src):
            if dst not in names: errs.append(f'{name}:dangling:{src}->{dst}')

if errs:
    print('SYNTHESIS GRAPH VALIDATION FAILED')
    for e in errs: print('-',e)
    sys.exit(1)

print('SYNTHESIS GRAPH VALIDATION PASSED')
print('- 19-node main workflow / 9-node adversarial workflow')
print('- deterministic classifier and AI-validation boundaries enforced')
print('- AI cannot directly reach executive route or human decision')
print('- no live AI-provider nodes')
