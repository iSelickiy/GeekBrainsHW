while True:
    dur_input = input('Input seconds("q" = stop): ')

    if dur_input == 'q':
        break

    duration = int(dur_input)

    day = 86400
    hour = 3600
    minute = 60
    second = 1
    result = []

    d = int(duration / day)
    h = int((duration % day) / hour)
    m = int((duration % hour) / minute)
    s = int((duration % minute) / second)

    if duration >= day:
        print(d, 'd', h, 'hr',  m, 'min', s, 'sec')
    elif duration >= hour:
        print(h, 'hr', m, 'min', s, 'sec')
    elif duration>= minute:
        print(m, 'min', s, 'sec')
    elif duration >= second:
        print(s, 'sec')
    else:
        print('error')
