import sys
sys.path.append('..')
import unittest
import asciidoc


class testAsciidocMethods(unittest.TestCase):

    def test_asciidoc_object_exists(self):
        self.assertTrue(asciidoc.file())

    def test_heading(self):
        self.assertTrue(asciidoc.heading(None,None))

    def test_heading_with_name(self):
        oHeading = asciidoc.heading('heading',None)
        self.assertEqual(oHeading.sTitle,'heading')

    def test_heading_with_level(self):
        oHeading = asciidoc.heading(None,iLevel=2)
        self.assertEqual(oHeading.iLevel,2)

    def test_asciidoc_file_with_headers(self):
        oFile = asciidoc.file()
        oFile.process('asciidoc-headers.adoc')
        self.assertEqual(oFile.objects[0].sTitle,'One Interface')
        self.assertEqual(oFile.objects[0].iLevel,1)
        self.assertEqual(oFile.objects[1].sTitle,'First Protocol')
        self.assertEqual(oFile.objects[1].iLevel,2)
        self.assertEqual(oFile.objects[2].sTitle,'Second Protocol')
        self.assertEqual(oFile.objects[2].iLevel,2)
        self.assertEqual(oFile.objects[3].sTitle,'Third level header')
        self.assertEqual(oFile.objects[3].iLevel,3)
        self.assertEqual(oFile.objects[4].sTitle,'Fourth level header')
        self.assertEqual(oFile.objects[4].iLevel,4)
        self.assertEqual(oFile.objects[5].sTitle,'Fifth level header')
        self.assertEqual(oFile.objects[5].iLevel,5)

    def test_paragraph(self):
        oParagraph = asciidoc.paragraph('paragraph')
        self.assertEqual(oParagraph.sParagraph,'paragraph')

    def test_asciidoc_file_with_headers_and_paragraphs(self):
        oFile = asciidoc.file()
        oFile.process('asciidoc-paragraphs.adoc')
        self.assertEqual(oFile.objects[0].sTitle,'One Interface')
        self.assertEqual(oFile.objects[0].iLevel,1)
        self.assertEqual(oFile.objects[1].sParagraph,'Paragraph one.')
        self.assertEqual(oFile.objects[2].sTitle,'First Protocol')
        self.assertEqual(oFile.objects[2].iLevel,2)
        self.assertEqual(oFile.objects[3].sParagraph,'Sentence one.  Sentence two.  Sentence three.')
        self.assertEqual(oFile.objects[4].sTitle,'Second Protocol')
        self.assertEqual(oFile.objects[4].iLevel,2)
        self.assertEqual(oFile.objects[5].sParagraph,'Sentence four.')
        self.assertEqual(oFile.objects[6].sParagraph,'Sentence five.')
        self.assertEqual(oFile.objects[7].sTitle,'Third level header')
        self.assertEqual(oFile.objects[7].iLevel,3)
        self.assertEqual(oFile.objects[8].sParagraph,'Sentence six.')
        self.assertEqual(oFile.objects[9].sTitle,'Fourth level header')
        self.assertEqual(oFile.objects[9].iLevel,4)
        self.assertEqual(oFile.objects[10].sParagraph,'Sentence seven.')
        self.assertEqual(oFile.objects[11].sTitle,'Fifth level header')
        self.assertEqual(oFile.objects[11].iLevel,5)
        self.assertEqual(oFile.objects[12].sParagraph,'Sentence eight  sentence nine')
        self.assertEqual(oFile.objects[13].sParagraph,'sentence ten  sentence eleven')


    def test_block_image_object(self):
        oImage = asciidoc.block_image('image_path')
        self.assertEqual(oImage.sImagePath,'image_path')

    def test_asciidoc_file_with_images(self):
        oFile = asciidoc.file()
        oFile.process('asciidoc-images.adoc')
        self.assertEqual(oFile.objects[0].sTitle,'One Interface')
        self.assertEqual(oFile.objects[0].iLevel,1)
        self.assertEqual(oFile.objects[1].sParagraph,'Paragraph one.')
        self.assertEqual(oFile.objects[2].sTitle,'First Protocol')
        self.assertEqual(oFile.objects[2].iLevel,2)
        self.assertEqual(oFile.objects[3].sImagePath,'img/image_a.png')
        self.assertEqual(oFile.objects[4].sParagraph,'Sentence one.  image::img/image_b.png[]')


    def test_table_object(self):
        oTable = asciidoc.table()
        oTable.add_row(['one','two','three'])
        self.assertEqual(oTable.lRows[0], ['one','two','three'])

    def test_table_object_with_multiple_rows(self):
        oTable = asciidoc.table()
        oTable.add_row(['one','two','three'])
        oTable.add_row(['four','five','six'])
        self.assertEqual(oTable.lRows[0], ['one','two','three'])
        self.assertEqual(oTable.lRows[1], ['four','five','six'])

    def test_asciidoc_file_with_tables(self):
        oFile = asciidoc.file()
        oFile.process('asciidoc-tables.adoc')
        self.assertEqual(oFile.objects[0].sTitle,'One Interface')
        self.assertEqual(oFile.objects[0].iLevel,1)
        self.assertEqual(oFile.objects[1].sParagraph,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        self.assertEqual(oFile.objects[2].lRows[0],['signal','width','description'])
        self.assertEqual(oFile.objects[2].lRows[1],['sig_one','1','Donec sed sapien eu ligula dictum consectetur.'])
        self.assertEqual(oFile.objects[2].lRows[2],['sig_two','16','Integer sodales ipsum ex, vitae auctor erat tristique nec.'])
        self.assertEqual(oFile.objects[3].sParagraph,'Vestibulum vitae metus odio.')


if __name__ == '__main__':
    unittest.main()
