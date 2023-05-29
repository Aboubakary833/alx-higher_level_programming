#!/usr/bin/python3

def safe_print_division(a, b):
    value = 0
    try:
        value = a / b
    except (ZeroDivisionError, TypeError):
        value = None
    finally:
        print("Inside result: {}".format(value))
    return value
