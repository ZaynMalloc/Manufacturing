from openpyxl import load_workbook

workbook_bitcoin = load_workbook('bitcoin_data.xlsx')
workbook_video_games = load_workbook('video_game_sales.xlsx')
workbook_shippment = load_workbook('shippment_data.xlsx')

active_bitcoin = workbook_bitcoin.active
active_video_games = workbook_video_games.active
active_shippment = workbook_shippment.active

time_bitcoin = active_bitcoin['A1:A24']
price_bitcoin = active_bitcoin['B1:B24']

time_video_games = active_video_games['A1:A24']
sales_video_games = active_video_games['B1:B24']

time_shippment = active_shippment['A1:A24']
amount_shippment = active_shippment['B1:B24']

