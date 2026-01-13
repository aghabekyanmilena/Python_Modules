def ft_plant_age():
    while True:
        age = int(input("Enter plant age in days: "))

        if age < 0:
            print("Positive value required")
            continue
        break
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")

ft_plant_age()