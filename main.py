import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
# print(lst)
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# print(data)
data.head()
# print(data.head())
def one_hot(dataframe):
    # print(dataframe)
    dataframe.loc[dataframe['whoAmI']=='robot', 'one_hot_means']=0
    dataframe.loc[dataframe['whoAmI'] == 'human', 'one_hot_means'] = 1
    dataframe['one_hot_means']=dataframe ['one_hot_means'].astype('int32')
    # print(dataframe.info())
    return dataframe
print(one_hot(data))

