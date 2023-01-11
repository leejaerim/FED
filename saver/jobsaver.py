from saver.saver import Saver
from sql_app.Employment.models import Emp
from sql_app.database import get_db
from sql_app.Stack.models import Stack


class JobSaver(Saver):
    db = get_db()
    def _save(self):
        for item in self._list:
            if not self.get_user_by_id(item['emp_id']):
                del item['company_id']
                del item['company_name']
                del item['team_name']
                del item['location']
                del item['country']
                del item['logo']
                item['stack_fk'] = self.get_stack_id_by_label(item['labels'])
                del item['labels']
                emp = Emp(**item)
                self.db.add(emp)
                self.db.commit()
                self.db.refresh(emp)

    def get_user_by_id(self, id: str) -> bool:
        return self.db.query(Emp).filter(Emp.emp_id == id).first() is not None

    def get_stack_id_by_label(self, label_list: list) -> str:
        result = []
        for target in label_list:
            value = self.db.query(Stack).filter(Stack.stack_name == target).first()
            if value is not None:
                result.append(str(value.stack_id))
        return ",".join(result)
