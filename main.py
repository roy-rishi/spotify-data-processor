import json

dataPath = "data/Streaming_History_Audio_2022-2023_0.json"

def getArtistName(track):
    return track["master_metadata_album_artist_name"]

def getTrackName(track):
    return track["master_metadata_track_name"]

# return total minutes listened as filtered by lists of artists and tracks
def filteredListeningTime(data, artistNames, trackNames):
    totalMin = 0
    for track in data:
        if ((artistNames == "*" or str(getArtistName(track)) in artistNames)
        and (trackNames == "*" or str(getTrackName(track)) in trackNames)):
            totalMin += (track["ms_played"] / 1000 / 60)
    return totalMin


filters = input("Enter filters: ")
filters = f"{{{filters}}}"
filters = json.loads(filters)

artistNames = "*"
if "artists" in filters:
    artistNames = filters["artists"]
    print(f"searching artists {artistNames}")
trackNames = "*"
if "tracks" in filters:
    trackNames = filters["tracks"]
    print(f"searching tracks {trackNames}")


data = None
with open(dataPath) as dataFile:
    data = json.load(dataFile)

totalMin = filteredListeningTime(data, artistNames, trackNames)

print(f"\nYou listened for\n{int(round(totalMin, 0))} minutes")
print()
