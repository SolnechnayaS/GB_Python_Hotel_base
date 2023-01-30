import logging

def employee_true(any_string):
    match any_string:
        case '1':
            return True
        case '0':
            return False
        case _:
            return employee_true(input ("Является сотрудником 1 - да, 0 - нет: "))
