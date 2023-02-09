from saver.saver import Saver
from sql_app.Employment.models import Emp, EmpSk
from sql_app.database import get_db
from sql_app.Stack.models import Stack


class JobSaver(Saver):
    db = get_db()

    def _save(self):
        for item in self._list:
            if self.get_user_by_id(item['emp_id']):
                self.save_stack_by_emp(item)
                emp_data = {'emp_id': item['emp_id'], 'emp_title': item['emp_title'],
                            'register_date': item['register_date'], 'dead_line': item['dead_line'],
                            'creer': item['creer'], 'company_fk': item['company_id']}
                emp = Emp(**emp_data)
                self.db.add(emp)
                self.db.commit()
                self.db.refresh(emp)

    def get_user_by_id(self, id: str) -> bool:
        return self.db.query(Emp).filter(Emp.emp_id == id).first() is None

    def save_stack_by_emp(self, item: dict) -> None:
        for target in item['labels']:
            value = self.db.query(Stack).filter(Stack.stack_name == target).first()
            label = {'emp_fk': item['emp_id'], 'stack_fk': value.stack_id}
            emp_sk = EmpSk(**label)
            self.db.add(emp_sk)
        self.db.commit()
        #self.db.refresh(emp_sk)
            # value = self.db.query(Stack).filter(Stack.stack_name == target).first()
            # if value is not None:
            #     result.append(str(value.stack_id))
