
import sys
sys.path.append('..')
import unittest
import xray
import os

class testAsciidocMethods(unittest.TestCase):

    def test_interface_list_exists(self):
        self.assertEqual(xray.interfaces().lInterfaces,[])


    def test_system_exits(self):
        self.assertEqual(xray.system('filename.blah').sFilename,'filename.blah')

    def test_system_builds_html(self):
        self.maxDiff = None
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
        oDocument.add_object(xray.system('filename.blah'))
        self.assertEqual(len(oDocument.lObjects),1)
        self.assertEqual(oDocument.lObjects[0].sFilename,'filename.blah')

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


if __name__ == '__main__':
    unittest.main()
