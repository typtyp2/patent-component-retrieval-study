"""Reproduce released descriptive means with the Python standard library."""
from pathlib import Path
from collections import defaultdict
from statistics import mean
import csv
import json
import math

HERE=Path(__file__).resolve().parent

def main():
    with (HERE/'data/retrieval_metrics.csv').open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    expected=json.loads((HERE/'data/expected_means.json').read_text())
    output={}
    for subset in ('all','exclude_translation_exposed'):
        groups=defaultdict(lambda:defaultdict(list))
        for r in rows:
            if subset!='all' and (r['query_set']=='name' or r['translation_exposed']=='1'): continue
            key=(r['query_set'],r['retriever'],r['condition'])
            groups[key][r['patent_id']].append(r)
        for (query,retriever,condition),patents in groups.items():
            values={m:mean(mean(float(r[m]) for r in rs) for rs in patents.values()) for m in ('ndcg10','mrr10','r10')}
            if subset=='all':
                for m,v in values.items():
                    assert math.isclose(v,expected[query][retriever]['mean_by_condition'][condition][m],abs_tol=1e-12)
            output[' | '.join((subset,query,retriever,condition))]=dict(n_patents=len(patents),n_queries=sum(map(len,patents.values())),**values)
    (HERE/'reproduced_means.json').write_text(json.dumps(output,indent=2))
    print(f'PASS: {len(rows)} metric rows; {len(output)} aggregated conditions; expected means match.')

if __name__=='__main__': main()
