from abc import ABC, abstractmethod

class Cleanser(ABC):
    def cleanser(self):
        return self._cleanser()

    @abstractmethod
    def _cleanser(self):
        pass
