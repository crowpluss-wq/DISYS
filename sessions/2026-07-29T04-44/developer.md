def verify_deployment_assets(deployment_bundle):
    tracking_code = "G-1234567890"
    asset_count = 0

    for asset in deployment_bundle:
        content = open(asset, 'r', encoding='utf-8').read()
        if tracking_code not in content:
            with open(asset, 'a', encoding='utf-8') as f:
                f.write('\n' + tracking_code)
        elif content.count(tracking_code) > 1:
            lines = content.splitlines()
            unique_lines = []
            for line in lines:
                if tracking_code not in line or any(tracking_code in line for _ in range(2)): # Remove duplicate entries
                    unique_lines.append(line)
            with open(asset, 'w', encoding='utf-8') as f:
                f.write('\n'.join(unique_lines))
        else:
            asset_count += 1

    return asset_count