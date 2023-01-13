from saver.saver import Saver
from sql_app.Employment.models import Emp
from sql_app.database import get_db
from sql_app.Stack.models import Stack


class JobSaver(Saver):
    db = get_db()

    def _save(self):
        for item in self._list:
            if self.get_user_by_id(item['emp_id']):
                emp_data = {'emp_id': item['emp_id'], 'emp_title': item['emp_title'],
                            'register_date': item['register_date'], 'dead_line': item['dead_line'],
                            'creer': item['creer'], 'stack_fk': self.get_stack_id_by_label(item['labels'])}
                emp = Emp(**emp_data)
                self.db.add(emp)
                self.db.commit()
                self.db.refresh(emp)

    def get_user_by_id(self, id: str) -> bool:
        return self.db.query(Emp).filter(Emp.emp_id == id).first() is None

    def get_stack_id_by_label(self, label_list: list) -> str:
        result = []
        for target in label_list:
            value = self.db.query(Stack).filter(Stack.stack_name == target).first()
            if value is not None:
                result.append(str(value.stack_id))
        return ",".join(result)
