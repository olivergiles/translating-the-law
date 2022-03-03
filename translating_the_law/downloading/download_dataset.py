import pandas as pd
from pandas_jsonlines.read_jsonlines import read_jsonlines
import requests
from translating_the_law.downloading.get_details import details_new, details_old
import urllib.request
import os
import re
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import json

base_path = os.path.dirname(os.path.realpath(__file__))
links_path = os.path.join(base_path, "..", "..", "notebooks", "all.jsonlines")

def get_cleanlinks():
    links = read_jsonlines(links_path)
    clean_links = []
    for link in links.dropna().iterrows():
        sc_link = "https://www.supremecourt.uk"
        base_url = link[1]['link'].split()[2][:-1].strip()
        j_link = link[1]['judgment_link'].strip()
        s_link = link[1]['pdf_link'].strip()
        if j_link.startswith("/cases/docs"):
            j_link = sc_link + j_link
        elif j_link.startswith("docs/"):
            j_link = sc_link + "/cases/" + j_link
        else:
            j_link = sc_link + "/cases/docs" + j_link
        if s_link.endswith(".html"):
            s_link = sc_link + s_link
        elif s_link.startswith("/cases"):
            s_link = sc_link + s_link
        else:
            s_link = sc_link + "/cases/" + s_link
        clean_links.append({"base":base_url, "judgment":j_link, "summary":s_link})
        #if link[0] == 318 or  link[0] == 333 or  link[0] == 413:
        #    x = requests.get(j_link)
        #    if x.status_code != 200:
        #        print(link[0], j_link)
        #    x = requests.get(s_link)
        #    if x.status_code != 200:
        #        print(link[0], s_link)
    return clean_links

def alt_extract_judgement(case):
    main_text_file = f"{case}-main-text.pdf"
    judgement = extract_text(main_text_file)
    return judgement

def alt_extract_press_summary(case, html_link=None):
    if not html_link:
        press_summary_file = f"{case}-press-summary.pdf"
        summary = extract_text(press_summary_file)
    else:
        url = html_link
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

def alt_extract_details(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    strips = list(soup.stripped_strings)
    if 'Facts' in strips:
        details = details_new(strips)
    else:
        details = details_old(strips)
    details['URL'] = url
    return details

def alt_get_case_files(links):
    case = links['base'].replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    main_text_file = f"{case}-main-text.pdf"
    press_summary_file = f"{case}-press-summary.pdf"
    urllib.request.urlretrieve(links['judgment'], main_text_file)
    if links['summary'].endswith(".pdf"):
        urllib.request.urlretrieve(links['summary'], press_summary_file)

def alt_delete_case_files(links):
    case = links['base'].replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    main_text_file = f"{case}-main-text.pdf"
    press_summary_file = f"{case}-press-summary.pdf"
    os.system(f"rm -rf {main_text_file}")
    if links['summary'].endswith(".pdf"):
        os.system(f"rm -rf {press_summary_file}")

def alt_extract_judgement(case):
    case = case['base'].replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
    main_text_file = f"{case}-main-text.pdf"
    judgement = extract_text(main_text_file)
    return judgement

def alt_extract_press_summary(case):
    if case['summary'].endswith(".pdf"):
        case = case['base'].replace('.html', '').replace('https://www.supremecourt.uk/cases/','')
        press_summary_file = f"{case}-press-summary.pdf"
        summary = extract_text(press_summary_file)
    else:
        url = case['summary']
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

def alt_extract_details(case):
    url = case['base']
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    strips = list(soup.stripped_strings)
    if 'Facts' in strips:
        details = details_new(strips)
    else:
        details = details_old(strips)
    details['URL'] = url
    return details

def alt_extract_all(case):
    j = alt_extract_judgement(case)
    ps = alt_extract_press_summary(case)
    d = alt_extract_details(case)
    return j, ps, d

def judgement_to_dict(judgement):
    judgement = judgement.replace("\n", "").strip()
    return {"body":judgement}

def summary_to_dict(summary, summary_url):
    summary_regex = r"PRESS SUMMARY(.*)JUSTICES:(.*)BACKGROUND TO THE APPEAL(.*)JUDGMENT(.*)REASONS FOR THE JUDGMENT(.*)"
    summary = summary.replace("\n", "").strip()
    search = re.search(summary_regex,summary,flags=re.M)
    if search:
        return {
            "Press summary":search.group(1).strip(),
            "Justices":search.group(2).strip(),
            "Background to the appeal":search.group(3).strip(),
            "Judgment":search.group(4).strip(),
            "Reasons for the judgment":search.group(5).strip()
        }
    return {"error": summary_url}

def parse_all(judgement, summary, summary_url, details):
    j = judgement_to_dict(judgement)
    if type(summary) != dict:
        ps = summary_to_dict(summary, summary_url)
    else:
        ps = summary
    d = details
    return {'judgement':j, 'press summary':ps, 'details':d}

def download_dataset(test=False):
    save_base_path = os.path.dirname(os.path.realpath(__file__))
    save_path = os.path.join(save_base_path, "..","..", "raw_data", "data.json")
    links = get_cleanlinks()
    data = []
    i = 0
    for case in links:
        i += 1
        if test and i>=5:
            break
        alt_get_case_files(case)
        j, ps, d = alt_extract_all(case)
        data.append(parse_all(j, ps, case['summary'],d))
        alt_delete_case_files(case)
    json_string = json.dumps(data)
    with open(save_path, 'w') as outfile:
        json.dump(json_string, outfile)
    return data

if __name__ == "__main__":
    download_dataset()