cinema = {
   'Пятница': {
        12: 250,
        16: 350,
        20: 450
    },
   'Чемпионы': {
       10: 250,
       13: 350,
       16: 350
   },
   'Пернатая банда': {
       10: 350,
       14: 450,
       18: 450
   }
}
##################################################
movie = input("Пятница, Чемпионы, Пернатая банда? ")
datetime = input("сегодня или завтра? ")

def get_time(movie):
    if movie in cinema.keys():
        lst = list(cinema[movie].keys())
        return lst

    else:
        print('There is no this movie')

times = get_time(movie)
time = int(input(f'Pick time: {", ".join([str(i) for i in times])}: '))

def get_prices(time, times):
    if time in times:
       return cinema[movie][time]
    else:
        return 'There is no this time'


count = int(input('How many tickets?: '))
price = get_prices(time, times)

total_list = lambda movie, count, time, date, price : f'''
    movie: {movie},
    tickets: {count},
    time: {time},
    date: {date},
    total price: {count * price} rub
'''

def get_discount_price(price, percent):
    return price - (price * (percent / 100))


def get_total(movie, count, time, datetime, price):
    if datetime == 'сегодня' and count < 20:
        return total_list(movie, count, time, datetime, price)
    elif count > 20:
        return total_list(movie, count, time, datetime, get_discount_price(price, 20))
    elif datetime == 'завтра':
        return total_list(movie, count, time, datetime, get_discount_price(price, 5))
    else:
        'Somehting went wrong'

print(get_total(movie, count, time, datetime, price))


