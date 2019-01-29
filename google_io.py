import gspread
import json
import xlwt
import xlrd
from oauth2client.service_account import ServiceAccountCredentials

book = xlwt.Workbook()
wb2 = xlrd.open_workbook('Shiny Kanto.xls')

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Shiny').sheet1

x = 13

sheet1 = wb2.sheet_by_name('Kanto')

while x < 164:
    curr = sheet1.row_values(x)
    print(curr)
    wks.append_row([curr])
    x = x + 1
