import shelve, sys, os

# Accept exactly 3 arguments only
if not len(sys.argv) == 3:
	print("Usage: python remove.py [playlist name] [video id]")
	sys.exit()
	
# Get the playlist name and the video id from the arguments
playlist, id = sys.argv[1:3]
