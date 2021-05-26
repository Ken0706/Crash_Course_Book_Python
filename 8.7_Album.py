def make_album(artist_name, album_title, number_track = ''):
    if number_track :
         user = {"artist" : artist_name, "album" : album_title, "track" : number_track}
    else : user = {"artist" : artist_name, "album" : album_title}
    return user

def main():
    print(make_album("Noo Phuoc Thinh", "Ba cham"))
    print(make_album("Hamlet Truong", "Rong Go"))
    print(make_album("VPOP", "2020", 2))

if __name__ == '__main__':
    main()

