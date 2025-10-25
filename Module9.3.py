class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        travelled_distance = self.current_speed * hours
        self.travelled_distance += travelled_distance

car = Car("ABC-123" , 142)
car.accelerate(60)
car.drive(1.5)

print(f"Registration number: {car.reg_number:s}")
print(f"Maximum speed: {car.max_speed:d} km/h")
print(f"Current speed: {car.current_speed:d} km/h")
print(f"Distance travelled: {car.travelled_distance}")