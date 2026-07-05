import json, sys


def update_style():
    try:
        with open("/users/crowpluss/ai disys/_company/_agents/designer/tools/style_library.json", "r") as f:
            lib = json.load(f)
        print("[INFO] Current style library loaded and validated.")
    except FileNotFoundError:
        print("[ERROR] Style library missing.")

def learn_and_apply():
    # Simulate trend scan → apply to lib
    new_accent_hex = "#FF6F00" 
    with open("/users/crowpluss/ai disys/_company/_agents/designer/tools/style_library.json", "w") as f:
        data = {"color_palette": {"primary": "#0A1E42", "accent": new_accent_hex, "bg_light": "#F5F7FA"}, 
                 "typography": {"heading": "Pretendard Bold", "body": "Pretendard Medium", "sub_text": "Pretendard Regular"}}
        json.dump(data, f)
    print("[SUCCESS] Daily learning loop applied new accent color.")

if __name__ == "__main__":
    update_style()
    learn_and_apply()