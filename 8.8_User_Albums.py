def make_album(artist_name, album_title, number_track = ''):
    if number_track :
         user = {"artist" : artist_name, "album" : album_title, "track" : number_track}
    else : user = {"artist" : artist_name, "album" : album_title}
    return user

def main():
    while True :
        name = input("Enter name of artist (Enter 'q' to quit): ").title()
        if name == 'q' : break
        album = input("Enter name of album (Enter 'q' to quit) : ").title()
        if album == 'q' : break
        print(make_album(name, album))

if __name__ == '__main__':
    main()

