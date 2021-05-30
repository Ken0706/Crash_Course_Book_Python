def cars(manufact, model_name, **details):
    cars = {}
    cars['manufactorer'] = manufact
    cars['model'] = model_name
    for k, v in cars.items():
        cars[k] = v
    return cars


def main():
    car1 = cars('toyota', 'outback', color='blue', date='29/05/2002')
    car2 = cars('subaru', 'inback', color='red', seat=4)
    print(car1, car2, sep='\n')


if __name__ == '__main__':
    main()
