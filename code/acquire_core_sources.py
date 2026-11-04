"""Optional primary-source acquisition. Not required for constructed_checks.py."""
from pathlib import Path
import urllib.request,subprocess,json
B=Path(__file__).resolve().parents[1]
(B/'sources').mkdir(exist_ok=True)
SOURCES={'R01': 'https://openaccess.thecvf.com/content_CVPR_2020/papers/Shen_Towards_Backward-Compatible_Representation_Learning_CVPR_2020_paper.pdf', 'R02': 'https://arxiv.org/pdf/2206.03040', 'R03': 'https://arxiv.org/pdf/2201.09724', 'R04': 'https://www.ijcai.org/proceedings/2022/0225.pdf', 'R05': 'https://arxiv.org/pdf/2306.12689', 'R06': 'https://arxiv.org/pdf/2505.12540', 'R07': 'https://arxiv.org/pdf/2510.02348', 'R08': 'https://arxiv.org/pdf/2609.16875', 'R09': 'https://raw.githubusercontent.com/mlresearch/v267/main/assets/bui25b/bui25b.pdf', 'R10': 'https://arxiv.org/pdf/2610.09411', 'R16': 'https://openaccess.thecvf.com/content/CVPR2022/papers/Ramanujan_Forward_Compatible_Training_for_Large-Scale_Embedding_Retrieval_Systems_CVPR_2022_paper.pdf', 'R17': 'https://openaccess.thecvf.com/content/ICCV2021/papers/Meng_Learning_Compatible_Embeddings_ICCV_2021_paper.pdf', 'R18': 'https://arxiv.org/pdf/2609.05339', 'R19': 'https://arxiv.org/pdf/2608.05857', 'R20': 'https://arxiv.org/pdf/2609.23036', 'R21': 'https://arxiv.org/pdf/2509.16664', 'R22': 'https://arxiv.org/pdf/2609.39836', 'R23': 'https://arxiv.org/pdf/2211.09032', 'R24': 'https://arxiv.org/pdf/2506.00037', 'R25': 'https://arxiv.org/pdf/2303.04766'}
for key,url in SOURCES.items():
 try:
  data=urllib.request.urlopen(url,timeout=40).read()
  if not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
  p=B/'sources'/(key+'.pdf');p.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  print(key,'retrieved; compare hash with evidence/source_manifest.json')
 except Exception as e:print(key,'FAILED',str(e))
