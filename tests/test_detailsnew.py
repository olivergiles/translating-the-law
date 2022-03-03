from translating_the_law.downloading.get_case import get_case

def test_newcase_details():
    test_uksc = get_case('https://www.supremecourt.uk/cases/uksc-2020-0076.html')
    assert(len(test_uksc)==4)
    assert(type(test_uksc['details'])==dict)
    assert(len(test_uksc['details'])==6)
    assert(type(test_uksc['additional'])==dict)
