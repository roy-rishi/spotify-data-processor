import json
import vars

dataPath = vars.DATA_PATH

def getArtistName(track):
    artists = track["master_metadata_album_artist_name"]
    if artists == None:
        artists = "no artist recorded"
    return artists

def getTrackName(track):
    return track["master_metadata_track_name"]

def matchArtists(track, artistNames):
    if type(artistNames) is list:
        for name in artistNames:
            if name in getArtistName(track):
                return True
    else:
        if artistNames in getArtistName(track):
            return True
    return False

# return total minutes listened as filtered by lists of artists and tracks
def filteredListeningTime(data, artistNames, trackNames):
    totalMin = 0
    for track in data:
        if ((artistNames == "*" or matchArtists(track, artistNames))
        and (trackNames == "*" or str(getTrackName(track)) in trackNames)):
            totalMin += (track["ms_played"] / 1000 / 60)
    return totalMin

# return total minutes listened as filtered by lists of artists and tracks
def filteredAnniversaries(data, artistNames, trackNames):
    anniversaries = {}
    totalMin = 0
    alreadyCovered = []
    for track in data:
        trackName = track["master_metadata_track_name"]

        trackArtists = track["master_metadata_album_artist_name"]
        # print(trackArtists, track["ts"])
        trackArtistsStr = ""

        if trackArtists == None:
            trackArtists = "unknown"

        for i in range(len(trackArtists)):
            trackArtistsStr = trackArtistsStr + trackArtists[i] + ", " if i < len(trackArtists) - 1 else trackArtistsStr + trackArtists[i]

        if ((artistNames == "*" or matchArtists(track, artistNames))
        and (trackNames == "*" or str(getTrackName(track)) in trackNames)
        and (trackName not in alreadyCovered)):
            alreadyCovered.append(trackName)
            timestamp = track["ts"]
            print(f"{timestamp.replace('-', '/')}: {trackName}, {trackArtistsStr}")


print(f"\nreading from {dataPath}")
data = None
with open(dataPath) as dataFile:
    data = json.load(dataFile)

filters = input("\nEnter filters: ")
filters = f"{{{filters}}}"
filters = json.loads(filters)

functions = artistNames = trackNames = "*"
if "funcs" in filters:
    functions = filters["funcs"]
    print(f"executing functions {functions}")
if "artists" in filters:
    artistNames = filters["artists"]
    print(f"searching artists {artistNames}")
if "tracks" in filters:
    trackNames = filters["tracks"]
    print(f"searching tracks {trackNames}")
print()


if "sum" in functions:
    totalMin = filteredListeningTime(data, artistNames, trackNames)
    print(f"You listened for\n{int(round(totalMin, 0))} minutes\n")

if "anniversary" in functions:
    filteredAnniversaries(data, artistNames, trackNames)
    print()

print()
