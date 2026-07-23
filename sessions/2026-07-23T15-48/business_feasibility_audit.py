def audit_deployment():
    content = open('reports/banner_package_unified.md').read()

results = []
if "내보험다보아" in content:
    results.append("✅ CTA confirmed")
else:
    results.append("❌ CTA missing")

tracking_count = content.count('[INSERT TRACKING CODE HERE]')
if tracking_count == 1:
    results.append(f"✅ Tracking count: {tracking_count}")
elif tracking_count > 1:
    results.append(f"⚠️ Duplicate tracking found ({tracking_count})")
else:
    results.append("❌ No tracking tag found")

print('\n'.join(results))

if all("✅" in r for r in results):
    return "APPROVED — ready for multi-channel push."
return "REJECTED — fix audit issues first."