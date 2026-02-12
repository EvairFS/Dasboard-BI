from config import USE_MOCK

if USE_MOCK:
    from utils.mock_data import get_mock_data as get_data
else:
    from utils.db_connection import get_data