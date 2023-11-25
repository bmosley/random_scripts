# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property   
    def get_temperature(self):
        print("Getting value...")
        return self.temperature


human = Celsius(37)
print(human.get_temperature)