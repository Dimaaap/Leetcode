def distance_traveled(main_tank: int, additional_tank: int) -> int:
    """
    A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main
    tank in liters and additionalTank representing the fuel present in the additional tank in liters.

    The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the
    additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to
    the main tank.

    Return the maximum distance which can be traveled.

    Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
    """

    distance = 0
    counter = 0

    while main_tank:
        distance += 10
        main_tank -= 1
        counter += 1

        if counter % 5 == 0 and additional_tank:
            main_tank += 1
            additional_tank -= 1
    return distance


print(distance_traveled(5, 10))
print(distance_traveled(1, 2))