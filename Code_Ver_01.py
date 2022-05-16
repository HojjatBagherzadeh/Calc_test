class User:

    def __init__(self):
        self.profile = {'active': False, 'level': 1, 'points': 0}

    def activate(self):
        self.profile['active'] = True

    def is_active(self):
        return self.profile['active']

    def get_level(self):
        return self.profile['level']

    def get_points(self):
        return self.profile['points']

    def add_points(self, additional_points):
        self.profile['points'] += additional_points

        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2


user1 = User()
print(user1.__dict__)

user1.activate()
print(user1.is_active())

user1.add_points(25)
print(user1.get_points())

print("User total points: {}".format(user1.get_points()))
print("User level: {}".format(user1.get_level()))
user1.add_points(205)
print("User total points: {}".format(user1.get_points()))
print("User level: {}".format(user1.get_level()))


