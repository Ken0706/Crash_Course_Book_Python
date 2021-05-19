def Cities():
    cities = {
        "london" : {"country ": "england", "population" : "9,426,000", "fact" : "Police never caught Jack the Ripper"},
        "tokyo" : {"country ": "japan", "population" : "37,393,000", "fact" : "Tokyo is the largest metropolitan area in the world, hosting over 36 million people spread over three prefectures"},
        "paris" : {"country ": "france", "population" : "2,161,000", "fact" : "City of Light"}
    }
    for city, info in cities.items():
        print("City : " + city.title())
        for key, detail in info.items():
            print(f"\t{key.title()} : {detail.title()}")

def main():
    Cities()

if __name__ == '__main__':
    main()