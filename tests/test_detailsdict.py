from translating_the_law.downloading.get_case import get_case

def test_details():
    test_uksc = get_case('https://www.supremecourt.uk/cases/uksc-2011-0110.html')
    assert(len(test_uksc)==3)
    assert(type(test_uksc['details'])==dict)
    assert(len(test_uksc['details'])==6)
