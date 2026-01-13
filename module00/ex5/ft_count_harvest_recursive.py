def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def foo(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        foo(day + 1)
    foo(1)

ft_count_harvest_recursive()