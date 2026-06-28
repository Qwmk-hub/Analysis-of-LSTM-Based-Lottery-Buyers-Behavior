import os
import pandas as pd
import numpy as np
from numba import jit

draw_based_lottery_1 = pd.read_csv('./data/draw_based_lottery/240801-3_01.csv')
draw_based_lottery_2 = pd.read_csv('./data/draw_based_lottery/240801-3_02.csv')
draw_based_lottery_3 = pd.read_csv('./data/draw_based_lottery/240801-3_03.csv')

draw_based_lottery_1.columns = ['User_ID',    'Date',    'Time',    'Price']
draw_based_lottery_2.columns = ['User_ID',    'Date',    'Time',    'Price']
draw_based_lottery_3.columns = ['User_ID',    'Date',    'Time',    'Price']

dataframes = [draw_based_lottery_1, draw_based_lottery_2, draw_based_lottery_3]
draw_based_lottery = pd.concat(dataframes, ignore_index=True)


for idx, row in draw_based_lottery.iterrows():

    if idx % 10000==0:
        print(idx)

    #raw_data = draw_based_lottery.iloc[idx]['Date']
    raw_data=draw_based_lottery.at[idx, 'Date']

    raw_data = raw_data - 20240000
    day = raw_data % 100
    month = raw_data // 100
    if month==1:
        date= day
    elif month==2:
        date = day + 31
    elif month == 3:
        date = day + 31 + 29
    elif month == 4:
        date = day + 31 + 29 + 31
    else:
        print(month, day)

    draw_based_lottery.at[idx, 'Date'] = date

draw_based_lottery.to_csv('./data/draw_based_lottery.csv', index=False)

#############################

instant_lottery_1 = pd.read_csv('./data/instant_lottery/240801-4_01.csv')
instant_lottery_2 = pd.read_csv('./data/instant_lottery/240801-4_02.csv')
instant_lottery_3 = pd.read_csv('./data/instant_lottery/240801-4_03.csv')

instant_lottery_1.columns = ['User_ID',    'Date',    'Time',    'Price']
instant_lottery_2.columns = ['User_ID',    'Date',    'Time',    'Price']
instant_lottery_3.columns = ['User_ID',    'Date',    'Time',    'Price']

dataframes = [instant_lottery_1, instant_lottery_2, instant_lottery_3]
instant_lottery = pd.concat(dataframes, ignore_index=True)

for idx, row in instant_lottery.iterrows():
    if idx%10000==0:
        print(idx)

    raw_data = instant_lottery.iloc[idx]['Date']

    raw_data = raw_data - 20240000
    day = raw_data % 100
    month = raw_data // 100
    if month==1:
        date= day
    elif month==2:
        date = day + 31
    elif month == 3:
        date = day + 31 +29
    elif (month == 4):
        date = day + 31 + 29 + 31
    else:
        print(month, day)

    instant_lottery.at[idx,'Date'] = date



instant_lottery.to_csv('./data/instant_lottery.csv', index=False)

#############################
pension_lottery_2 = pd.read_csv('./data/pension_lottery/240801-5_02.csv')
pension_lottery_3 = pd.read_csv('./data/pension_lottery/240801-5_03.csv')
pension_lottery_4 = pd.read_csv('./data/pension_lottery/240801-5_04.csv')
pension_lottery_5 = pd.read_csv('./data/pension_lottery/240801-5_05.csv')
pension_lottery_6 = pd.read_csv('./data/pension_lottery/240801-5_06.csv')
pension_lottery_7 = pd.read_csv('./data/pension_lottery/240801-5_07.csv')
pension_lottery_8 = pd.read_csv('./data/pension_lottery/240801-5_08.csv')

pension_lottery_2.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_3.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_4.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_5.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_6.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_7.columns = ['User_ID',    'Date',    'Time',    'Price']
pension_lottery_8.columns = ['User_ID',    'Date',    'Time',    'Price']

dataframes = [pension_lottery_2, pension_lottery_3, pension_lottery_4,
              pension_lottery_5,pension_lottery_6,pension_lottery_7,pension_lottery_8]
pension_lottery = pd.concat(dataframes, ignore_index=True)

for idx, row in pension_lottery.iterrows():
    if idx%10000==0:
        print(idx)

    raw_data = pension_lottery.iloc[idx]['Date']

    raw_data = raw_data - 20240000
    day = raw_data % 100
    month = raw_data // 100
    if month==1:
        date= day
    elif month==2:
        date = day + 31
    elif month == 3:
        date = day + 31 +29
    elif (month == 4):
        date = day + 31 + 29 + 31
    else:
        print(month, day)

    pension_lottery.at[idx,'Date'] = date

pension_lottery.to_csv('./data/pension_lottery.csv', index=False)

#############################
online_lottery_1 = pd.read_csv('./data/online_lottery/240801-6_01.csv')
online_lottery_2 = pd.read_csv('./data/online_lottery/240801-6_02.csv')
online_lottery_3 = pd.read_csv('./data/online_lottery/240801-6_03.csv')
online_lottery_4 = pd.read_csv('./data/online_lottery/240801-6_04.csv')
online_lottery_5 = pd.read_csv('./data/online_lottery/240801-6_05.csv')
online_lottery_6 = pd.read_csv('./data/online_lottery/240801-6_06.csv')
online_lottery_7 = pd.read_csv('./data/online_lottery/240801-6_07.csv')
online_lottery_8 = pd.read_csv('./data/online_lottery/240801-6_08.csv')
online_lottery_9 = pd.read_csv('./data/online_lottery/240801-6_09.csv')
online_lottery_10 = pd.read_csv('./data/online_lottery/240801-6_10.csv')
online_lottery_11 = pd.read_csv('./data/online_lottery/240801-6_11.csv')
online_lottery_12 = pd.read_csv('./data/online_lottery/240801-6_12.csv')

online_lottery_1.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_2.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_3.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_4.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_5.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_6.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_7.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_8.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_9.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_10.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_11.columns = ['User_ID',    'Date',    'Time',    'Price']
online_lottery_12.columns = ['User_ID',    'Date',    'Time',    'Price']


dataframes = [online_lottery_1, online_lottery_2, online_lottery_3,
              online_lottery_4, online_lottery_5, online_lottery_6,
              online_lottery_7, online_lottery_8, online_lottery_9,
              online_lottery_10, online_lottery_11, online_lottery_12]

online_lottery = pd.concat(dataframes, ignore_index=True)


for idx, row in online_lottery.iterrows():
    if idx%10000==0:
        print(idx)

    raw_data = online_lottery.iloc[idx]['Date']

    raw_data = raw_data - 20240000
    day = raw_data % 100
    month = raw_data // 100
    if month==1:
        date= day
    elif month==2:
        date = day + 31
    elif month == 3:
        date = day + 31 + 29
    elif (month == 4):
        date = day + 31 + 29 + 31
    else:
        print(month, day)

    online_lottery.at[idx,'Date'] = date

online_lottery.to_csv('./data/online_lottery.csv', index=False)