def storage():
    pet = {
        "Gold"  : {"kind" : "dog", "host_name" : "ken"} ,
        "ChichChoe"  : {"kind" : "bird", "host_name" : "lan"},
        "Meow" : { "kind" : "cat", "host_name" : "phuong" }
    }
   
   
    pets = [pet]
    for pet_name, pet_info in pet.items():
        print(pet_name)
        print(f'\tKind : {pet_info["kind"].title()}')
        print(f'\tHost name : {pet_info["host_name"].title()}')
       

def main():
    storage()

if __name__ == '__main__': 
    main()