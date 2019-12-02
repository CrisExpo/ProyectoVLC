import xml.etree.ElementTree as ET


def xmlParse(library):

    tree = ET.parse(library)
    root = tree.getroot()
    
    try:
        p = open(library)
    except FileNotFoundError:
         print('File not found')
    else:
        pass

    playlist = {}

    for track in root.iter('track'):
        songName = track.findtext('path')
        idSong = track.findtext('id')

        playlist[idSong] = songName

    assert playlist != {}

    return(playlist)
