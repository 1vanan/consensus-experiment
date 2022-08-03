import json
import pandas as pd
import matplotlib.pyplot as plt

path_prefix = 'resources/cnf_3_orgs-multifactor_2/'
path_read = path_prefix + 'results.json'

path_write_1 = path_prefix + 'prob_backwards'
path_write_2 = path_prefix + 'msg_backwards'

var_on_axis = 'probability'

with open(path_read) as f:
    json_data = json.load(f)

    y_axis = [i[var_on_axis] for i in json_data["modelCheckResultList"]]
    backwards_num = [len(i['backwardTransitions']) for i in json_data['modelCheckResultList']]

    df = pd.DataFrame({var_on_axis: y_axis, 'backwards_num': backwards_num})
    df.plot(x='backwards_num', y=var_on_axis, kind='scatter')
    plt.savefig(path_write_1)
