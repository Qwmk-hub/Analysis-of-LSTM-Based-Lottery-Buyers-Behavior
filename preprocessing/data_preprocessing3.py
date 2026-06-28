import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#['User_ID',    'Date',    'Time',    'Price']
lottery_all = pd.read_csv('./data/lottery_all.csv')

user_pool = lottery_all['User_ID'].unique()
print(len(user_pool))
# Group by 'user-id' and count the number of purchases
purchase_counts = lottery_all.groupby('User_ID').size().reset_index(name='num_purchases')

plt.figure(figsize=(10, 6))
plt.plot(purchase_counts['num_purchases'])
plt.show()


filtered_users = purchase_counts[purchase_counts['num_purchases'] > 300]

# Step 3: Merge or filter the original dataframe to keep only those user-ids
reduced_lottery_all = lottery_all[lottery_all['User_ID'].isin(filtered_users['User_ID'])]
reduced_user_pool = reduced_lottery_all['User_ID'].unique()
reduced_purchase_counts = reduced_lottery_all.groupby('User_ID').size().reset_index(name='num_purchases')

print(len(reduced_user_pool))

plt.figure(figsize=(10, 6))
plt.plot(reduced_purchase_counts['num_purchases'])
plt.show()

reduced_lottery_all.to_csv('./data/reduced_lottery_all.csv', index=False)