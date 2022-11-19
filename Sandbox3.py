from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import robin_stocks.robinhood as rs
import time
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = os.environ["service_account_file"]

credentials = None
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.environ['sample_spreadsheet_id']

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet2!A2:E14").execute()
values = result.get('values', [])

#########################################################################


rs.login(username='',
         password='',
         expiresIn=3600,
         by_sms=True)

#########################################################################

# positions = rs.account.build_holdings()

# print(positions)
# if not values:
#    print('No data found.')
# else:
#    print('Success')
# for row in values:
#   print('%s, %s' % (row[0], row[4]))
#    print("rs.orders.order_buy_fractional_by_price('%s', %s, timeInForce='gtc', extendedHours=False)"
#          % (row[0], row[4]))
#    print("rs.orders.order_buy_fractional_by_price('%s', row[4], timeInForce='gtc', extendedHours=False) % row[0]")
#    print(str(row[0]))
#    print(int(row[4]))

#request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                range="sheet2!A2:E75", valueInputOption="USER_ENTERED",
#                                body={"values": position_list}).execute()

#print(request)


# A simple task to do to each response object
#def do_something(response):
#    print(response.url)


# A list to hold our things to do via async

#count = 0
#for row in values:
#    count = count + 1
#    if count%5 == 0:
#        time.sleep(45)
#        order = rs.orders.order_buy_fractional_by_price(row[0], int(row[4]), timeInForce='gfd', extendedHours=True)
#        print(row[0] + " Complete")
#    else:
#        order = rs.orders.order_buy_fractional_by_price(row[0], int(row[4]), timeInForce='gfd', extendedHours=True)
#        print(row[0] + " Complete")

count = 0
for row in values:
    count = count + 1
    if count % 10 == 0:
        time.sleep(61)
        rs.orders.order_buy_fractional_by_price(row[0], int(row[4]), timeInForce='gfd', extendedHours=True)
        print(row[0] + " Complete")
    else:
        rs.orders.order_buy_fractional_by_price(row[0], int(row[4]), timeInForce='gfd', extendedHours=True)
        print(row[0] + " Complete")


# print(positions['GDDY']['price'])
# positions = json.dumps(positions)
# print(positions)
# position_dict = json.load(positions)
# print(positions)


# position_dict = json.load(positions)
# position_obj = Positions(**position_dict)

# print(position_obj[0].price)
