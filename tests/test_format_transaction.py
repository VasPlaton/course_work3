from src.utils import format_transaction

TEST_OPERATIONS = [
    {'id': 863064926, 'state': 'EXECUTED', 'date': '08.12.2019',
     'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Открытие вклада', 'to': 'Счет **5907'},
    {'id': 114832369, 'state': 'EXECUTED', 'date': '07.12.2019',
     'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'Visa 2842 78** **** 9012', 'to': 'Счет **3655'},
    {'id': 154927927, 'state': 'EXECUTED', 'date': '19.11.2019',
     'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод организации', 'from': 'Maestro 7810 46** **** 5568', 'to': 'Счет **2869'},
    {'id': 482520625, 'state': 'EXECUTED', 'date': '13.11.2019',
     'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод со счета на счет', 'from': 'Счет **9794', 'to': 'Счет **8125'},
    {'id': 801684332, 'state': 'EXECUTED', 'date': '05.11.2019',
     'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Открытие вклада', 'to': 'Счет **8381'}
]


def test_format_transaction():
    result = format_transaction(TEST_OPERATIONS)
    assert isinstance(result, list)
    assert result == [
        "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD\n",
        "07.12.2019 Перевод организации\nVisa 2842 78** **** 9012 -> Счет **3655\n48150.39 USD\n",
        "19.11.2019 Перевод организации\nMaestro 7810 46** **** 5568 -> Счет **2869\n30153.72 руб.\n",
        "13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.\n",
        "05.11.2019 Открытие вклада\nСчет **8381\n21344.35 руб.\n",
    ]
