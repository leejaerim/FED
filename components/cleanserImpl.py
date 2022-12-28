from components.cleanser import Cleanser
from stack_list import eratos


class WantedCleanser(Cleanser):
    def __init__(self, _dict: dict) -> None:
        self.dict = _dict
    #company, lables, start_time,due_time,career,location
    def _cleanser(self)->None:
        pass


    def validate(self):
        #we have to proof self.dict has all of columns we want
        pass
    def get_stack(self) -> list:
        stack = []
        for word in eratos:
            if word in self.dict['jd'].lower():
                stack.append(word)
        return stack
