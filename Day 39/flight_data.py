class FlightData:
    # 3. This class is responsible for structuring the flight data.
    def formatted_list(self):
        if "error" in self.raw_data:
            print("API error:", self.raw_data["error"])
            return
        for deal in self.raw_data.get("deals", []):
            print(deal.get("name"), deal.get("price"))