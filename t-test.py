import pandas as pd
from scipy.stats import ranksums

csv1_path = 'resources/cnf_3_orgs-majority/consensus-base-experiment.csv'
csv2_path = 'resources/cnf_3_orgs-majority/consensus-base-prism.csv'
consensus_base = pd.read_csv(csv1_path)
consensus_modified = pd.read_csv(csv2_path)
print('test for 3 orgs without backward transitions:')
print(ranksums(consensus_base, consensus_modified))
## pvalue=0.9986249506398537 - more than 0.05, then populations are similar


csv2_path = 'resources/cnf_3_orgs-majority/consensus-backwards-experiment.csv'
csv3_path = 'resources/cnf_3_orgs-majority/consensus-backwards-prism.csv'
consensus_base = pd.read_csv(csv2_path)
consensus_modified = pd.read_csv(csv3_path)
print('test for 3 orgs backward transitions:')
print(ranksums(consensus_base, consensus_modified))
## pvalue=0.9986249506398537 - more than 0.05, then populations are similar
