from bs4 import BeautifulSoup
import xlwt
import urllib.request

url = "https://www.serebii.net/sunmoon/pokemon.shtml"

thePage = urllib.request.urlopen(url)
soupData = BeautifulSoup(thePage,"html.parser")


def main():

    book = xlwt.Workbook()
    sheet = book.add_sheet('Test')
    book.save('Text.xls')

    sheet.write(0, 0, 'test')

    book.save('Text.xls')


    x = 721
    for img in soupData.findAll('img'):
        x = x +1
        if (x < 810):
            temp = img.get('src')

            temp = "https://www.serebii.net/Shiny/SM/" + str(x) + ".png"
            print(temp)



main()