from pdfminer.high_level import extract_text
from translating_the_law.downloading.get_details import details_new, details_old
from bs4 import BeautifulSoup
import requests

def extract_judgement(case):
    main_text_file = f"{case}-main-text.pdf"
    judgement = extract_text(main_text_file)
    return judgement

def extract_press_summary(case, post2016):
    if not post2016:
        press_summary_file = f"{case}-press-summary.pdf"
        summary = extract_text(press_summary_file)
    else:
        url = f"https://www.supremecourt.uk/press-summary/{case}.html"
        html = requests.get(url).content
        soup = BeautifulSoup(html)
        for script in soup(["script", "style"]):
            script.decompose()
        strips = list(soup.stripped_strings)
        summary = {}
        for i, strip in enumerate(strips):
            judges = 0
            background = 0
            judgment = 0
            reasons = 0
            if strip == "Justices":
                print(i)
                judges = i
                print(strip)
            elif strip == "Background to the Appeal":
                print(i)
                background = i
                print(strip)
            elif strip == "Judgment":
                print(i)
                judgment = i
                print(strip)
            elif strip == "Reasons for the Judgment":
                print(i)
                reasons = i
                print(strip)
            summary["Press summary"] = "".join(strips[:judges])
            summary["Justices"] = "".join(strips[judges+1:background])
            summary["Background to the appeal"] = "".join(strips[background+1:judgment])
            summary["Judgment"] = "".join(strips[judgment+1:reasons])
            summary["Reasons for the judgment"] = "".join(strips[reasons + 1:])
    return summary

def extract_details(case):
    url = f"https://www.supremecourt.uk/press-summary/{case}.html"
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    strips = list(soup.stripped_strings)
    if 'Facts' in strips:
        details = details_new(strips)
    else:
        details = details_old(strips)
    details['URL'] = url
    return details

def extract_all(case, post2016):
    j = extract_judgement(case)
    ps = extract_press_summary(case, post2016)
    d = extract_details(case)
    return j, ps, d

if __name__ == "__main__":
    print(extract_press_summary('uksc-2021-0062', True))
