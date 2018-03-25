from openpyxl import load_workbook
import pandas as pd
import numpy as np

#Load workbooks
workbook_bitcoin = pd.read_excel('bitcoin_data.xlsx', sheet_name = 0, usecols = 1)
workbook_video_games = pd.read_excel('video_game_data.xlsx', sheet_name = 0, usecols = 1)
workbook_shippment = pd.read_excel('shippment_data.xlsx', sheet_name = 0, usecols = 1)

print(workbook_video_games)

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

