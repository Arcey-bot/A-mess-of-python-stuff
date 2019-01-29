from bs4 import BeautifulSoup
import xlwt
import xlrd
import urllib.request
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

url = "https://www.serebii.net/sunmoon/pokemon.shtml"

thePage = urllib.request.urlopen(url)
soupData = BeautifulSoup(thePage, "html.parser")


book = xlwt.Workbook()
sheet = book.add_sheet('Alola')
book.save('Shiny Alola.xls')


#sheet.write(0, 0, 'test')

#scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

#gc = gspread.authorize(credentials)

#wks = gc.open('Shiny').sheet1
y = 0
x = 721
for img in soupData.findAll('img'):
    x = x + 1
    if (x < 810):
        temp = img.get('src')

        temp = "https://www.serebii.net/Shiny/SM/" + str(x) + ".png"
        print(temp)
        #wks.append_row(['=image("' + temp + '",4,200,200)'])
        sheet.write(y, 0, '=image("' + temp + '",4,100,100)')
        book.save('Shiny Alola.xls')
        y = y + 1



