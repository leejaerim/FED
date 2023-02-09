from saver.saver import Saver
from sql_app.Company.models import Company
from sql_app.database import get_db


class CompanySaver(Saver):
    db = get_db()

    def _save(self):
        for item in self._list:
            if self.get_item_by_id(item['emp_id']):
                company_data = {'company_id': item['company_id'], 'company_name': item['company_name'],
                                'logo': item['logo'], 'location': item['location'], 'country': item['country'],'emp_fk': item['emp_id']}
                company = Company(**company_data)
                self.db.add(company)
                self.db.commit()
                self.db.refresh(company)

    def get_item_by_id(self, id: str) -> bool:
        return self.db.query(Company).filter(Company.emp_fk == id).first() is None
