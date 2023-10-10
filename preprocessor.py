import json
from datetime import datetime, timezone

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

# convert artist name strings to single element arrays of one string
# "Lorde" -> ["Lorde"]
for i in range(len(logs)):
    name = logs[i]["master_metadata_album_artist_name"]
    if type(name) is str:
        logs[i]["master_metadata_album_artist_name"] = [name]

# reformat UTC
# %Y-%m-%dT%H:%M:%SZ  ->  %Y-%m-%d %H:%M:%S %z %Z
for i in range(len(logs)):
    date_str = logs[i]["ts"]
    logs[i]["ts"] = reformat_utc(date_str)

writeLogs(logs)
