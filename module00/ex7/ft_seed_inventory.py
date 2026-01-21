def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        seed_type  = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seed: covers {quantity} square meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("tomato", 12, "grams")
ft_seed_inventory("carrot", 12, "packets")
ft_seed_inventory("apple", 12, "area")