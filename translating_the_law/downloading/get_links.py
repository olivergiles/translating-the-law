from pandas_jsonlines.read_jsonlines import read_jsonlines
import numpy as np
import os

base_path = os.path.dirname(os.path.realpath(__file__))
links_path = os.path.join(base_path, "..", "..", "notebooks", "links.jsonlines")

def get_links():
    case_links = read_jsonlines(links_path)
    return np.array(case_links)
