# from covid import INFECTION_RATE
class Disease(object):
    def __init__(self, arg_name="UKNOWN DISEASE", infection_rate=.1, infection_radius=15):
        super().__init__()
        self.name = arg_name
        self.infection_rate = infection_rate
        self.infection_radius = infection_radius
        self.radius = 10
        print("New disease discovered !", self.name)

        # Any cells withing this radius are susceptible to be infected
        self.infection_radius = infection_radius
        # The chances of catching the disease if within the infection radius
        self.infection_rate = infection_rate

    def set_radius(self, radius):
        self.infection_radius = radius

    def set_infection_rate(self, infection_rate):
        self.infection_rate = infection_rate

    def get_name(self):
        return name

    def get_radius(self):
        return self.infection_radius

    def get_rate(self):
        return self.infection_rate
