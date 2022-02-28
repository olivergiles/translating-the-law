from black import Dict
from translating_the_law.downloading.get_case import get_case

def test_onecase():
    case = get_case('https://www.supremecourt.uk/cases/uksc-2009-0119.html')
    assert(type(case) == dict)