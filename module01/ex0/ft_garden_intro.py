#!/usr/bin/env python3
#(this script makes file an executable file)

def ft_garden_intro(name, height, age):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)