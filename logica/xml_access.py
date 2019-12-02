import xml.etree.ElementTree as ET

library = '/home/cristina/Escritorio/ProyectoVLC/libreriaXml/Library.xml'

tree = ET.parse(library)
root = tree.getroot()


def xmlParse(root, library):

    try:
        f = open(library)
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

    print(playlist)


xmlParse(root, library)
