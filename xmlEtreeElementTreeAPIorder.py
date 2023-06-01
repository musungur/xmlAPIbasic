# Python XML API
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
inventory = ET.Element('inventory')

File = ET.dump(inventory)
computers = ET.Element('computers')

inventory.append(computers)

#ET.dump(inventory)

laptops = ET.SubElement(computers,'laptops')

desktops = ET.SubElement(computers,'desktops')

printers = ET.Element('printers')

inventory.append(printers)

#ET.dump(inventory)

#computer: laptops
kerubop = ET.SubElement(laptops,'kerubop')
kerubop.text = "KERUBOP"
peninao = ET.SubElement(laptops,'PENINAO')
peninao.text = "PENINAO"
rajendraf = ET.SubElement(laptops,'rajendraf')
rajendraf.text = "RFALOR"
robertm = ET.SubElement(laptops,'robertm')
robertm.text = 'ROBERTM'
#computers: Desktops
isoe = ET.SubElement(desktops,'isoe')
isoe.text = 'BENETICI'
ramaitan = ET.SubElement(desktops,'ramaitan')
ramaitan.text = 'NRAMAITA'
ericko = ET.SubElement(desktops,'ericko')
ericko.text = "EONYANGO"
manjult = ET.SubElement(desktops,'manjult')
manjult.text = "MANJULT"

# Printers details: models
canons = ET.SubElement(printers,'canons')
canons.text = "CEO's office HQ"
epson = ET.SubElement(printers,'epson')
epson.text = 'cEO office - BO'
kyocera = ET.SubElement(printers,'kyocera')
kyocera.text = "R and D Archive"
ricoh = ET.SubElement(printers,'ricoh')
ricoh.text = 'QC, R and D, ADMIN and FGSTORES'
hpprinter = ET.SubElement(printers,'hpprinter')
hpprinter.text = 'RF,RM,QC,CO'

# Attributes to
computers.attrib['info'] = "computer assets"
printers.attrib['info'] = "printer assets"

print('****to plain XML text****\n')
xmlText = ET.dump(inventory)
print("*****END****\n")

print(f"****xml text***\n {xmlText} \n********\n to XML String")

string = ET.tostring(inventory)

# print(f'\n***printing to string\n{string}')
print('\n*****End of XML String\n')

minidom.parseString(ET.tostring(inventory)).toprettyxml()
#invetorystring = ET.dump(inventory)
pprettyxmlfileformat = minidom.parseString(string).toprettyxml()

print('*****printing XML to Pretty Format*******\n')
print(f'pretty xml format\n{pprettyxmlfileformat}\n****END****')