import os

def delete_case_files(case, post2016):
    main_text_file = f"{case}-main-text.pdf"
    press_summary_file = f"{case}-press-summary.pdf"
    os.system(f"rm -rf {main_text_file}")
    if not post2016:
        os.system(f"rm -rf {press_summary_file}")