import random


class SimulatorSensor:
    # randomly generating temperature
    def getTemperature(self):
        random.seed()
        return (random.randint(25, 28))
