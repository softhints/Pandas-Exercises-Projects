#Solutions 1
import pandas as pd
df = pd.read_csv('../../data/movies_metadata.csv', low_memory=False)


df.shape
df.shape[0]
df.shape[1]


rows - observations, records, trials
columns - variable, feature


df.head()
df.tail()


import numpy as np
df.iloc[np.r_[0:5, -5:0]]


r_ - Row-wise merging. Concatenate objects using slice notation.


df.columns
df.index


df.describe()


df.dtypes


df.head(2).T


df.sort_values(by='revenue', ascending=False)[['title', 'vote_count']].head()


from pandas.api.types import is_numeric_dtype

dfs = []

for col in df.columns:
    top_values = []
    if is_numeric_dtype(df[col]):
        top_values = df[col].nlargest(n=7)
        dfs.append(pd.DataFrame({col: top_values}).reset_index(drop=True))
pd.concat(dfs, axis=1)


`df.head()` - method
`df.shape` - attribute
`df.shape[1]` - square brackets - indexing



import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

ProfileReport(df, title="Pandas Profiling Report")