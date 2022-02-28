from pandas_jsonlines.read_jsonlines import read_jsonlines
from get_case import get_case
import pandas as pd
import numpy as np
import os

base_path = os.path.dirname(os.path.realpath(__file__))
links_path = os.path.join(base_path, "..", "..", "notebooks", "links.jsonlines")


def get_data(num=5):
    case_links = read_jsonlines(links_path)
    if num > 1010:
        raise ValueError("Not enough cases")
    if num == 0:
        num = 1010
    data = []
    for i in range(num):
        base_url = np.array(case_links)[i][0].split()[2][:-1]
        case = get_case(base_url)
        data.append(case)
    return data

if __name__ == "__main__":
    print(get_data()[0])