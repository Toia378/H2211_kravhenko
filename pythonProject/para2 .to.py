import random

class Student:

    def __init__(self, name):
        self.name = name
        self. gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("ime to studu")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print(" will sleep")
        self.gladness += 3

    def to_chill(self):
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Caet out...")
            self.alive = False
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
    def  end_of_day(self):
       print(f"GLadnes = {self.gladness}")
       print(f"Progress = {self.gladness}")


    def live (self, day):
           day = f"Day {day} of {self.name} life"
           print(f"{day:^50}")
           live_cude = random.randint(1,3)
           if live_cude ==1:
                self.to_study()
           elif live_cude == 2:
                self.to_sleep()
           elif live_cude == 3:
                self.to_chill()
           self.end_of_day()
           self.is_alive()


personage = Student(name="Vasya")

for day in range(365):
    if personage.alive == False:
        break
    personage.live(day)