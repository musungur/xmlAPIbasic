import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

#Inventory Root Element
inventory = ET.Element('inventory')

ET.dump(inventory)
print("printing dump")
print(ET.dump(inventory))
print("\nPrinting ET.tostring\n")
print(ET.tostring(inventory))
print('\n')
computers = ET.Element('computers')
# append Element computer into Inventory
inventory.append(computers)
print(ET.dump(inventory))

desktops = ET.SubElement(computers,'desktops')
laptops = ET.SubElement(computers,'laptops')

# Printer Element
printers = ET.Element('printes')

#append printers into Inventory
inventory.append(printers)
print(ET.dump(inventory))
#printer subElements
canons = ET.SubElement(printers,'canons')
epsons = ET.SubElement(printers,'epsons')
ricohs = ET.SubElement(printers,'ricohs')
kyoceras = ET.SubElement(printers,'kyoceras')

print(ET.dump(inventory))
## Destops
robertm = ET.SubElement(desktops,'robertm')
robertm.text = 'ROBERTM'
kerubop =ET.SubElement(desktops,'kerubop')
kerubop.text = 'KERUBOP'
fred = ET.SubElement(desktops,'fred')
fred.text = 'FOSEWE'

## Laptops
penina = ET.SubElement(laptops,'peninao')
penina.text = 'PENINAO'
richard = ET.SubElement(laptops,'richard')
richard.text = 'RKARIUKI'
hillary = ET.SubElement(laptops,'hillary')
hillary.text = 'HLANGAT'

## Printer Locations
canonsloc = ET.SubElement(canons,'canonloc')
canonsloc.text = 'CEOs residence'

ricohsloc = ET.SubElement(ricohs,'ricohsloc')
ricohsloc.text = 'QC, ADMIN & FGstores'

epsonsloc = ET.SubElement(ricohs,'epsonsloc')
epsonsloc.text = 'Commercial Office & HeadOffcie'

kyocerasloc = ET.SubElement(kyoceras,'kyocerasloc')
kyocerasloc.text = 'R&D Archive'
print(inventory)
print("\nConverting to ET.tostring\n")
text = ET.tostring(inventory)
print(text)
print("end of ET.tostring\n")
print(ET.dump(inventory))
print("\nPrints into pretty")

print(minidom.parseString(ET.tostring(inventory)).toprettyxml())


print("#######################x***xml parse***#########")

myxmlfile = ET.parse('xmlfime.xml')
print(myxmlfile)
root = myxmlfile.getroot
print(root)
print('\n$$$$$$$$$$$$$$$$$$')