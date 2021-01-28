import shelve, sys, os

# Accept exactly 3 arguments only
if not len(sys.argv) == 3:
	print("Usage: python remove.py [playlist name] [video id]")
	sys.exit()
	
# Get the playlist name and the video id from the arguments
playlist, video_id = sys.argv[1:3]

# Change to "Playlists" folder
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
	found_video = False
	
	for title, id in file['links']:
		if id == video_id:
			found_video = True
			
			# Prompt user for confirmation until valid response given
			while True:
				choice = input("Are you sure you want to remove:\n" + title + "\n[y/n]? ")
				
				if choice.lower() == 'y' or 'yes' in choice.lower():
					# Make a copy of the list then give it back
					links = file['links']
					
					# Delete the video entry in the file
					links.remove((title, id))
					file['links'] = links
					
					print(title, "has been removed")
					print("There are now", len(file['links']), "videos in", playlist)
					break
				
				elif choice.lower() == 'n' or 'no' in choice.lower():
					print(title, "will remain in", playlist)
					break
					
			break
				
	if not found_video:
		print("Cannot find video with the given ID:", video_id)