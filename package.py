class Package:
    def __init__(self, ID, address, city, zip, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.zip, self.deadline, self.weight, self.status)