class Truck:
    def __init__(self, speed, capacity, load, packages, mileage, address, depart_time):
        self.speed = speed
        self.capacity = capacity
        self.weight = weight
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.speed, self.capacity, self.weight, self.packages, self.mileage,
                                               self.address, self.depart_time)