def survey():
    survey = {}
    while True :
        name = input("What's your name ? : ")
        place = input("If you could visit one place in the world, where would you go ? : ")
        another = input("Would you like to let another person respond ? (yes/ no) : ")
        survey[name] = place
        if another == 'no' : break
    
    #print survey 
    print("\n--- Poll Results ---")
    for name_, place_ in survey.items():
        print(f"{name_.title()} would like to go {place_.title()}!")

def main():
    survey()

if __name__ == '__main__':
    main()
        