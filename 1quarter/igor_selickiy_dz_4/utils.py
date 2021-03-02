import datetime
from decimal import Decimal
import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

def currency_rates(valute, site=response):
    res = None
    for elem in site.split('<Valute ID'):
        if valute in elem:
            course = Decimal(elem[elem.find('<Value>'):elem.find('</Value>')].split('>')[1].replace(",", "."))
            res = course.quantize(Decimal('1.00'))
    if res:
        date = site[site.find('Date="'):site.find('" name="Foreign Currency Market"')].split('"')[1].split('.')
        date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
        print(res, date)
    else:
        print(res)