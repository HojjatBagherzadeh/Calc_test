from Code_Ver_01 import User

user1 = User()
print(user1.__dict__)

user1.activate()
print(user1.is_active())

user1.add_points(25)
print(user1.get_points())

print("User total points: {}".format(user1.get_points()))
print("User level: {}".format(user1.get_level()))