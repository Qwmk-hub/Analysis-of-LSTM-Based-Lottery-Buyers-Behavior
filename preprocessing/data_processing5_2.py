import os

# %%
os.listdir()
# %%
import pandas as pd
import numpy as np
import pickle

# Step 1: Load the reduced lottery data

reduced_lottery_all = pd.read_csv('./data/reduced_lottery_all.csv')
reduced_lottery_all.head()
# %%
# Step 2: Get the list of unique users
users = reduced_lottery_all['User_ID'].unique()

user_data_dict = {}
date_length = 31 + 29 + 31 + 30
count = 0
for user in users:
    user_numpy = np.zeros([date_length, 2], dtype='float')
#    for i in range(date_length):
    temp=reduced_lottery_all[reduced_lottery_all['User_ID'] == user]
    purchase_date = temp['Date'].unique()
    for date in purchase_date:
        user_numpy[date - 1, 0] = temp[temp['Date']==date]['Price'].sum()
        user_numpy[date - 1, 1] = len(temp[temp['Date'] == date]['Price'])

    user_data_dict[user] = user_numpy
    count = count + 1
    if count % 10 == 0:
        print(count)


# Step 3: Create a dictionary to hold user data in numpy format

with open('./data/user_data_dict.pkl', 'wb') as f:
    pickle.dump(user_data_dict, f)
