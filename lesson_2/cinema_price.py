movie = input("Пятница, Чемпионы, Пернатая банда? ")
date = input("сегодня или завтра? ")

def get_time(movie):
    if movie == 'Пятница':
        return int(input('12, 16, 20 '))
    elif movie == 'Чемпионы':
        return int(input('10, 13, 16 '))
    elif movie == 'Пернатая банда':
        return int(input('10, 14, 18 '))

def get_tickets_count():
    return int(input('How many tickets? '))

time = get_time(movie)
count = get_tickets_count()

total_list = lambda movie, count, time, date, price : f'''
    movie: {movie},
    tickets: {count},
    time: {time},
    date: {date},
    total price: {count * price} rub
'''

def get_discount_price(price, percent):
    return price - (price * (percent / 100))



def get_total(date, time, count, movie):
    if date == 'сегодня' and count < 20:
        if movie == 'Пятница':
            if time == 12:
                return total_list(movie, count, time, date, 250)
            elif time == 16:
                return total_list(movie, count, time, date, 350)
            elif time == 20:
                return total_list(movie, count, time, date, 450)

        elif movie == 'Чемпионы':
            if time == 10:
                return total_list(movie, count, time, date, 250)
            elif time == 13 or time == 16:
                return total_list(movie, count, time, date, 350)

        elif movie == 'Пернатая банда':
            if time == 10:
                return total_list(movie, count, time, date, 350)
            elif time == 14 or time == 18:
                return total_list(movie, count, time, date, 450)

    elif date == 'сегодня' and count >= 20:
        if movie == 'Пятница':
            if time == 12:
                return total_list(movie, count, time, date, get_discount_price(250, 20))
            elif time == 16:
                return total_list(movie, count, time, date, get_discount_price(350, 20))
            elif time == 20:
                return total_list(movie, count, time, date, get_discount_price(450, 20))

        elif movie == 'Чемпионы':
            if time == 10:
                return total_list(movie, count, time, date, get_discount_price(250, 20))
            elif time == 13 or time == 16:
                return total_list(movie, count, time, date, get_discount_price(350, 20))

        elif movie == 'Пернатая банда':
            if time == 10:
                return total_list(movie, count, time, date, get_discount_price(350, 20))
            elif time == 14 or time == 18:
                return total_list(movie, count, time, date, get_discount_price(450, 20))

    elif date == 'завтра':
        if movie == 'Пятница':
            if time == 12:
                return total_list(movie, count, time, date, get_discount_price(250, 5))
            elif time == 16:
                return total_list(movie, count, time, date, get_discount_price(350, 5))
            elif time == 20:
                return total_list(movie, count, time, date, get_discount_price(450, 5))

        elif movie == 'Чемпионы':
            if time == 10:
                return total_list(movie, count, time, date, get_discount_price(250, 5))
            elif time == 13 or time == 16:
                return total_list(movie, count, time, date, get_discount_price(350, 5))

        elif movie == 'Пернатая банда':
            if time == 10:
                return total_list(movie, count, time, date, get_discount_price(350, 5))
            elif time == 14 or time == 18:
                return total_list(movie, count, time, date, get_discount_price(450, 5))




print(get_total(date, time, count, movie))


