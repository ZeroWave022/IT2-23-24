import csv
import matplotlib.pyplot as plt

with open("global-youtube-statistics.csv") as f:
    reader = csv.DictReader(f)
    stats = list(reader)

countries = {}

for channel in stats:
    if channel["Country"] not in countries:
        countries[channel["Country"]] = 1
    else:
        countries[channel["Country"]] += 1

# Delete nan from countries
del countries["nan"]

sorted_countries = sorted(countries, key=lambda country: countries[country], reverse=True)

channel_counts = []

for country in sorted_countries[:10]:
    channel_counts.append(countries[country])

subscribers = []
views = []

# Find average subscriber count and video views for these countries
for country in sorted_countries[:10]:
    subs = 0
    view_count = 0
    for channel in stats:
        if channel["Country"] == country:
            subs += int(channel["subscribers"])
            view_count += int(channel["video views"])
    subscribers.append(subs / countries[country])
    views.append(view_count / countries[country])

plt.bar(sorted_countries[:10], channel_counts)
plt.title("Antall kanaler per land")
plt.figure()

plt.bar(sorted_countries[:10], subscribers)
plt.title("Gjennomsnittelig antall subs")
plt.figure()

plt.bar(sorted_countries[:10], views)
plt.title("Gjennomsnittelig antall videovisn.")

plt.show()
