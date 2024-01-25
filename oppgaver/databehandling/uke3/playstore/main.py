import json
import re

with open("./googleplaystore.json", encoding="utf-8") as f:
    apps = json.load(f)

categories = {}

for app in apps:
    category = app["Category"]
    if category not in categories:
        categories[category] = 1
    else:
        categories[category] += 1

sorted_categories = sorted(categories.keys(), key=categories.get, reverse=True)

top_categories = []

for i in range(3):
    top_categories.append({
        "name": sorted_categories[i],
        "apps": categories[sorted_categories[i]],
        "avg_rating": None,
        "avg_install": None
    })

for category in top_categories:
    ratings = []
    installs = []
    for app in apps:
        if app["Category"] != category["name"]:
            continue

        if app["Rating"].lower() != "nan":
            ratings.append(float(app["Rating"]))

        install = re.sub(r"\+|,", "", app["Installs"])
        installs.append(int(install))

    category["avg_rating"] = sum(ratings) / len(ratings)
    category["avg_install"] = sum(installs) / len(installs)

for num, category in enumerate(top_categories, 1):
    print(f"""
Kategori {num}: {category['name']}
Apper: {category['apps']}
Gjennomsnittsrating: {round(category['avg_rating'], 2)}
Gjennomsnittsinstallasjoner: {round(category['avg_install'])}""")

for category in sorted_categories[:3]:
    apps_in_category = [a for a in apps if a["Category"] == category]
    apps_in_category = sorted(
        apps_in_category,
        key=lambda a: re.sub(r"\+|,", "", a["Installs"]),
        reverse=True
    )

    print(f"\nTop 3 mest populære apper i kategorien {category}:")
    for i in range(1, 4):
        print(f"{i}. {apps_in_category[i-1]['App']}")
