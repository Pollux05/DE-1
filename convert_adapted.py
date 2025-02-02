import sys
import os
import glob
import hdf5_getters
import re


class Song:
    songCount = 0

    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        self.albumName = None
        self.albumID = None
        self.artistFamiliarity = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        self.energy = None
        self.hotness = None
        self.keySignature = None
        self.keySignatureConfidence = None
        self.mode = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None

    def displaySongCount(self):
        print
        "Total Song Count %i" % Song.songCount

    def displaySong(self):
        print
        "ID: %s" % self.id


def main():
    csvAttributeList = []
    outputFile1 = open('MSD_Sub_as_CSV.csv', 'w')
    csvRowString = ""
    
    #################################################
    # change the order of the csv file here
    # Default is to list all available attributes (in alphabetical order)
    csvRowString = ("SongID,AlbumID,AlbumName,ArtistFamiliarity,ArtistID,ArtistLatitude,ArtistLocation," +
                    "ArtistLongitude,ArtistName,Danceability,Duration,Energy,Hotness,KeySignature," +
                    "KeySignatureConfidence,Mode,Tempo,TimeSignature,TimeSignatureConfidence," +
                    "Title,Year")
    #################################################

    csvAttributeList = re.split('\W+', csvRowString)
    for i, v in enumerate(csvAttributeList):
        csvAttributeList[i] = csvAttributeList[i].lower()
    outputFile1.write("SongNumber,");
    outputFile1.write(csvRowString + "\n");
    csvRowString = ""

        #################################################

    # Set the basedir here, the root directory from which the search
    # for files stored in a (hierarchical data structure) will originate
    basedir = r"C:\Users\justu\OneDrive\Documents\Uppsala_University\Period_3\Data_Engineering_1\MSD\MillionSongSubset"  # "." As the default means the current directory
    ext = ".H5"  # Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    # FOR LOOP
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*' + ext))
        for f in files:
            print(f)

            songH5File = hdf5_getters.open_h5_file_read(f)
            byte_songH5File = hdf5_getters.get_song_id(songH5File).decode("utf-8", "ignore")
            song = Song(byte_songH5File)
            # song = Song(str(hdf5_getters.get_song_id(songH5File)))

            song.artistID = str(hdf5_getters.get_artist_id(songH5File).decode('ASCII', "ignore"))
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.albumName = str(hdf5_getters.get_release(songH5File).decode('ASCII', "ignore"))
            song.artistFamiliarity = str(hdf5_getters.get_artist_familiarity(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File).decode('ASCII', "ignore"))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistName = str(hdf5_getters.get_artist_name(songH5File).decode('ASCII', "ignore"))
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            song.energy = str(hdf5_getters.get_energy(songH5File))
            song.hotness = str(hdf5_getters.get_song_hotttnesss(songH5File))
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File).decode('ASCII', "ignore"))
            song.year = str(hdf5_getters.get_year(songH5File))

            # print song count
            csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:


                if attribute == 'AlbumID'.lower():
                    csvRowString += song.albumID
                elif attribute == 'AlbumName'.lower():
                    albumName = song.albumName
                    albumName = albumName.replace(',', "")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'ArtistFamiliarity'.lower():
                    csvRowString += "\"" + song.artistFamiliarity + "\""
                elif attribute == 'ArtistID'.lower():
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLocation'.lower():
                    location = song.artistLocation
                    location = location.replace(',', '')
                    csvRowString += "\"" + location + "\""
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude
                elif attribute == 'ArtistName'.lower():
                    csvRowString += "\"" + song.artistName + "\""
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'Energy'.lower():
                    csvRowString += song.energy
                elif attribute == 'Hotness'.lower():
                    csvRowString += song.hotness    
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'SongID'.lower():
                    csvRowString += song.id
                elif attribute == 'Mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'Tempo'.lower():
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                else:
                    csvRowString += " Error\n"

                csvRowString += ","

            # Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex - 1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()


main()

