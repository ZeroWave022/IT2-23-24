while True:
    # Try to get user's age,
    # else print an error message and try again
    try:
        alder = int(input("Hvor gammel er du? "))
        break
    except:
        print("Ugyldig input. Alder må være et tall.")

# Calculate birth year and display it
år = 2024
fødselsår = år - alder
print(f"Du er født i {fødselsår}")
