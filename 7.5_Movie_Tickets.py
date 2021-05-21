def cost():
    s = 0
    check = 0
    while True :
        age = int(input("Enter age :  "))
        if age >= 3 and age <= 12 : 
            s += 10
        elif age > 12 : 
            s += 15
        cont = input("Continue enter (y/n) : ")
        if cont == 'n' :
            print("The price of the movie ticket you have to pay is : " + str(s))
            break
            
        


def main():
    cost()

if __name__ == '__main__': 
    main()