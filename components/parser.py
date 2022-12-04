from abc import ABC, abstractmethod

class Parser(ABC):
    def parse(self):
        return self._parse()

    @abstractmethod
    def _parse(self):
        pass
