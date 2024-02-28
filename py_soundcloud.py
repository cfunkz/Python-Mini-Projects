from sclib import SoundcloudAPI, Track, Playlist # pip install soundcloud-lib

api = SoundcloudAPI()

def get_playlist():
    question = input("Enter playlist url or any number to exit: ")
    try:
        playlist = api.resolve(question)
        assert type(playlist) is Playlist
        for track in playlist.tracks:
            filename = f'./{track.artist} - {track.title}.mp3'
            try:
                with open(filename, 'wb+') as file:
                    track.write_mp3_to(file)
            except Exception as e:
                print("Track error:", e)
                return 0
    except Exception as e:
        print("Link error: ", e)
        print("Exiting...")
        return 0

def get_track():
    question = input("Enter track url or any number to exit: ")
    try:
        track = api.resolve(question)
        assert type(track) is Track
        filename = f'./{track.artist} - {track.title}.mp3'
        with open(filename, 'wb+') as file:
            track.write_mp3_to(file)
    except Exception as e:
        print("Link error: ", e)
        print("Exiting...")
        return 0


question1 = input("1 for playlist link || 2 for track link || or any other number to exit: ")

while True:
    if int(question1) == 1:
        check = get_playlist()
        if check == 0: #If 0 returned instead of link it closes
            break
        else:   # Else run
            continue
    elif int(question1) == 2:
        check = get_track()
        if check == 0: #If 0 returned instead of link it closes
            break
        else:   # Else run
            continue
    else:   # If something else than 1 or 2 is entered its closed.
        print("Exiting..")
        break
