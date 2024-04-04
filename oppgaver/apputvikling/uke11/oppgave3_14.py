def generate_mail(name: str) -> str:
    names = name.lower().split(" ")
    return f"{names[0]}{names[-1][0]}@afk.no"


while True:
    user = input("Skriv inn ditt fulle navn: ")
    if len(user.split(" ")) < 2:
        print("Du må skrive inn minst et fornavn og etternavn")
    else:
        break

print(generate_mail(user))
