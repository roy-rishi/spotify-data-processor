# spotify-data-processor
 generate stats and more from Spotify data logs

## set-up
set the data path in [vars.py](./vars.py) to the path to the exported data

## usage
first, preprocess all files with
`python3 preprocessor.py`

then, run the processor
`python3 main.py`

## filter schema
execute one or more functions filtered by one or more artists and/or tracks
`"funcs":"FUNCTION", "artists":"ARTIST"` or
`"funcs":"FUNCTION", "artists":"ARTIST", "tracks":"TRACK"` or
`"funcs":"FUNCTION", "artists":["ARTIST1", "ARTIST2], "tracks":["TRACK1", "TRACK2"]` etc.

example
`"funcs":"sum", "artists":"Lorde", "tracks":["The Louvre", "A World Alone"]`
