from pdfminer.high_level import extract_text

def extract_judgement(case):
    main_text_file = f"{case}-main-text.pdf"
    judgement = extract_text(main_text_file)
    return judgement

def extract_press_summary(case):
    press_summary_file = f"{case}-press-summary.pdf"
    summary = extract_text(press_summary_file)
    return summary

def extract_all(case):
    j = extract_judgement(case)
    ps = extract_press_summary(case)
    return j, ps