class Visitor:
    def __init__(self, _id, name, address, phone_number):
        self.id = _id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phoneNumber': self.phone_number
        }
