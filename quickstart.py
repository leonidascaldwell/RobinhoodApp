from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import robin_stocks.robinhood as rs
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
                            range="sheet1!A2:E75").execute()
values = result.get('values', [])

rs.login(username=os.environ['rs_username'],
         password=os.environ['rs_password'],
         expiresIn=3600,
         by_sms=True)

positions = rs.account.build_holdings()

print(positions)
#if not values:
#    print('No data found.')
#else:
#    print('Success')
#for row in values:
#   print('%s, %s' % (row[0], row[4]))
#    print("rs.orders.order_buy_fractional_by_price('%s', %s, timeInForce='gtc', extendedHours=False)"
#          % (row[0], row[4]))
#    print("rs.orders.order_buy_fractional_by_price('%s', row[4], timeInForce='gtc', extendedHours=False) % row[0]")
#    print(str(row[0]))
#    print(int(row[4]))

