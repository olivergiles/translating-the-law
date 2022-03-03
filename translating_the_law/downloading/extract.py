from pdfminer.high_level import extract_text
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
        judges = 0
        background = 0
        judgment = 0
        reasons = 0
        for i, strip in enumerate(strips):
            if strip == "Justices":
                judges = i
            elif strip == "Background to the Appeal":
                background = i
            elif strip == "Judgment":
                judgment = i
            elif strip == "Reasons for the Judgment":
                reasons = i
        summary["Press summary"] = "".join(strips[:judges])
        summary["Justices"] = "".join(strips[judges+1:background])
        summary["Background to the appeal"] = "".join(strips[background+1:judgment])
        summary["Judgment"] = "".join(strips[judgment+1:reasons])
        summary["Reasons for the judgment"] = "".join(strips[reasons + 1:])
    return summary

def extract_all(case, post2016):
    j = extract_judgement(case)
    ps = extract_press_summary(case, post2016)
    return j, ps

if __name__ == "__main__":
    print(extract_press_summary('uksc-2021-0062', True))