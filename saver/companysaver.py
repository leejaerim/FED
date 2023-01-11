from saver.saver import Saver
from sql_app.Company.models import Company
from sql_app.database import get_db


class CompanySaver(Saver):
    db = get_db()

    def _save(self):
        for item in self._list:
            if self.get_item_by_id(item['company_id']):
                # del item['company_name']

                del item['labels']
                del item['team_name']
                del item['dead_line']
                del item['register_date']
                del item['creer']
                item['emp_fk'] = item['emp_id']
                del item['emp_id']
                del item['emp_title']
                company = Company(**item)
                self.db.add(company)
                self.db.commit()
                self.db.refresh(company)

    def get_item_by_id(self, id: str) -> bool:
        return self.db.query(Company).filter(Company.company_id == id).first() is not None
