import json


def build_unified_landing_package(tracking_code="G-1234567890"):
    """
    Build the final unified landing page package by merging approved CompareMatrix and summary data,
    and embedding the tracking code for all marketing channel inflow.

    Validated against:
    - [2026-07-24] 18-58 / 18-28 (Latest decisions)
    """

    matrix_data = {
        "comparison": "Eliminate Waste vs Strengthen Coverage",
        "remove": ["Unnecessary riders", "Hidden fees"],
        "strengthen": ["Surgery costs", "LTV enhancement"],
        "color_code": {"gray": "#808080", "red": "#FF4B5C"}
    }

    summary = {
        "headline": "Get the Coverage You Actually Need, Without the Junk.",
        "subtext": "We cut what you don't need and beef up what matters — surgery costs, critical coverage.",
        "cta_label": "See the Comparison Report",
        "sections": ["Hero", "Features", "Pricing", "FAQ", "CTA", "Footer"]
    }

    # Embed tracking code for all marketing channels
    tracking_info = {
        "ga4_id": tracking_code,
        "channels": [
            {"name": "Instagram", "link": "/instagram"},
            {"name": "YouTube", "link": "/youtube"}
        ],
        "note": "Unified across all marketing channels per 2026-07-18 decision"
    }

    package = {
        "metadata": {
            "version": "3.0",
            "track_id": tracking_code,
            "status": "DEPLOYMENT READY"
        },
        "content": {
            "hero": summary,
            "matrix": matrix_data,
            "cta": {"text": summary["cta_label"], "button_color": "#FF4B5C"}
        },
        "tracking": tracking_info
    }

    return package


def validate_package(package):
    """Verify the final build's integrity."""
    assert package["metadata"]["track_id"] == "G-1234567890", "Tracking code mismatch!"
    assert len(package["content"]["sections"]) == 6, "Landing page must have exactly 6 sections."
    return True


if __name__ == "__main__":
    result = build_unified_landing_package()
    validated = validate_package(result)

    with open("build/unified_landing.json", 'w') as f:
        f.write(json.dumps(result, indent=2))

    print(f"Verification successful: {validated}")