from components.cleanser import Cleanser
from stack_list import eratos




class WantedCleanser(Cleanser):
    CleansedData = {}
    def __init__(self, _dict: dict) -> None:
        self.dict = _dict
    #company, lables, start_time,due_time,career,location
    def _cleanser(self)->dict:
        return self.get_list_cleansedData()
    def get_list_cleansedData(self)->list:
        data_list = []
        for job_id in self.dict.keys():
            cleansed_data = {}
            job_data = self.dict[job_id]
            cleansed_data['country'] = job_data['address']['country']
            cleansed_data['company_name'] = job_data['company_name']
            cleansed_data['company_id'] = job_data['company_id']
            cleansed_data['labels'] = self.get_stack(job_data['jd'])
            cleansed_data['team_name'] = job_data['company_name']
            cleansed_data['dead_line'] = job_data['due_time']
            cleansed_data['register_date'] = job_data['confirm_time']
            cleansed_data['creer'] = job_data['is_newbie']
            cleansed_data['location'] = job_data['location']
            cleansed_data['logo'] = job_data['logo_img']
            cleansed_data['emp_id'] = job_id
            cleansed_data['emp_title'] = job_data['position']
            data_list.append(cleansed_data)
        return data_list
    def get_stack(self, jd:str) -> list:
        stack = []
        for word in eratos:
            if word in jd.lower():
                stack.append(word)
        return stack
