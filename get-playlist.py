import shelve, sys, os

# Accept exactly 2 arguments only
if len(sys.argv) != 2:
	print("Usage: python get-playlist.py [playlist name]")
	sys.exit()

# Get the name of the playlist requested
playlist = sys.argv[1]

# Change to correct folder
if not os.path.exists("C:\\Playlists"):
	print("No playlists exist. Create one using add.py")
	sys.exit()
	
else:
	os.chdir("C:\\Playlists")
	
# Check if the playlist exists
if not os.path.exists("C:\\Playlists\\{}.dat".format(playlist)):
	print("Playlist not found.")
	sys.exit()
	
with shelve.open(playlist) as file:
	link = "http://www.youtube.com/watch_videos?video_ids="
	
	for pair in file['links']:
		link = link + pair[1] + ","
		
	print(link)