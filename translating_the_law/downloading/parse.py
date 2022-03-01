import re

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

def parse_all(judgement, summary, summary_url):
    j = judgement_to_dict(judgement)
    ps = summary_to_dict(summary, summary_url)
    return {'judgement':j, 'press summary':ps}