from components.cleanser import Cleanser


class WantedCleanser(Cleanser):
    def __init__(self, _dict: dict) -> dict:
        self.dict = _dict
    #company, lables, start_time,due_time,career,location
    def _cleanser(self):
        pass

    def validate(self):
        #we have to proof self.dict has all of columns we want
        pass