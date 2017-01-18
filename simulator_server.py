import server
import simulator_sensor


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.notifyClient(self)


# Example usage
class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.data = 0

    def setData(self, data):
        self.data = data
        self.notify()

    def getData(self):
        return self.data


class SimulationServer:
    def __init__(self):
        self.sensor_simulator = simulator_sensor.SimulatorSensor()

    def notifyClient(self, subject):
        # notify the client
        server.notifyClient('SimulationServer:  %s is %d' % (subject.name, subject.getData()))

    def getTemperature(self):
        return self.sensor_simulator.getTemperature()
