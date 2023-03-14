from abc import ABC, abstractmethod
import pickle
import jsonpickle

class Persist(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def save(self, application):
        pass

    @abstractmethod
    def load(self):
        pass

class PersistBinary(Persist):
    def __init__(self) -> None:
        super().__init__()
        self._gagfile = './gag.bjson'

    def save(self, application):
        with open(self._gagfile, mode='wb') as bin_file:
            pickle.dump(application, bin_file)

    def load(self):
        with open(self._gagfile, mode='wb') as bin_file:
            application = pickle.load(bin_file)
        return application

class PersistJson(Persist):
    def __init__(self) -> None:
        super().__init__()
        self._gagfile = './gag.json'

    def save(self, application):
        with open(self._gagfile, 'w') as json_file:
            application_str = jsonpickle.encode(application)
            json_file.write(application_str)

    def load(self):
        application = None
        try:
            with open(self._gagfile, 'r') as json_file:
                application_str = json_file.read()
                application = jsonpickle.decode(application_str)
        except:
            print('Unable to load file')
        return application