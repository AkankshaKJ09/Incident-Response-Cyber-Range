import json
from datetime import datetime

def write_log(event, details):
    log = {
        "timestamp": str(datetime.now()),
        "event": event,
        "details": details
    }

    with open("logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")