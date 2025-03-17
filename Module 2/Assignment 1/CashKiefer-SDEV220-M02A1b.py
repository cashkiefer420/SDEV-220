# Assign True or False to small and green
small = True
green = True

# Check conditions and print the matching item
if small and green:
    print("pea")  # Small and green
elif small and not green:
    print("cherry")  # Small but not green
elif not small and green:
    print("watermelon")  # Not small but green
else:
    print("pumpkin")  # Not small and not green
