# minus-youtube
Create and manage YouTube playlists without the hassle of signing into your Google account.

*Note: Currently works on Windows only*

## How to use
To create a playlist, or add a video to a playlist:
```python add.py [NAME OF PLAYLIST] [TITLE OF VIDEO] [VIDEO ID]```


To list the contents of a playlist, or generate its URL:
```python get-playlist.py [NAME OF PLAYLIST]```


To remove a video from a playlist:
```python remove.py [NAME OF PLAYLIST] [VIDEO ID]```


The playlists generated are stored as a python shelve object in ```C:\Playlists```
