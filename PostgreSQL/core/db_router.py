from hr.models import Employee
from sales.models import Sale

HR_MODELS = [Employee]
SALES_MODELS = [Sale]

class DBRouter(object):

    def db_for_read(self, model, **hints):
        if model in HR_MODELS:
            return 'hr'
        elif model in SALES_MODELS:
            return 'sales'
        return None

    def db_for_write(self, model, **hints):
        if model in HR_MODELS:
            return 'hr'
        elif model in SALES_MODELS:
            return 'sales'
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in ('hr', 'sales'):
            if app_label == 'hr' and db == 'hr':
                return True
            elif app_label == 'sales' and db == 'sales':
                return True
            # Allow migration for other databases that might not be explicitly mentioned
            return False
        # Allow migration for the default database or any other database not explicitly mentioned
        return True