# spotify-data-processor
 generate stats and more from Spotify data logs

## set-up
set the data path in [vars.py](./vars.py) to the path to the exported data

## usage
`python3 main.py`

## filter schema
filter by one or more artists and/or tracks
`"artists":"ARTIST"`
`"artists":"ARTIST", "tracks":"TRACK"`
`"artists":["ARTIST1", "ARTIST2], "tracks":["TRACK1", "TRACK2"]`

example
`"artists":"Lorde", "tracks":["The Louvre", "A World Alone"]`
