import xlrd 

workbook_bitcoin = xlrd.open_workbook('bitcoin_data.xlsx')
workbook_video_games = xlrd.open_workbook('shippment_data.xlsx')
workbook_bitcoin = xlrd.open_workbook('video_game_sales.xlsx')

time_bitcoin = workbook_bitcoin['A']
price_bitcoin = workbook_bitcoin['B']
time_video_games = workbook_video_games['A']
sales_video_games = workbook_video_games['A']
time_shippment = workbook_shippment['A']
shipments_shippment = workbook_shippment['B']

print(time_bitcoin)