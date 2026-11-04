"""Constructed mathematical checks, NOT measurements of embedding models.
Run with Python >=3.10; standard library only. Fixed seed 20261104.
"""
from pathlib import Path
import math,random,json
B=Path(__file__).resolve().parents[1]
def vec(t):return [math.cos(t),math.sin(t)]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def norm(x):return math.sqrt(dot(x,x))
def sub(x,y):return [a-b for a,b in zip(x,y)]
def unit(x):
 n=norm(x);return [a/n for a in x]
def order(s):return sorted(range(len(s)),key=lambda i:(-s[i],i))
def run():
 # A: arbitrarily high query cosine, but a boundary crossing reverses top-1.
 q=vec(.001);qh=vec(-.001);docs=[vec(.01),vec(-.01)]
 a={'query_cosine':dot(q,qh),'reference_scores':[dot(q,d) for d in docs],'mapped_scores':[dot(qh,d) for d in docs]}
 assert order(a['reference_scores'])[0]==0 and order(a['mapped_scores'])[0]==1
 # B: perfect same-item matching across a finite anchor pool says nothing about an unseen query.
 # Identity map on document anchors; held-out query is mapped to the wrong side.
 anchors=[vec(0),vec(math.pi/2),vec(math.pi)]
 b={'anchor_counterpart_top1':sum(order([dot(x,y) for y in anchors])[0]==i for i,x in enumerate(anchors))/3,'heldout_query_reference_top1':0,'heldout_query_mapped_top1':1,'reference_query':vec(.1),'mapped_query':vec(1.4)}
 assert order([dot(b['reference_query'],d) for d in anchors])[0]==0
 assert order([dot(b['mapped_query'],d) for d in anchors])[0]==1
 # C: monotone score mapping preserves ranking but invalidates a reused threshold.
 s=[.9,.7,.2];mapped=[x/2 for x in s];c={'old_scores':s,'new_scores':mapped,'threshold':.8,'old_accepts':sum(x>=.8 for x in s),'new_accepts':sum(x>=.8 for x in mapped)}
 assert order(s)==order(mapped) and c['old_accepts']!=c['new_accepts']
 # D: both homogeneous endpoints retrieve the positive; a mixed gallery does not.
 oldq=vec(.45);newq=vec(0);old=[vec(.45),vec(.65)];new=[vec(.10),vec(.20)]
 d={'old_old_scores':[dot(oldq,x) for x in old],'new_new_scores':[dot(newq,x) for x in new],'new_old_scores':[dot(newq,x) for x in old],'mixed_scores':[dot(newq,old[0]),dot(newq,new[1])]}
 assert order(d['old_old_scores'])[0]==order(d['new_new_scores'])[0]==order(d['new_old_scores'])[0]==0
 assert order(d['mixed_scores'])[0]==1
 rng=random.Random(20261104);n=5000;cert=flips=0;max_ratio=0
 cases=[]
 for i in range(n):
  dim=rng.choice([2,4,8,16]);nd=12;k=3
  q=unit([rng.gauss(0,1) for _ in range(dim)]);ds=[unit([rng.gauss(0,1) for _ in range(dim)]) for _ in range(nd)]
  scale=10**rng.uniform(-6,-.3)
  qh=unit([v+rng.gauss(0,scale) for v in q]);dh=[unit([v+rng.gauss(0,scale) for v in x]) for x in ds]
  eq=norm(sub(qh,q));ed=max(norm(sub(x,y)) for x,y in zip(ds,dh));bound=eq+ed+eq*ed
  s=[dot(q,x) for x in ds];sh=[dot(qh,x) for x in dh];err=max(abs(x-y) for x,y in zip(s,sh))
  assert err<=bound+1e-12
  idx=order(s);gap=s[idx[k-1]]-s[idx[k]];stable=set(idx[:k])==set(order(sh)[:k]);certified=gap>2*bound
  if certified: assert stable;cert+=1
  if not stable:flips+=1
  max_ratio=max(max_ratio,err/bound)
  cases.append({'case':i,'dimension':dim,'epsilon_q':eq,'epsilon_d':ed,'bound':bound,'max_score_error':err,'top3_gap':gap,'certified':certified,'top3_stable':stable})
 out={'provenance':'All vectors are constructed. No pretrained model, real query corpus, or deployment was evaluated.','examples':{'A':a,'B':b,'C':c,'D':d},'randomized_checks':{'seed':20261104,'instances':n,'certified_top3':cert,'uncertified_top3_changes':flips,'maximum_score_error_to_bound_ratio':max_ratio,'violations':0}}
 (B/'evidence/constructed_results.json').write_text(json.dumps(out,indent=2));(B/'evidence/randomized_cases.json').write_text(json.dumps(cases,separators=(',',':')))
 print(json.dumps(out,indent=2))
if __name__=='__main__':run()
