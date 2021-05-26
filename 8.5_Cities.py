def describe_city(city, country ='Viet Nam'):
    print(city + " is in " + country)

def main():
    describe_city("Thanh pho Ba Ria - Vung Tau")
    describe_city("TPHCM")
    describe_city("Reykjavik", "Iceland")

if __name__ == '__main__':
    main()