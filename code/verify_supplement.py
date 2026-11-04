"""Verify the supplementary inventory and re-run the constructed checks."""
from pathlib import Path
import json,subprocess,sys
B=Path(__file__).resolve().parents[1]
load=lambda n:json.loads((B/'evidence'/n).read_text())
studies=load('study_extraction.json');refs=load('references.json');tables=load('tables.json');cases=load('randomized_cases.json');old=load('constructed_results.json')
assert len(studies)==20 and len(refs)==26 and len(tables)==4 and len(cases)==5000
assert len({r['id'] for r in studies})==20
assert [r['ref'] for r in refs]==list(range(1,27))
assert len(tables[0]['rows'])==20
assert all(r['anchor_page']>=1 and r['anchor_excerpt'] and len(r['pdf_sha256'])==64 for r in studies)
assert all(c['max_score_error']<=c['bound']+1e-12 for c in cases)
assert all(c['top3_stable'] for c in cases if c['certified'])
assert sum(c['certified'] for c in cases)==3338
assert sum(not c['top3_stable'] for c in cases)==667
subprocess.run([sys.executable,str(B/'code/constructed_checks.py')],check=True,stdout=subprocess.DEVNULL)
new=load('constructed_results.json')
for key in ['seed','instances','certified_top3','uncertified_top3_changes','violations']:
 assert old['randomized_checks'][key]==new['randomized_checks'][key]
print('PASS: 20 studies; 26 references; 4 tables; 4 examples; 5000 checks; 3338 certified sets; 0 violations.')
