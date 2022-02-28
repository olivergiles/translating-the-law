from translating_the_law.downloading.get_data import get_data

def test_fivecase():
    five = get_data()
    assert(len(five)==5)
    assert(type(five)==list)