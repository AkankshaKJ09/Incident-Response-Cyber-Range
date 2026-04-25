import json

def detect_threats():
    alerts = []
    failed = 0

    try:
        with open("logs.json", "r") as f:
            lines = f.readlines()
    except:
        return alerts

    for line in lines:
        try:
            log = json.loads(line.strip())
        except:
            continue

        if log["event"] == "LOGIN_FAILED":
            failed += 1

        if log["event"] == "MALWARE_EXECUTION":
            alerts.append("⚠ Malware Detected")

        if log["event"] == "DATA_EXFILTRATION":
            alerts.append("⚠ Data Exfiltration Detected")

    if failed >= 5:
        alerts.append("⚠ Brute Force Attack Detected")

    return alerts