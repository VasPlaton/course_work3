from src.utils import filter_file


TEST_OPERATIONS = [
    {"id": 1, "state": "EXECUTED", "description": "Transaction 1"},
    {"id": 2, "state": "PENDING", "description": "Transaction 2"},
    {"id": 3, "state": "EXECUTED", "description": "Transaction 3"},
    {"id": 4, "state": "FAILED", "description": "Transaction 4"}
]


def test_filter_file_with_executed_state():
    result = filter_file(TEST_OPERATIONS)
    assert isinstance(result, list)
    assert len(result) == 2
    for item in result:
        assert 'id' in item
        assert 'state' in item
        assert 'description' in item
        assert item['state'] == 'EXECUTED'


def test_filter_file_with_empty_list():
    result = filter_file([])
    assert result == []


def test_filter_file_with_no_executed_state():
    test_data = [
        {"id": 1, "state": "PENDING", "description": "Transaction 1"},
        {"id": 2, "state": "FAILED", "description": "Transaction 2"}
    ]
    result = filter_file(test_data)
    assert result == []
