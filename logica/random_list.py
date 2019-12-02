import random


def songPlaylist(playlist):
    counter = 0
    song_list = []
    assert isinstance(playlist, dict)
    while counter < len(playlist):

        song = random.choice(list(playlist.keys()))

        if song not in song_list:
            song_list.append(song)
            counter += 1

    assert song_list != []

    return song_list







