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

# Step 3: Create a dictionary to hold user data in numpy format
user_data_dict = {}

# Step 4: Group the data by User_ID and Date, then calculate total price and purchase count for each user and each date
grouped = reduced_lottery_all.groupby(['User_ID', 'Date']).agg(
    total_price=('Price', 'sum'),  # Total amount spent on each date
    purchase_count=('Price', 'size')  # Number of purchases on each date
).reset_index()

# Step 5: For each user, convert their data into a numpy array where
# row: date
# column 0: total price, column 1: purchase count
for user in users:
    user_data = grouped[grouped['User_ID'] == user]

    # Create numpy array where each row is [total_price, purchase_count] for each date
    user_numpy = np.zeros((user_data['Date'].nunique(), 2))

    # Fill numpy array with total price and purchase count
    user_numpy[:, 0] = user_data['total_price'].values  # Total price for each date
    user_numpy[:, 1] = user_data['purchase_count'].values  # Purchase count for each date

    # Store the user's numpy array in the dictionary
    user_data_dict[user] = user_numpy
# %%
grouped
# %%
user_data_dict.keys()
# %%
len(user_data_dict.keys())
# %%
user_data_dict.items()
# %%
# Step 6: Save the dictionary as a pickle file
with open('./data/user_data_dict.pkl', 'wb') as f:
    pickle.dump(user_data_dict, f)

print("Pickle file saved successfully.")