
import sys
sys.path.append('..')
import unittest
import xray
import os


class testAsciidocMethods(unittest.TestCase):

    def test_interface_exists(self):
        self.assertEqual(xray.interface('xray-interface_a.adoc', 'xray_system').sFilename,'xray-interface_a.adoc')

    def test_interface_name(self):
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        self.assertEqual(oInterface.sName, 'Interface A')

    def test_interface_builds_html(self):
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        lResults = []
        for oHtml in oInterface.build_html():
            lResults.extend(oHtml.create())
        lExpected = []
        lExpected.extend(['<h1>','Interface A','</h1>'])
        lExpected.extend(['<p>','Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Fusce aliquet eleifend ante, a vestibulum dui.  Sed vel arcu eu erat viverra finibus eget ut dolor.  In blandit, est tincidunt ornare vehicula, metus neque consectetur nulla, ac venenatis orci tortor nec libero.  Vestibulum vitae metus odio.','</p>'])
        self.assertEqual(lResults[0:6],lExpected)
         
    def test_system_exits(self):
        self.assertEqual(xray.system('xray-system.adoc').sFilename,'xray-system.adoc')

    def test_system_builds_html(self):
        oSystem = xray.system('xray-system.adoc')
        lResults = []
        for oHtml in oSystem.build_html():
            lResults.extend(oHtml.create()) 
        lExpected = []
        lExpected.extend(['<h1>','Xray System','</h1>'])
        lExpected.extend(['<p>', 'Aenean in erat quam.  Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.  Cras quis tellus sem.  Nunc ultrices velit eu vestibulum hendrerit.  Curabitur et lectus mattis, iaculis dolor in, commodo nisl.  Praesent nec purus ut augue viverra mattis at sit amet purus.  Sed at nisi iaculis, vehicula dui non, finibus eros.  Aliquam ac vehicula orci, vel ultricies libero.  Nam venenatis sollicitudin risus, a pulvinar sapien tincidunt ut.  In fringilla interdum mollis.  Aenean leo libero, egestas at lectus quis, consequat porta urna.  Vestibulum consectetur ligula et velit tincidunt interdum.  Nullam mollis tincidunt fringilla.  Quisque consectetur libero nulla, sed pretium nibh tincidunt ac.  Nam consequat efficitur lectus, sed vulputate nibh gravida quis.','</p>'])

        self.assertEqual(lResults[0:6],lExpected)
        
    def test_document_exists(self):
        self.assertEqual(xray.document().lObjects,None)

    def test_document_add_object(self):
        oDocument = xray.document()
        oDocument.add_object(xray.system(None))
        self.assertEqual(len(oDocument.lObjects),1)
        self.assertEqual(oDocument.lObjects[0].sFilename,None)

    def test_document_creates_system_file(self):
        if os.path.exists('xray_system-system.html'):
            os.remove('xray_system-system.html')
        oDocument = xray.document()
        oDocument.add_object(xray.system('xray-system.adoc'))
        oDocument.create_html()
        self.assertTrue(os.path.exists('xray_system-system.html'))

    def test_document_builds_system(self):
        if os.path.exists('xray_system-system.html'):
            os.remove('xray_system-system.html')
        oDocument = xray.document()
        oDocument.add_object(xray.system('xray-system.adoc'))
        oDocument.create_html()
        with open('xray_system-system.html') as oFile:
            lResults = oFile.readlines()
        with open('xray-document_system-expected.html') as oFile:
            lExpected = oFile.readlines()
        self.assertEqual(lResults, lExpected)

    def test_device_exists(self):
        self.assertEqual(xray.device('xray-device_a.adoc', 'xray_system').sFilename,'xray-device_a.adoc')

    def test_device_build_html(self):
        oDevice = xray.device('xray-device_a.adoc', 'xray_system')
        lResults = []
        for oHtml in oDevice.build_html():
          lResults.extend(oHtml.create()) 
        lExpected = []
        lExpected.extend(['<h1>','Device A','</h1>'])
        lExpected.extend(['<p>','Tri-tip burgdoggen ground round turducken, ham venison drumstick t-bone kevin shank filet mignon short ribs brisket flank. Landjaeger tri-tip ribeye, drumstick andouille salami tenderloin beef swine pastrami porchetta chicken. Pork loin t-bone prosciutto landjaeger, shank ball tip pastrami pork. Tail drumstick shank, sausage flank brisket short ribs rump tenderloin. Short loin boudin sausage swine kevin. Short loin drumstick venison brisket turkey chuck ham pork chop beef ribs.','</p>'])
        self.assertEqual(lResults[0:6],lExpected)

    def test_device_name(self):
        oDevice = xray.device('xray-device_a.adoc', 'xray_system')
        self.assertEqual(oDevice.sName,'Device A')

    def test_device_adding_interface(self):
        oDevice = xray.device('xray-device_a.adoc', 'xray_system')
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        oDevice.add_interface(oInterface)
        self.assertEqual(oDevice.lInterfaces[0].sName, 'Interface A')

    def test_device_create_navbar(self):
        oDevice = xray.device('xray-device_a.adoc', 'xray_system')
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        oDevice.add_interface(oInterface)
        lExpected = []
        with open('device-build_navbar-expected.html') as oFile:
            for sLine in oFile:
                lExpected.append(sLine.rstrip())
        self.assertEqual(oDevice.create_navbar().create(), lExpected)

    def test_device_with_component(self):
        oDevice = xray.device('xray-device_a.adoc', 'xray_system')
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        oDevice.add_component(oComponent)
        self.assertEqual(oDevice.lComponents[0].sName, 'Component A')

    def test_component_exists(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        self.assertEqual(oComponent.sFilename, 'xray-component_a.adoc')

    def test_component_name(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        self.assertEqual(oComponent.sName, 'Component A')

    def test_component_html_filename(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        self.assertEqual(oComponent.sHtmlFilename, 'xray_system-component_a.html')

    def test_component_with_interfaces(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        oComponent.add_interface(oInterface)
        self.assertEqual(oComponent.lInterfaces[0].sName, 'Interface A')

    def test_component_with_component(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        oComponent2 = xray.component('xray-component_b.adoc', 'xray_system')
        oComponent.add_component(oComponent2)
        self.assertEqual(oComponent.lComponents[0].sName, 'Component B')

    def test_component_with_component_with_interface(self):
        oComponent = xray.component('xray-component_a.adoc', 'xray_system')
        oComponent2 = xray.component('xray-component_b.adoc', 'xray_system')
        oInterface = xray.interface('xray-interface_a.adoc', 'xray_system')
        oComponent2.add_interface(oInterface)
        oComponent.add_component(oComponent2)
        self.assertEqual(oComponent.lComponents[0].lInterfaces[0].sName, 'Interface A')

if __name__ == '__main__':
    unittest.main()
