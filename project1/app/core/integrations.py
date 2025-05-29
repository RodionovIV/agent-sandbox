from .database import get_db_session
from .utils import sync_external_services

def integrate_with_crm(request_id):
    session = next(get_db_session())
    request = session.query(Request).get(request_id)
    # логика синхронизации с CRM
    sync_external_services(request)
    