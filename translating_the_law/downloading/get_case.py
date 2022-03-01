from translating_the_law.downloading.download import get_case_files
from translating_the_law.downloading.remove import delete_case_files
from translating_the_law.downloading.extract import extract_all
from translating_the_law.downloading.parse import parse_all

def get_case(base_url):
    pdf_url = base_url.replace('.html', '-judgment.pdf').replace('cases/', 'cases/docs/')
    summary_url = base_url.replace('.html', '-press-summary.pdf').replace('cases/', 'cases/docs/')
    case = base_url.replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    post2016 = False
    if int(base_url[39:43]) >= 2017:
        post2016 = True
    get_case_files(case, summary_url, pdf_url, post2016)
    j , ps = extract_all(case, post2016)
    delete_case_files(case, post2016)
    return parse_all(j, ps, summary_url)

if __name__ == "__main__":
    test = get_case('https://www.supremecourt.uk/cases/uksc-2009-0119.html')
    print(test)