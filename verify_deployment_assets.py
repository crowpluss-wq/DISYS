def verify_deployment_assets(channels=["youtube", "instagram"]):
    tracking_code = "G-1234567890"
    results = []

    for channel in channels:
        asset = get_channel_asset(channel)  # 내부 함수로 가정
        if asset is None:
            status = "MISSING"
            summary = "No assets found for this channel"
        else:
            try:
                is_valid = validate_all_policies(asset, tracking_code)
                status = "VALID" if is_valid else "INVALID"
                summary = f"{'Pass' if is_valid else 'Fail'} - All policies checked"
            except Exception as e:
                status = "ERROR"
                summary = str(e)

        results.append({
            "channel": channel,
            "status": status,
            "summary": summary
        })

    return results