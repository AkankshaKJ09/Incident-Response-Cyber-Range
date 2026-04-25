def respond(alerts):
    actions = []

    for a in alerts:
        if "Brute Force" in a:
            actions.append("✔ Account Locked")

        if "Malware" in a:
            actions.append("✔ Process Terminated")

        if "Exfiltration" in a:
            actions.append("✔ Network Blocked")

    return actions