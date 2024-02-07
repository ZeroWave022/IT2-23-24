import json
import matplotlib.pyplot as plt

with open("./stortinget.json", encoding="utf-8") as f:
    data = json.load(f)

for politician in data["representanter_liste"]:
    print(f"{politician['etternavn']}, {politician['parti']['navn']}")

parties: dict[str, int] = {}

for politician in data["representanter_liste"]:
    party = politician["parti"]["navn"]
    if party in parties:
        parties[party] += 1
    else:
        parties[party] = 0

sorted_parties = sorted(parties.keys(), key=lambda p: parties[p], reverse=True)

print(f"Det største partiet er {sorted_parties[0]} med {parties[sorted_parties[0]]} representanter")

plt.bar(sorted_parties, [parties[party] for party in sorted_parties])
plt.xticks(rotation=90)
plt.show()

total = 0
for party in parties.values():
    total += party
average = total / len(parties)

print(f"I gjennomsnitt har hvert parti {average} representanter")
