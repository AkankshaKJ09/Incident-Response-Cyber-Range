def generate_report(logs, alerts, actions):
    report = "==== INCIDENT RESPONSE REPORT ====\n\n"

    report += "LOGS:\n"
    for l in logs:
        report += f"{l}\n"

    report += "\nALERTS:\n"
    for a in alerts:
        report += f"{a}\n"

    report += "\nACTIONS:\n"
    for act in actions:
        report += f"{act}\n"

    return reports