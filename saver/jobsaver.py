from saver.saver import Saver
from sql_app.Employment.models import Emp
from sql_app.database import get_db


class JobSaver(Saver):
    db = get_db()
    def _save(self):
        for item in self._list:
            if not self.get_user_by_id(item['emp_id']):
                del item['company_name']
                del item['labels']
                del item['team_name']
                del item['location']
                emp = Emp(**item)
                self.db.add(emp)
                self.db.commit()
                self.db.refresh(emp)
    def get_user_by_id(self,id: str) -> bool:
        return self.db.query(Emp).filter(Emp.emp_id == id).first() is not None