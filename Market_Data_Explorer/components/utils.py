import random
import string
from fmp.constants import *
import pandas as pd


def random_string(string_length=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def humanize(str_):
    return " ".join(list(map(str.capitalize, str_.lower().split('_'))))


def generate_dropdown_options(values):
    labels = list(map(humanize, values))
    return [{"label": labels[i], "value": values[i]} for i in range(len(labels))]


if __name__ == '__main__':
    x = generate_dropdown_options([key for key in FUNDS.keys()])
    print(x)
