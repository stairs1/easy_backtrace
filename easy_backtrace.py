import sys
import traceback
from tabulate import tabulate
import re


"""
for exception tabulation on all exceptions
"""
def custom_except_format(exc_type, exc_value, exc_traceback):
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

    print('\nTraceback:')
    tb = traceback.extract_tb(exc_traceback).format()
    traceback_list = [re.split(r',|\n', stack_info)[:4] for stack_info in tb]

    for index, stack in enumerate(traceback_list):
        traceback_list[index][0] = stack[0][7:]  # filename format
        traceback_list[index][1] = stack[1][6:]  # line number format
        traceback_list[index][2] = stack[2][4:]  # namespace format
        traceback_list[index][3] = stack[3][4:]  # statement format

    table_headers = ['file path', 'line #', 'namespace', 'offending statement']
    print(tabulate(traceback_list, headers=table_headers))

    return

sys.excepthook = custom_except_format


"""
for custom formatting from within a try except block: 

print('\nTraceback:')
    tb = traceback.extract_tb(sys.exc_info()[2]).format()
    traceback_list = [re.split(r',|\n', stack_info)[:4] for stack_info in tb]

    for index, stack in enumerate(traceback_list):
        traceback_list[index][0] = stack[0][7:]  # filename format
        traceback_list[index][1] = stack[1][6:]  # line number format
        traceback_list[index][2] = stack[2][4:]  # namespace format
        traceback_list[index][3] = stack[3][4:]  # statement format

    table_headers = ['file path', 'line #', 'namespace', 'offending statement']
    print(tabulate(traceback_list, headers=table_headers))
"""
