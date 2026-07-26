def validate(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    track_id = "G-1234567890"
    remove_color = "#808080"
    enhance_color = "#FF4B5C"

    missing = track_id not in content
    invalid = remove_color not in content or enhance_color not in content
    return missing, invalid


def run_batch_check(paths):
    results = []
    for path in paths:
        status = validate(path)
        results.append((path, status[0], status[1]))

    errors = [res for res in results if not res[2]]
    if errors:
        print("Error in files with invalid contrast structure:", errors)
    return results