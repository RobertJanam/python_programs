"""My first file handling program. Wrote comments everywhere thinking i would forget."""

# function to call main program
def main():
    file_name = 'Playlist.txt'
    # write the file
    name = '---Playlist---\n'
    total = 1# attaches numbers to songs in order
    count = 0# keep track of total number of songs in the file and terminal
    total_songs = 0# adds up the count

    print('\n----Your Playlist----\n')
    # set an empty dictionary
    my_playlist = {}
    # open a while loop to iterate over the inputs
    while True:
        # allow user to input name of the song or exit out of the loop
        title_of_song = input("Enter name of the song\nor type (stop) to exit: ")
        if title_of_song == 'stop'.lower():
            break
        # allow user to input name of the artist
        elif title_of_song != 'stop'.lower():
            name_of_artist = input("Enter name of the artist: ").title().strip()
            # key : value
            my_playlist[title_of_song] = name_of_artist
            # print the dictionary
            print(my_playlist)
            print("Saved successfully ✔\n")
        else:
            print("Invalid input")

    # print success to user
    print('\nStatus: Finished')
    print("Update: Successful")
    print("Run-time: Clear")
    # call write_liked_songs function
    write_liked_songs(my_playlist, file_name, total, count, name)

# function to call dictionary playlist and write it to a file
def write_liked_songs(playlist_song, file_name, total, count, name):
    # create and open file to save playlist
    with open(file_name, 'a') as file:
        file.write(name)
        # iterate to keep track of total songs
        while True:
            # take saved input from my_playlist dictionary and add it to file
            for song, name in playlist_song.items():
                file.write(f"{total}. {song} - {name}\n")
                total += 1 # adds 1 after every iteration
                count += 1 # adds 1 after every iteration
                total_songs = count # sums up the total_count of songs recorded
            break
        file.write(f"Total songs: {total_songs}")
        print(f"Total songs: {total_songs}")
        print("\nPlaylist Successfully saved 🖍")

main()# call main function to start program