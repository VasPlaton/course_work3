from src.utils import format_account

TEST_OPERATIONS_WITH_ACCOUNTS = [
    {"id": 1, "state": "EXECUTED", "from": "Счет 1234567890123456", "to": "Счет 9876543210987654",
     "description": "Transaction 1"},
    {"id": 2, "state": "EXECUTED", "from": "MasterCard 1234 5678 9012 3456", "to": "Счет 9876543210987654",
     "description": "Transaction 2"},
    {"id": 3, "state": "EXECUTED", "from": "Visa 9876 5432 1098 7654", "to": "Visa 4321 0987 6543 2109",
     "description": "Transaction 3"},
]


def test_format_account():
    result = format_account(TEST_OPERATIONS_WITH_ACCOUNTS)
    assert isinstance(result, list)
    for item in result:
        assert 'from' in item
        assert 'to' in item
        if item['from'].startswith('Счет'):
            assert item['from'] == f'Счет **{item["from"][-4:]}'
        else:
            assert item['from'] == f"{item['from'].split()[0]} {item['from'].split()[-1][:4]} {item['from'].split()[-1][5:7]}** **** {item['from'].split()[-1][-4:]}"

        if item['to'].startswith('Счет'):
            assert item['to'] == f'Счет **{item["to"][-4:]}'
        else:
            assert item['to'] == f"{item['to'].split()[0]} {item['to'].split()[-1][:4]} {item['to'].split()[-1][5:7]}** **** {item['to'].split()[-1][-4:]}"
