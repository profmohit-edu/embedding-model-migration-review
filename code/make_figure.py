from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
B=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size':10,'font.family':'DejaVu Sans','pdf.fonttype':42})
fig,ax=plt.subplots(1,2,figsize=(7,3),layout='constrained')
x=np.linspace(-.002,.002,200)
diff=np.cos(x-.01)-np.cos(x+.01)
ax[0].plot(x,diff*1e5,color='black');ax[0].axhline(0,color='.6',lw=.8)
ax[0].scatter([-.001,.001],[-1.9999663,1.9999663],color=['.2','.6'],zorder=3)
ax[0].set(xlabel='Query angle (radians)',ylabel='Relevant minus irrelevant score (x 10^-5)',title='A. High cosine; reversed order')
ax[0].ticklabel_format(axis='x',style='sci',scilimits=(0,0));ax[0].grid(alpha=.15)
r=json.loads((B/'evidence/constructed_results.json').read_text())['examples']['D']
keys=['old_old_scores','new_new_scores','new_old_scores','mixed_scores'];x=np.arange(4)
a=[r[k][0] for k in keys];b=[r[k][1] for k in keys]
ax[1].bar(x-.16,a,width=.30,color='.25',label='Relevant')
ax[1].bar(x+.16,b,width=.30,color='.7',label='Irrelevant')
ax[1].set(xticks=x,xticklabels=['Old/old','New/new','New/old','Mixed'],ylim=(.7,1.04),ylabel='Cosine score',title='D. Endpoints do not cover mixing')
ax[1].tick_params(axis='x',labelsize=9);ax[1].legend(frameon=False,fontsize=9,loc='lower left');ax[1].grid(axis='y',alpha=.15)
fig.savefig(B/'manuscript/Figure_1.pdf');fig.savefig(B/'manuscript/Figure_1.png',dpi=220)
