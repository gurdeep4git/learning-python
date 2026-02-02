seat = input("Enter seat type (Sleeper/AC/General): ").lower()

match seat:
    case 'sleeper':
        print(f"Sleeper has AC and space to sleep")
    case 'ac':
        print(f"AC is provided and seats")
    case 'general':
        print(f"only seats are available")
    case _:
        print(f"Unknown seat")        