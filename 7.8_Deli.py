def orders():
    sandwich_orders = ["tuna sandwich", "cheese sandwich", "chicken sandwich", "big sandwich", "jambon sandwich"]
    finished_sandwiches = []
    while len(sandwich_orders) != 0 :
        current_sand = sandwich_orders.pop()
        finished_sandwiches.append(current_sand)
        print(f"I made your {current_sand}")
    print("-" * 15)
    print("Sandwichs done : ")
    for _ in finished_sandwiches :
        print(f"- {_.title()}")
    
def main():
    orders()

if __name__ == '__main__':
    main()

