from translating_the_law.downloading.download import get_case_files
from translating_the_law.downloading.remove import delete_case_files
from translating_the_law.downloading.extract import extract_all
from translating_the_law.downloading.parse import parse_all

def get_case(base_url):
    pdf_url = base_url.replace('.html', '-judgment.pdf').replace('cases/', 'cases/docs/')
    summary_url = base_url.replace('.html', '-press-summary.pdf').replace('cases/', 'cases/docs/')
    case = base_url.replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    year_bool = False
    if int(base_url[39:43]) >= 2017:
        year_bool = True
    get_case_files(case, summary_url, pdf_url, year_bool)
    j , ps , d , ad = extract_all(case, year_bool)
    delete_case_files(case, year_bool)
    return parse_all(j, ps, summary_url, d, ad)

if __name__ == "__main__":
    test = get_case('https://www.supremecourt.uk/cases/uksc-2009-0119.html')
    test2 = get_case('https://www.supremecourt.uk/cases/uksc-2021-0160.html')
    print(test2['details'], test2['additional'])
