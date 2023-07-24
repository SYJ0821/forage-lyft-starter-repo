from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tireweararray):
        self.tireweararray = tireweararray

    def needs_service(self):
        if sum(self.tireweararray) >= 3:
            return True
        else:
            return False