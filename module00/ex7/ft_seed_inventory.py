def ft_seed_inventory(name, quantity, unit):
    if unit == "packets":
        name = name.capitalize()
        print(f"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        name = name.capitalize()
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        name = name.capitalize()
        print(f"{name} seed: covers {quantity} square meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("tomato", 12, "grams")
ft_seed_inventory("carrot", 12, "packets")
ft_seed_inventory("apple", 12, "area")