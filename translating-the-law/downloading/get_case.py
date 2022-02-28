from download import get_case_files
from remove import delete_case_files
from extract import extract_all
from parse import parse_all

def get_case(base_url):
    pdf_url = base_url.replace('.html', '-judgment.pdf').replace('cases/', 'cases/docs/')
    summary_url = base_url.replace('.html', '-press-summary.pdf').replace('cases/', 'cases/docs/')
    case = base_url.replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    get_case_files(case, summary_url, pdf_url)
    j , ps = extract_all(case)
    delete_case_files(case)
    return parse_all(j, ps)

if __name__ == "__main__":
    test = get_case('https://www.supremecourt.uk/cases/uksc-2009-0119.html')
    print(test)