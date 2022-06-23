import pandas as pd
dataframe1 = pd.read_csv('Bulk_Lead_Create - Sheet1 (10).csv')
print(repr(dataframe1.to_csv(index=False)))
