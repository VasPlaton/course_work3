from utils import *

operations = 'operations.json'

of = open_file(operations)
ff = filter_file(of)
so = sorted_operations(ff)
fd = format_date(so)
fa = format_account(fd)
ft = format_transaction(fa)

for item in ft:
    print(item)
