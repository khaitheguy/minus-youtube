import shelve, sys, os

# Allow exactly 4 command-line arguments only
if len(sys.argv) != 4:
	print("Usage: python add.py [playlist name] [title] [id]")
	sys.exit()

# Assign variables to the arguments
playlist, title, id = sys.argv[1:5]

# Create a folder for playlists on the C: drive if it does not exist
if not os.path.exists("C:\\Playlists"):
	os.mkdir("C:\\Playlists")

# Change to the correct folder
os.chdir("C:\\Playlists")

# Save the video title and id to the playlist file
with shelve.open(playlist) as file:
	# Create a list in the key if it has not been created yet
	file.setdefault('links', [])
	
	# "Copy" the list to a variable and "copy" it back to the key
	links = file['links']
	links.append((title, id))
	file['links'] = links
	
	# Print out the titles and ids of videos already in the file
	for pair in file['links']:
		print(pair[0], pair[1])