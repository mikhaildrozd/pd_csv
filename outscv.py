import pandas as pd
import numpy as np

in_data_a = pd.read_csv('in_data_a.csv')
in_data_b = pd.read_csv('in_data_p.csv')

in_data_a.rename(columns={'Date': 'date', 'Installs': 'installs', }, inplace=True)

result = pd.merge(in_data_a, in_data_b, on=['date', 'ad_id'])

result = result.loc[:, ('app', 'date', 'Campaign', 'os', 'installs', 'spend')]
result.rename(columns={'Campaign': 'campaign'}, inplace=True)

result = result.groupby(['app', 'date', 'campaign', 'os']).sum().reset_index()
result['cpi'] = result['spend'] / result['installs']

result = result.replace(np.inf, np.nan).dropna(axis=0)
decimals = pd.Series([2, 2], index=['spend', 'cpi'])
result = result.round(decimals)

result.to_csv('out.csv', encoding='utf-8', index=False)

