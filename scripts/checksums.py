
from pathlib import Path
import hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'SHA256SUMS.txt'

def files():
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts or p==LEDGER:
            continue
        yield p

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''):
            h.update(c)
    return h.hexdigest()

if '--write' in sys.argv:
    LEDGER.write_text(''.join(f'{digest(p)}  {p.relative_to(ROOT).as_posix()}\n' for p in files()),encoding='utf-8')
    print('SHA256SUMS WRITTEN')
    sys.exit(0)

exp={}
for line in LEDGER.read_text(encoding='utf-8').splitlines():
    if line.strip():
        sha,rel=line.split('  ',1)
        exp[rel]=sha

act={p.relative_to(ROOT).as_posix():digest(p) for p in files()}
errs=[]
for rel,sha in act.items():
    if rel not in exp: errs.append('omitted:'+rel)
    elif exp[rel]!=sha: errs.append('mismatch:'+rel)
for rel in exp:
    if rel not in act: errs.append('missing:'+rel)

if errs:
    print('SHA256SUMS FAILED')
    for e in errs: print('-',e)
    sys.exit(1)

print('SHA256SUMS PASSED')
print(f'- entries: {len(act)}')
