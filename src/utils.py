import json
from datetime import datetime


def open_file(operations):
    """открываем файл operations.json и возвращает данные в понятном для питона виде
    :param operations:
    """
    with open(operations, 'r', encoding="UTF=8") as file:
        file = json.load(file)
    return file


def filter_file(file):
    """фильтруем файл по EXECUTED"""
    new_data = []
    for item in file:
        if not item:
            continue
        elif item['state'] == 'EXECUTED':
            new_data.append(item)
    return new_data


def sorted_operations(new_data):
    """сортируем отфильтрованный файл и возвращаем 5 последних операций"""
    sorted_date = sorted(new_data, key=lambda x: x['date'], reverse=True)
    last_operations = sorted_date[:5]
    return last_operations


def format_date(file):
    """форматируем дату и время в требуемый вид"""
    for item in file:
        python_date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
        item['date'] = python_date.strftime('%d.%m.%Y')
    return file


def format_account(file):
    """скрываем номер счета и карты"""
    for item in file:
        _from = item.get('from')
        if _from is not None:
            if _from.startswith('Счет'):
                item['from'] = 'Счет **' + _from[-4:]
            else:
                numbers = _from.split()[-1]
                card_name = _from.split()[0]
                item['from'] = f"{card_name} {numbers[:4]} {numbers[5:7]}** **** {numbers[-4:]}"
        _to = item.get('to')
        if _to.startswith('Счет'):
            item['to'] = 'Счет **' + _to[-4:]
        else:
            numbers_to = _to.split()[-1]
            card_name_to = _to.split()[0]
            item['to'] = f"{card_name_to} {numbers_to[:4]} {numbers_to[5:7]}** **** {numbers_to[-4:]}"
    return file


def format_transaction(file):
    """форматируем чек для отображения в личном кабинете"""
    format_trans = []
    for item in file:
        date = item['date']
        description = item['description']
        summ_from = f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"
        if 'from' in item:
            from_to = f"{item['from']} -> {item['to']}"
        else:
            from_to = item['to']
        format_trans.append(f"{date} {description}\n{from_to}\n{summ_from}\n")
    return format_trans
