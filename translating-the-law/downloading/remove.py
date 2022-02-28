import os

def delete_case_files(case):
    main_text_file = f"{case}-main-text.pdf"
    press_summary_file = f"{case}-press-summary.pdf"
    os.system(f"rm -rf {main_text_file}")
    os.system(f"rm -rf {press_summary_file}")