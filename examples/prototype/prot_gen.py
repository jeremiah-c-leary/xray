
import sys
sys.path.append('../../src')
import xray
import os

def main():

    # Create the document
    oDocument = xray.document()

    # Add the system document
    oSystem = xray.system('xray-system.adoc')
    oDocument.add_object(oSystem)

    # Add first device
    oDeviceA = xray.device('xray-device_a.adoc', 'xray_system')
    oDocument.add_object(oDeviceA)

    # Add second device
    oDeviceB = xray.device('xray-device_b.adoc', 'xray_system')
    oDocument.add_object(oDeviceB)

    # Create some interfaces
    oInterfaceA = xray.interface('xray-interface_a.adoc', 'xray_system')
    oInterfaceB = xray.interface('xray-interface_b.adoc', 'xray_system')

    # Create some components
    oComponentA = xray.component('xray-component_a.adoc', 'xray_system')
    oComponentB = xray.component('xray-component_b.adoc', 'xray_system')

    

    oDocument.add_object(oInterfaceA)
    oDocument.add_object(oInterfaceB)
    oDeviceA.add_interface(oInterfaceA)
    oDeviceA.add_interface(oInterfaceB)
    oDeviceA.add_component(oComponentA)
    oDeviceB.add_interface(oInterfaceA)
    oDeviceB.add_component(oComponentA)
    oDeviceB.add_component(oComponentB)

    # Create the HTML
    oDocument.create_html()

if __name__ == '__main__':
    main()
