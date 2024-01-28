from datetime import datetime
from src.utils import format_date

TEST_OPERATIONS_WITH_DATES = [
    {"id": 1, "state": "EXECUTED", "date": "2021-01-01T12:34:56.789000", "description": "Transaction 1"},
    {"id": 2, "state": "EXECUTED", "date": "2021-02-01T13:45:23.456000", "description": "Transaction 2"},
    {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:56:34.123000", "description": "Transaction 3"},
]


def test_format_date():
    result = format_date(TEST_OPERATIONS_WITH_DATES)
    assert isinstance(result, list)
    for item in result:
        assert 'date' in item
        assert isinstance(item['date'], str)
        expected_date_format = '%d.%m.%Y'
        formatted_date = datetime.strptime(item['date'], expected_date_format).strftime(expected_date_format)
        assert item['date'] == formatted_date
