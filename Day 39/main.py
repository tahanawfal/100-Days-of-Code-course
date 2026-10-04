#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from flight_search import FlightSearch

# airports = ['KUL', 'LGK', 'GYD', 'TBS', 'BUS', 'DPS', 'CGK', 'BKK', 'HKT', 'CMB', 'MNL', 'CEB', 'PPS', 'ENI', 'ZNZ', 'HAN', 'SGN', 'DAD', 'KTM', 'PKR', 'ALA']
# prices = []

# for airport in airports:
#   flight_search = FlightSearch("BGW", airport)
#   prices = prices.append({
#     "airport": airport,
#     "price": flight_search
#   })

# print(prices)

from test import FlightSearch
flight_search = FlightSearch()

flight_search.formatted_list()
