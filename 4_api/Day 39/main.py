from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
flight_data = FlightData(flight_search.bring_deals())
data_manager = DataManager()
notification_manager = NotificationManager()

for deal in flight_data.price_list:
    old_data = data_manager.get_sheet(deal)
    # print(deal, old_data)
    if old_data:
        if int(deal["price"]) < int(old_data["price"]):
            message = notification_manager.formatted_message(deal["price"], deal["city"], deal["arrivalAirportCode"], deal["country"])
            notification_manager.send_message(message)
        data_manager.put_sheet(deal, old_data["id"])
    else:
        data_manager.post_sheet(deal)