
import sys
sys.path.append('../../src')
import xray
import os

def main():

    # Create the document
    oDocument = xray.document()

    # Add the system document
    oDocument.add_object(xray.system('xray-system.adoc'))

    # Add the device
    oDocument.add_object(xray.device('xray-device_a.adoc'))

    # Add the device
    oDocument.add_object(xray.device('xray-device_b.adoc'))

    # Create the HTML
    oDocument.create_html()

if __name__ == '__main__':
    main()
