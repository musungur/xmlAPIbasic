import xml.etree.ElementTree as et
import xml.dom.minidom as mdom

#xml main element
inventory = et.Element('inventory')

root = et.dump(inventory)
print(f"***xml root tree***\n{root}")
print(f"xml stracture\n{inventory}")


#xml element; should be appended to main element later
computers = et.Element('computers')
inventory.append(computers)
root = et.dump(inventory)
print(f'**\n{inventory}\n****')
#computer's subElement
print("\n computers subElement")
laptops = et.SubElement(computers,'laptops')
desktops = et.SubElement(computers,'desktops')

#computer subelement append
printers = et.Element('printers')

computers.append(printers)

root = et.dump(inventory)

epson = et.Element('epson')
printers.append(epson)
epsonmodel = et.SubElement(epson,'epsonmodel')
epsonmodel.text = "epson mode-1"
root =et.dump(inventory)
#print(root)




