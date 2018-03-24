import xlrd 

workbook_bitcoin = xlrd.open_workbook('bitcoin_data.xlsx')
workbook_video_games = xlrd.open_workbook('shippment_data.xlsx')
workbook_shippment = xlrd.open_workbook('video_game_sales.xlsx')

time_bitcoin = sheet['A']
price_bitcoin = sheet['B']
time_video_games = sheet['A']
sales_video_games = sheet['A']
time_shippment = sheet['A']
shipments_shippment = sheet['B']

