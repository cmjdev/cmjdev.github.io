import sys
import json
import datetime

try:
    update = sys.argv[1]
except:
    update = None

if not update:
    update = input("What are you interested in? ")
update = update.strip()

timestamp = datetime.datetime.now()

if update:
    update = {"interest": update, "date": timestamp.strftime("%Y%m%d")}

    try:
        with open("./updates.json", "r") as f:
            updates = json.load(f)
    except:
        updates = []

    updates.append(update)

    try:
        with open("./updates.json", "w") as f:
            json.dump(updates, f)
    except:
        pass