class Airplane:

    def __init__(self, make, model, year, max_speed):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed
        self.__odometer = 0
        self.__is_flying = False

    def take_off(self):
        self.is_flying = True
        get_take_off = f'{self.__make} {self.__model} of year {self.__year} is taking of to the air'
        return get_take_off

    def fly(self, distance):
        self.__odometer += distance
        get_fly = f'{self.__make} {self.__model} of year {self.__year} is flying with the max speed of {self.__max_speed}'
        get_odometer = f'The odometer sign shows {self.__odometer}'
        return get_fly, get_odometer


    def land(self):
        self.is_flying = False
        get_land = f'The {self.__make} {self.__model} of year {self.__year} is landed.'
        return get_land


airplane1 = Airplane('Boeing', '737', 2018, 900)
print(airplane1.take_off())
print(airplane1.fly(1000))
print(airplane1.land())

print(airplane1.take_off())
print(airplane1.fly(3000))
print(airplane1.land())