# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает 
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. 
# Если адрес не валиден, выбросить исключение ValueError
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
# В Domain part обязательно должна быть хотя бы одна точка.
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; 
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

def email_parse(mail):
    RE_MAIL = re.compile(r'(?P<username>[\w\d\'\.\+\-\_]+)@(?P<domain>[\w\-]+\.[\w\-\.]+)')
    try:
        usr = RE_MAIL.match(mail).group('username')
        dmn = RE_MAIL.match(mail).group('domain')
        res = {'username': usr, 'domain': dmn}
        return res
    except: raise ValueError(f'wrong e-mail: {mail}')


# Test
# mail_lst = ["iselickiy@ynadex.ru", "1resea2rch@att.net", "daveed@mac.com", "kspiteri@msn.com", "iamc'al@aol.com", "linux.hack@yahoo.ca", "jgmye_rs@att.net", "bwcart+y@aol.com", "jonatha-n@yahoo.ca", 
# "kobayasi@yah-oo.com", "syrinx@yahoo.co-m", "b'd.b_r+o-wn@mac.co.m", "metzzo@hotmail.com"]

# for mail_ad in mail_lst:
#     print(email_parse(mail_ad))