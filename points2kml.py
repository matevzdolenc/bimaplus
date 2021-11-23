#! /usr/bin/env python

import xml.etree.cElementTree as et
import sys

print("Input file:", sys.argv[1])

dat = open(sys.argv[1], "r")
n = int(dat.readline())
print("Number of geo locations:", n)

lats = []
longs = []
names = []
cities = []
countries = []

print("Reading data: ", end='')
for i in range(n):
    line = dat.readline()
    words = line.split(",")
    lats.append(words[0])
    longs.append(words[1])
    names.append(words[2])
    cities.append(words[3])
    countries.append(words[4])
    print(".", end='')

print()

# Output to KML file format
print()
print("Output file:", sys.argv[1]+".kml")
print("Writing data: ", end='')
kml = et.Element("kml")
kml.set("xmlns", "http://www.opengis.net/kml/2.2")
kml.set("xmlns:gx", "http://www.google.com/kml/ext/2.2")
kml.set("xmlns:kml", "http://www.opengis.net/kml/2.2")
kml.set("xmlns:atom", "http://www.w3.org/2005/Atom")

document = et.SubElement(kml, "Document")

document_name = et.SubElement(document, "name")
document_name.text = sys.argv[1]

folder = et.SubElement(document, "Folder")
folder_name = et.SubElement(folder, "name")
folder_name.text = "Points"

for i in range(n):
    print(".", end='')
    placemark = et.SubElement(folder, "Placemark")
    placemark_name = et.SubElement(placemark, "name")
    placemark_name.text = f"{names[i]} | {cities[i]}, {countries[i]}"

    point = et.SubElement(placemark, "Point")

    coordinates = et.SubElement(point, "coordinates")
    coordinates.text = "{},{},0".format(longs[i], lats[i])

xml_tree = et.ElementTree(kml)
xml_tree.write(sys.argv[1]+".kml", encoding='utf-8', xml_declaration=True)

print()
