import json

dataPath = input("path to file for preprocessing: ")

def readLogs():
    logFile = open(dataPath)
    logs = json.load(logFile)
    logFile.close()
    return logs

def writeLogs(logs):
    logFile = open(dataPath, "w")
    json.dump(logs, logFile, indent=2)
    logFile.close()


logs = readLogs()

for i in range(len(logs)):
    name = logs[i]["master_metadata_album_artist_name"]
    if type(name) is str:
        logs[i]["master_metadata_album_artist_name"] = [name]

writeLogs(logs)
