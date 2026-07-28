import re
from pathlib import Path

TRACKING_CODE = "G-1234567890"

def update_comparison_matrix(report_path):
    content = ""
    try:
        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error: report file not found"

    # Latest data from writer's summary (actual values filled in matrix)
    replacements = {
        r"\b(진단비)\b": r"120만 원",
        r"\b(수술비)\b": r"350 만 원",
        r"\b(입원일당)\b": r"8.5 만 원",
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    # Remove duplicate tracking codes and ensure single insertion at the end of each file
    files_to_process = [
        Path("reports/insurance_comparison_matrix_final.md"),
        Path("deployments/youtube.md"),
        Path("deployments/instagram_morning.md"),
        Path("deployments", dir_mode=True), # For glob search below
    ]

    for file in files_to_process:
        if not file.is_dir():
            path = str(file)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()

            # Remove existing trackers to avoid duplicates
            text = re.sub(rf'Tracking Code:\s*{TRACKING_CODE}', '', text)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(text + f"\n\n[System Info]\nTracking Code: {TRACKING_CODE}\n")

    return "Update successful"

if __name__ == "__main__":
    update_comparison_matrix("reports/insurance_comparison_matrix_final.md")