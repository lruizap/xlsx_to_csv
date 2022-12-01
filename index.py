import os
from pd_xls_to_csv import *
from xlsx_to_csv import *

dir = '.'
ls = os.listdir(dir)
documents = []

for file in ls:
    documents.append(file)

if documents.__contains__('E4.xlsx'):
    pd_xls_to_csv('E4.xlsx')
else:
    print('Introduzca el fichero "E4.xlsx"')
