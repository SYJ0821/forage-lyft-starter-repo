from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tireweararray):
        self.tireweararray = tireweararray

    def needs_service(self):
        if max(self.tireweararray) >= 0.9:
            return True
        else:
            return False