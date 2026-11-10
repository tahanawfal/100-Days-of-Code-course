class FlightData:
    # 2. This class is responsible for structuring the flight data.
    def __init__(self, unformatted_data):
        self.price_list = []

        if "error" in unformatted_data:
            print("API error:", unformatted_data["error"])
            return
        for deal in unformatted_data.get("deals"):
            self.price_list.append({
                "country": deal.get("country"),
                "city": deal.get("name"),
                "arrivalAirportCode": deal.get("arrival_airport_code"),
                "price": deal.get("price")
                })