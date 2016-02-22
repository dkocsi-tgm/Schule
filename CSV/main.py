__author__ = 'Daniel'

import csv
"""Dialekt festlegen, bzw angeben woher das File stammt, in unserem fall excel"""
csv.list_dialects()
var = ['excel-tab', 'excel']

""" Dialect Herausfinden mittels Sniffer """
POSSIBLE_DELIMITERS = [',', '\t', ';', ' ', ':', '|']

def sniff_dialect(sample):
    """
    A functional version of ``csv.Sniffer().sniff``, that extends the
    list of possible delimiters to include some seen in the wild.
    """
    try:
        dialect = csv.Sniffer().sniff(sample, POSSIBLE_DELIMITERS)
    except:
        dialect = None

    return dialect


"""Auslesen aus dem csv files, delimeter gibt an in welcher form das csv file getrennt ist """
reader = csv.reader(open("dbCSV.csv"), delimiter=";")

"""Ausgabe des csv files, umformatiert, keine eckige Klammer am beginn, keine einzelnen hochkomma und ein strichpunkt am ende"""
for row in reader:
    text = ''
    for i in range(0,20):
        if i < 19:
            text += (row[i]+',')
        else:
            text +=(row[i]+';')
    print(text)

"""Writeing to a file """
file = open("csvTest.csv","w")
file.write("\nHello World")

""" appending to a file"""
file = open("csvTest.csv","a")
file.write("\nJonny")

""" reading file """
file = open("csvTest.csv","r")
testArray = file.readlines()
for line in testArray:
    print(line)
file.close()

def saveDataCSV(self,dialect,outfilename):
        '''
        This function writes the already read csv data into a choosen file with a certain dialect.

        :param dialect: One of the dialects provided by python or saved in python.
        :param outfilename: the path and name of the wanted output file
        '''
        if dialect in csv.list_dialects():
            ofile = open(outfilename,"w")
            writer = csv.writer(ofile, dialect=dialect)
            writer.writerow(self.header)

            for row in self.storealt:
                writer.writerow(row)

            ofile.close()

        else:
            raise TypeError("Dialect is unknown. Read csv.list_dialects for all dialects.")