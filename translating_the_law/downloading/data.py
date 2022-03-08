from numpy import ALLOW_THREADS
from translating_the_law.downloading.get_data import get_data
data = get_data(0)
for n in range(len(data)):
    background_to_the_appeal = n['press summary']['Background to the appeal']
    reasons_for_the_judgment = n['press summary']['Reasons for the judgment']
    if 'allows the appeal' in n['press summary']['Judgment']:
        judgment = 'Allowed'
    else:
        judgment = 'Rejected'
    justices = n['press summary']['Justices']
    
