# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# получить список кортежей вида: 
# (<remote_addr>, <request_type>, <requested_resource>).
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания. 
# Спамер — это клиент, отправивший больше всех запросов; 
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

def parser(file_name, spam_count):
    res_lst = []
    all_ip = {}
    spam_ip = []
    with open(file_name, 'r', encoding='utf-8') as f:
        str_gen = (el for el in f)
        for work_str in str_gen:
            remote_addr = work_str[0:work_str.find(' - - ')]
            request_type = work_str[work_str.find('] "'):work_str.find(' /')].split('"')[1]
            requested_resource = work_str[work_str.find(' /d') - 3:work_str.find(' HT')].split()[1]
            if remote_addr in all_ip:
                all_ip[remote_addr] += 1
            else:
                all_ip[remote_addr] = 1
            res_lst.append((remote_addr, request_type, requested_resource))

    for key, value in all_ip.items():
        if value > spam_count:
            spam_ip.append(key)
    with open('unic_ip.txt', 'w', encoding='utf-8') as f:
        for elem in all_ip:
            f.write(f'{elem}\n')
    with open('spam_ip.txt', 'w', encoding='utf-8') as f:
        for elem in spam_ip:
            f.write(f'{elem}\n')


parse_file_name = 'nginx_logs.txt'
spam_counter = 1000 # How many requests from ip to add in spam list
parser(parse_file_name,spam_counter)
