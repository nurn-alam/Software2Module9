import random

class Car:
        def __init__(self, reg_number, max_speed):
                self.reg_number = reg_number
                self.max_speed = max_speed
                self.current_speed = 0
                self.travelled_distance = 0
        
        def accelerate(self, speed_change):
                self.current_speed += speed_change
                if self.current_speed < 0:
                        self.current_speed = 0
                elif self.current_speed > self.max_speed:
                        self.current_speed = self.max_speed
                
        def drive(self, hours):
                self.travelled_distance += self.current_speed * hours

# Race cars
race_cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    reg_number = f"ABC-{i}"
    race_cars.append(Car(reg_number, max_speed))


hours = 0
race_continue = True

while race_continue:
    hours += 1

    for car in race_cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_continue = False
            winner = car


print(f"The winner is {winner.reg_number}!")
print(f"{'Reg Number':<14}{'Max Speed':>10}{'Current Speed':>18}{'Distance':>11}")
for car in race_cars:
    print(f"{car.reg_number:<12}{car.max_speed:>10}"
          f"{car.current_speed:>15}{car.travelled_distance:>15.1f}")
