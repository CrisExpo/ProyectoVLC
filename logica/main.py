from xml_access import xmlParse
from random_list import songPlaylist
from vlc_access import vlcAccess


def main():
    library = '/home/cristina/Escritorio/ProyectoVLC/libreriaXml/Library.xml'
    vlcpath = '/snap/bin/vlc'
    xmlParse(library)
    playlist = xmlParse(library)
    randomplaylist = songPlaylist(playlist)
    vlcAccess(randomplaylist, vlcpath)


main()
