size = input('Enter preferred size (small/medium/large): ').lower()
if size == 'small':
    print(f"Your bill is $10")
elif size == 'medium':
    print(f"Your bill is $15")
elif size == 'large':
    print(f"Your bill is $20")
else:
    print(f"Unknown size")    