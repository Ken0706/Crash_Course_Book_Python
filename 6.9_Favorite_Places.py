def place ():
    favorite_place = {
        "ken" : [{"viet nam" : "ha noi"}, {"laos" : "vientiane"}],
        "nam" : [{"american" : "washington"}, {"italy" : "roma"}],
        "hieu" : [{"czech" : "pra-ha"}, {"singapore" : "republic of singapore"}]
    }
    for name, info in favorite_place.items():
        print(name.title())
        for place in info:
            for country, city in place.items():
                print(f"\t{country.title()} : {city.title()}")
def main():
    place()

if __name__ == '__main__':
    main()
