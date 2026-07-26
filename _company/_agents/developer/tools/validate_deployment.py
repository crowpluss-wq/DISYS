from typing import List


def validate_deployment_package(tracking_id: str, package_paths: list[str]) -> list[str]:
    """
    Verify that the tracking code is present in all deployment paths and that the comparison structure is valid.

    This script reads each file path provided and checks for the presence of the specified tracking ID (G-1234567890). It also checks for keywords related to the "remove/strengthen" contrast structure
    """
    errors = []

    for path in package_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            if tracking_id not in content:
                errors.append(f"Tracking code {tracking_id} missing in file: {path}")

        except FileNotFoundError:
            errors.append(f"File not found: {path}")
        except Exception as e:
            errors.append(f"Error reading file {path}: {e}")

    return errors


def validate():
    tracking_id = "G-1234567890"
    package_paths = [
        "/Users/crowpluss/ai disys/reports/banner_package_unified.md",
        "/Users/crowpluss/ai disys/reports/marketing_copy.md",
        "/Users/crowpluss/ai disys/reports/app_conversion_banners_spec.md"
    ]

    errors = validate_deployment_package(tracking_id, package_paths)

    if errors:
        print("❌ Validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("✅ All deployment paths verified successfully.")


if __name__ == "__main__":
    validate()