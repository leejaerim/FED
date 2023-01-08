from abc import ABC, abstractmethod
class Saver(ABC):
    def __init__(self, _list:list):
        self._list = _list
    def save(self):
        return self._save()
    @abstractmethod
    def _save(self):
        pass



