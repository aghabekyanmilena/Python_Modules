def ft_water_reminder():
    while True:
        days = int(input("Days since last watering: "))

        if days < 0:
            print("Positive value required")
            continue
        break
    if days > 2:
        print("Water the plants!")
    else:
        print("Plant are fine")

ft_water_reminder()