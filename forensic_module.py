import json

def get_logs():
    data = []

    try:
        with open("logs.json", "r") as f:
            for line in f:
                try:
                    data.append(json.loads(line.strip()))
                except:
                    continue
    except:
        pass

    return data