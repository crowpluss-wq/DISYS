def verify_tracking_codes(package_files):
    REQUIRED_CODE = "G1234567890"  # Normalized for comparison
    results = []
    for file in package_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            occurrences = content.count(REQUIRED_CODE)
            if occurrences == 1:
                status = "SUCCESS"
            elif occurrences == 0:
                status = "MISSING"
            else:
                status = f"DUPLICATE ({occurrences})"
        results.append((file, status))

    # The tracking code must appear exactly once per asset file across all channels
    if any(res[1] != "SUCCESS" for res in results):
        raise ValueError("Verification failed: Not all files have a single occurrence of the tracking code.")
    return results

def verify_deployment():
    channel_files = [
        'deploy/youtube.md',
        'deploy/instagram_morning.md',
        'deploy/instagram_afternoon.md',
    ]
    try:
        verification_results = verify_tracking_codes(channel_files)
        print("Verification successful for all assets.")
    except ValueError as e:
        print(f"Error during deployment verification: {e}")
        raise

if __name__ == "__main__":
    verify_deployment()