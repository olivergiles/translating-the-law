from translating_the_law.downloading.get_data import get_data

def test_sevencase():
    seven = get_data()
    assert(len(seven)==7)
    assert(type(seven)==list)