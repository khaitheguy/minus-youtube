import shelve, sys, os

# Accept exactly 2 arguments only
if len(sys.argv) != 2:
	print("Usage: get-playlist.py [playlist name]")
	sys.exit()

# Get the name of the playlist requested
playlist = sys.argv[1]

# Check if the playlist exists
if not os.path.exists("C:\\Playlists\\{}.dat".format(playlist)):
	print("Playlist not found.")
	sys.exit()