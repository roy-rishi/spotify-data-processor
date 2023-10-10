import json
from datetime import datetime, timezone

# a sample to be edited for your own needs


TARGET_FORMAT="%Y-%m-%d %H:%M:%S %z"

def readLogs():
    logFile = open(dataPath)
    logs = json.load(logFile)
    logFile.close()
    return logs

def writeLogs(logs):
    logFile = open(dataPath, "w")
    json.dump(logs, logFile, indent=2)
    logFile.close()

def reformat_utc(date_string):
    date_pdt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    print(f"{date_pdt} PDT")

    utc_str = date_pdt.strftime(TARGET_FORMAT + "+0000 UTC")
    print(utc_str)
    return utc_str


dataPath = input("path to file for preprocessing: ")
logs = readLogs()

current_time = datetime.now()
print(f"It is currently {current_time}\nAll times will be converted to this timezone\n")

# reformat UTC
# %Y-%m-%dT%H:%M:%SZ  ->  %Y-%m-%d %H:%M:%S %z %Z
for i in range(len(logs)):
    date_str = logs[i]["ts"]
    logs[i]["ts"] = reformat_utc(date_str)

writeLogs(logs)
