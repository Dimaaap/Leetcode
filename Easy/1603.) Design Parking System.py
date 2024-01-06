class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def add_car(self, car_type: int):
        self.slots[car_type] = count = max(self.slots[car_type]-1, -1)
        return count > -1
