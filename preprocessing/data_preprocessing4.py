import pandas as pd
import json
import pickle
import matplotlib.pyplot as plt
import numpy as np

#['User_ID',    'Date',    'Time',    'Price']
data = pd.read_csv('./data/reduced_lottery_all.csv')

user_pool = data['User_ID'].unique()
print(len(user_pool))
# Group by 'user-id' and count the number of purchases
purchase_counts = data.groupby('User_ID').size().reset_index(name='num_purchases')

#plt.figure(figsize=(10, 6))
#plt.plot(purchase_counts['num_purchases'])
#plt.show()

user_dict = {}

count = 0
for user in user_pool:
    count = count + 1
    restricted_df = data[data['User_ID'] == user].reset_index(drop=True)
    user_dict[user] = restricted_df
    print(count)

with open('./data/reduced_data_each_user.pkl', 'wb') as f:
    pickle.dump(user_dict, f)