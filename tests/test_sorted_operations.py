from src.utils import sorted_operations

TEST_FILTERED_OPERATIONS = [
    {"id": 1, "state": "EXECUTED", "date": "2021-01-01", "description": "Transaction 1"},
    {"id": 2, "state": "EXECUTED", "date": "2021-02-01", "description": "Transaction 2"},
    {"id": 3, "state": "EXECUTED", "date": "2021-03-01", "description": "Transaction 3"},
    {"id": 4, "state": "EXECUTED", "date": "2021-04-01", "description": "Transaction 4"},
    {"id": 5, "state": "EXECUTED", "date": "2021-05-01", "description": "Transaction 5"},
    {"id": 6, "state": "EXECUTED", "date": "2021-06-01", "description": "Transaction 6"},
]


def test_sorted_operations_with_valid_data():
    result = sorted_operations(TEST_FILTERED_OPERATIONS)
    assert isinstance(result, list)
    assert len(result) == 5
    assert result == [
        {"id": 6, "state": "EXECUTED", "date": "2021-06-01", "description": "Transaction 6"},
        {"id": 5, "state": "EXECUTED", "date": "2021-05-01", "description": "Transaction 5"},
        {"id": 4, "state": "EXECUTED", "date": "2021-04-01", "description": "Transaction 4"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01", "description": "Transaction 3"},
        {"id": 2, "state": "EXECUTED", "date": "2021-02-01", "description": "Transaction 2"},
    ]


def test_sorted_operations_with_empty_data():
    result = sorted_operations([])
    assert result == []
