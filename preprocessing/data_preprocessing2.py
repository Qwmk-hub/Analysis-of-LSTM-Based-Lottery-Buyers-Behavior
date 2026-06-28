import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


draw_based_lottery = pd.read_csv('./data/draw_based_lottery.csv')
instant_lottery = pd.read_csv('./data/instant_lottery.csv')
online_lottery = pd.read_csv('./data/online_lottery.csv')
pension_lottery = pd.read_csv('./data/pension_lottery.csv')


dataframes = [draw_based_lottery, instant_lottery, online_lottery,pension_lottery]

lottery_all = pd.concat(dataframes, ignore_index=True)

lottery_all.sort_values(by=['User_ID'], inplace=True,ignore_index=True)
print(lottery_all)


lottery_all.to_csv('./data/lottery_all.csv', index=False)