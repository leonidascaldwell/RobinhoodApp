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
                            range="sheet3!A2:E7").execute()
values = result.get('values', [])
print(values)
# Start of Robinhood - login
rs.login(username=os.environ['rs_username'],
         password=os.environ['rs_password'],
         expiresIn=3600,
         by_sms=True)

count = 0
for row in values:
    count = count + 1
    if count % 10 == 0:
        time.sleep(61)
        rs.orders.order_buy_fractional_by_price(row[0], int(row[3]), timeInForce='gfd', extendedHours=True)
        #rs.orders.order_buy_fractional_by_quantity(row[0], row[1], timeInForce='gfd', extendedHours=True)
        print(row[0] + " Complete")
    else:
        rs.orders.order_buy_fractional_by_price(row[0], int(row[3]), timeInForce='gfd', extendedHours=True)
        #rs.orders.order_buy_fractional_by_quantity(row[0], row[1], timeInForce='gfd', extendedHours=True)
        print(row[0] + " Complete")
print("SUCCESS!!!")
