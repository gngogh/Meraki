import yaml
from yaml.loader import SafeLoader

class conf:

    def __init__(self, f):
        self.f = f

    def data(self):
        with open(self.f) as file:
            data = yaml.load(file, Loader=SafeLoader)
        file.close()
        return data

