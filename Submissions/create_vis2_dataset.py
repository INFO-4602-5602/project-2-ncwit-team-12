import pandas as pd

df = pd.read_csv('NCWIT_DataV2_RawData.csv')
df2 = df.loc[df['School Year'] == '2015-2016']
df2 = df2[['Totals, Female: Asian (Tot. F)',
           'Totals, Female: Black/African American (Tot. F)',
           'Totals, Female: Hispanics of any race (Tot. F)',
           'Totals, Female: American Indian/Alaska Native (Tot. F)',
           'Totals, Female: Native Hawaiian/Other Pacific Islander (Tot. F)',
           'Totals, Female: White (Tot. F)']]

df2.to_csv("2015-2016_ethnicity_data.csv", na_rep='0')
