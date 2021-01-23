import shelve, sys, os

# Allow exactly 4 command-line arguments only
if len(sys.argv != 4):
	print("Usage: python add.py [playlist name] [title] [id]")
	sys.exit()
	
if not os.path.exists("C:\\Playlists"):
	os.mkdir("C:\\Playlists")