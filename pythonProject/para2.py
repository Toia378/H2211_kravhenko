class Student:
    def __init__(self, h=160):
        self.h = h


nick = Student()
kate = Student(h=170)

print(nick.h)
print(kate.h)
