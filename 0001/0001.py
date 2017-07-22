# coding=utf-8
import string
import random

def gen_activation_code(length, number):
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = []
    while len(code)<number:
        key = ''
        for i in range(length):
            key += random.choice(base)
            if key in code:
                continue
        code.append(key)
    return code

print(gen_activation_code(16, 5))