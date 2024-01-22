import json

with open("./weekly-top-songs-global.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

### Find which songs are the longest on the top 250 spotify list ###

sorted_by_weeks = sorted(songs, key=lambda song: song["uker_paa_listen"], reverse=True)
longest_on_list = [sorted_by_weeks[0]]

# Check if multiple songs have the same score at the top
for song in sorted_by_weeks[1:]:
    if song["uker_paa_listen"] == longest_on_list[0]["uker_paa_listen"]:
        longest_on_list.append(song)
    else:
        break

song_names = [f"{song['artist']} - {song['navn']}" for song in longest_on_list]

if len(longest_on_list) > 1:
    print("The songs which have been the longest time on the top 250 spotify list")
    print(f"Duration: {longest_on_list[0]['uker_paa_listen']} weeks")
    print("\n".join(song_names))
else:
    print("The song which has been the longest time on the top 250 spotify list")
    print(f"Duration: {longest_on_list[0]['uker_paa_listen']} weeks")
    print(f"Song name: {song_names[0]}")

### Find total amount of Taylor Swift streams of songs which are on the list ###

total_streams = 0
for song in songs:
    if song["artist"] == "Taylor Swift":
        total_streams += song["antall_streams"]

print(f"The total amount of Taylor Swift streams: {total_streams}")

### The song which moved up the most amount of places ###

sorted_by_move = sorted(
    songs,
    key=lambda song: song["forrige_plassering"] - song["plassering"],
    reverse=True
)
top_moves = [sorted_by_move[0]]
top_move = top_moves[0]["forrige_plassering"] - top_moves[0]["plassering"]

# Check if multiple songs have moved the same amount of places
for song in sorted_by_move[1:]:
    move = song["forrige_plassering"] - song["plassering"]
    if move == top_move:
        top_moves.append(song)
    else:
        break

top_move_song_names = [f"{song['artist']} - {song['navn']}" for song in top_moves]

if len(top_moves) > 1:
    print("The songs which have moved up the most places are:")
    print("\n".join(top_move_song_names))
else:
    print("The song which has moved up the most places is:")
    print(top_move_song_names[0])

print(f"By moving up {top_move} places")
