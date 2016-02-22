__author__ = "Daniel Kocsi"

"""
 Die Klasse csvReadWriteAppend ermöglicht uns, wie der Name schon sagt,
 das Lesen, Schreiben und Anfügen von Text in CSV Files.
"""
import csv

class csvReadWriteAppend(object):

    def __init__(self, file):
        self.file = file
        self.liste = []

    """
    Mit der Methode read können csv files von verschiedenen Dialekten gelesen werden.
    """
    def read(self,filename):
        with open(filename, 'r') as f: #Mittels 'rb' wird bestimmt das das File nur gelesen wird.
            try:
                dialect = csv.Sniffer().sniff(f.read(), [',', '\t', ';', ' ', ':', '|']) #Festlegen der Delimiter(trennobjekte) die in
            except:                                                                      #einem CSV file vorkommen können
                dialect = None

            f.seek(0) #durch iterieren durch das file um auf dialekte zu prüfen
            csvreader = csv.reader(f, dialect)

            for n in csvreader:
                self.liste.append(n)

        return self.liste

    """
    Mit der Methode write können csv files von verschiedenen Dialekten geschrieben werden.
    """
    def write(self,filename):
        with open(filename, 'w') as f: #'w' als parameter für die option "schreiben"
            writer = csv.writer(f)
            writer.writerows(self.liste)

#Aufrufen der Klasse zum testen von einlesen und schreiben von files
csvfile = csvReadWriteAppend("dbCSV.csv")
csvfile.read("dbCSV.csv")
csvfile.write("test.csv")
csvfile.read("test1.csv")
csvfile.write("test.csv")