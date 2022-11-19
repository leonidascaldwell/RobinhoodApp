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
                            range="sheet3!A2:E100").execute()
values = result.get('values', [])

#########################################################################


rs.login(username=os.environ['rs_username'],
         password=os.environ['rs_password'],
         expiresIn=3600,
         by_sms=True)

positions = rs.account.build_holdings()

print(positions)
if not values:
   print('No data found.')
else:
   print('Success')
#for row in values:
#   print('%s, %s' % (row[0], row[4]))
#   print("rs.orders.order_buy_fractional_by_price('%s', %s, timeInForce='gtc', extendedHours=False)"
#          % (row[0], row[4]))
#   print("rs.orders.order_buy_fractional_by_price('%s', row[4], timeInForce='gtc', extendedHours=False) % row[0]")
#   print(str(row[0]))
#   print(int(row[4]))

position_list = []

for row in values:
    try:
        position_list.append([row[0], positions[row[0]]['quantity'], positions[row[0]]['equity']])
    except:
        position_list.append([row[0],0,0])

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="sheet3!A2:E100", valueInputOption="USER_ENTERED",
                                body={"values": position_list}).execute()

#print(request)

########################################################################################
# A simple task to do to each response object
#def do_something(response):
#    print(response.url)


# A list to hold our things to do via async
#async_list = [
#]

#for row in values:
    # The "hooks = {..." part is where you define what you want to do
    #
    # Note the lack of parentheses following do_something, this is
    # because the response will be used as the first argument automatically

    # Add the task to our list of things to do via async
    #async_list.append(action_item)
# Do our list of things to do via async
#try:
#    grequests.map(async_list)
#except:
#    print("something happened2")

# print(positions['GDDY']['price'])
# positions = json.dumps(positions)
# print(positions)
# position_dict = json.load(positions)
# print(positions)


# position_dict = json.load(positions)
# position_obj = Positions(**position_dict)

# print(position_obj[0].price)
