import random


def songPlaylist(playlist):
    counter = 0
    idsong_list = []
    assert isinstance(playlist, dict)
    while counter < len(playlist):

        song = random.choice(list(playlist.keys()))

        if song not in idsong_list:
            idsong_list.append(song)
            counter += 1

    assert idsong_list != []

    song_list = ' '.join(idsong_list)

    return song_list






