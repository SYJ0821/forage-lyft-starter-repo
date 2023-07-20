from abc import ABC

from car import Car


# Service criteria : Once every 2 years

class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        return self.current_date - self.last_service_date >= 365*2  # 待修改