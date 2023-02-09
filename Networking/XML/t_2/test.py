import xml.etree.ElementTree as ET
fname= "Library.xml"

stuff=ET.parse(fname)
all=stuff.findall("dict/dict/dict")
for a in all:
    print(a)