from components.cleanser import Cleanser
from stack_list import stack_list, option_stack


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
        for word in self.dict['jd'].replace('\n', '').split(' '):
            if word.lower() in stack_list:
                # target resemble one of option stack
                if word.lower() in option_stack.keys():
                    word = option_stack[word.lower()]
                stack.append(word)
        return stack
