class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f"Engine: {self.engine_type}"


class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return f"Transmission: {self.transmission_type}"


class Body:
    def __init__(self, body_type, color):
        self.body_type = body_type
        self.color = color

    def __str__(self):
        return f"Body: {self.body_type}, Color: {self.color}"


class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return f"Car:\n  {self.engine}\n  {self.transmission}\n  {self.body}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def get_car(self):
        return self.car

    def build_engine(self, engine_type):
        engine = Engine(engine_type)
        self.car.set_engine(engine)

    def build_transmission(self, transmission_type):
        transmission = Transmission(transmission_type)
        self.car.set_transmission(transmission)

    def build_body(self, body_type, color):
        body = Body(body_type, color)
        self.car.set_body(body)


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        pass


class SedanBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def construct_car(self):
        self.build_engine("V4")
        self.build_transmission("Automatic")
        self.build_body("Sedan", "Red")
        return self.get_car()


class SUVBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def construct_car(self):
        self.build_engine("V6")
        self.build_transmission("Automatic")
        self.build_body("SUV", "Black")
        return self.get_car()


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def construct_car(self):
        self.build_engine("V8")
        self.build_transmission("Manual")
        self.build_body("Sports Car", "Yellow")
        return self.get_car()


sedan_builder = SedanBuilder()
sedan = sedan_builder.construct_car()
print("Создан седан:", sedan)

suv_builder = SUVBuilder()
suv = suv_builder.construct_car()
print("Создан SUV:", suv)

sports_car_builder = SportsCarBuilder()
sports_car = sports_car_builder.construct_car()
print("Создан Sports Car:", sports_car)
