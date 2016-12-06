
import html
import unittest

class testHtmlMethods(unittest.TestCase):

    def test_html_object_exists(self):
        self.assertTrue(html.htmlFile())

    def test_empty_body_on_html_create(self):
        oHtml = html.htmlFile()
        self.assertFalse(oHtml.items)

    def test_add_to_html(self):
        oHtml = html.htmlFile()
        oHtml.add_item('This is body text')
        self.assertEqual(oHtml.items, ['This is body text'])

    def test_body_object_exists(self):
        self.assertTrue(html.body())

    def test_header_object_exists(self):
        self.assertTrue(html.header())

    def test_script_object_exists(self):
        self.assertTrue(html.script('Hello'))

    def test_script_object_source_item(self):
	oScript = html.script('Hello')
	self.assertEqual(oScript.source,'Hello')

    def test_add_script_to_header(self):
	oScript = html.script('Hello')
	oHeader = html.header()
	oHeader.add_item(oScript)
	self.assertEqual(oHeader.items[0].source,'Hello')

    def test_script_create(self):
        oScript = html.script('Hello')
        self.assertEqual(oScript.create(),'<script src="Hello"></script>')


    def test_add_bootstrap_to_header(self):
	oHeader = html.header()
	oHeader.add_bootstrap()
	self.assertEqual(oHeader.items[0].items[0],'charset="utf-8"')
	self.assertEqual(oHeader.items[1].items[0],'name="viewport"')
	self.assertEqual(oHeader.items[1].items[1],'content="width=device-width, initial-scale=1"')
	self.assertEqual(oHeader.items[2].rel,'stylesheet')
        self.assertEqual(oHeader.items[2].href,'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css')
	self.assertEqual(oHeader.items[3].source,'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
	self.assertEqual(oHeader.items[4].source,'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')

    def test_header_create_with_empty_item_list(self):
        oHeader = html.header()
        self.assertEqual(oHeader.create(),['<head>','</head>'])

    def test_header_create_with_script(self):
        oHeader = html.header()
        oHeader.add_item(html.script('Hello'))
        self.assertEqual(oHeader.create(),['<head>','<script src="Hello"></script>','</head>'])

    def test_meta(self):
        oMeta = html.meta()
        oMeta.add_item('name="viewport"')
        self.assertEqual(oMeta.items[0],'name="viewport"')

    def test_link_definition(self):
        oLink = html.link()
        oLink.rel = 'Hello'
        oLink.href = 'Goodbye'
        self.assertEqual(oLink.rel,'Hello')
        self.assertEqual(oLink.href,'Goodbye')

    def test_link_create(self):
        oLink = html.link()
        oLink.rel = 'Hello'
        oLink.href = 'Goodbye'
        self.assertEqual(oLink.create(),'<link rel="Hello" href="Goodbye">')

    def test_meta_create(self):
        oMeta = html.meta()
        oMeta.add_item('one')
        self.assertEqual(oMeta.create(),'<meta one>')
        oMeta.add_item('two')
        self.assertEqual(oMeta.create(),'<meta one two>')
        oMeta.add_item('three')
        self.assertEqual(oMeta.create(),'<meta one two three>')

    def test_header_create_with_bootstrap(self):
        lResult = []
        lResult.append('  <head>')
        lResult.append('    <meta charset="utf-8">')
        lResult.append('    <meta name="viewport" content="width=device-width, initial-scale=1">')
        lResult.append('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
        lResult.append('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>')
        lResult.append('    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
        lResult.append('  </head>')
        oHeader = html.header()
        oHeader.add_bootstrap()
        self.assertEqual(oHeader.create(indent=2),lResult)

    def test_html_create_with_bootstrap(self):
        lResult = []
        lResult.append('<html lang="en">')
        lResult.append('  <head>')
        lResult.append('    <meta charset="utf-8">')
        lResult.append('    <meta name="viewport" content="width=device-width, initial-scale=1">')
        lResult.append('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
        lResult.append('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>')
        lResult.append('    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
        lResult.append('  </head>')
        lResult.append('</html>')
        oHeader = html.header()
        oHeader.add_bootstrap()
        oHtml = html.htmlFile()
        oHtml.add_item(oHeader)
        self.assertEqual(oHtml.create(),lResult)

    def test_tag_name(self):
       oTag = html.tag('tag_name')
       self.assertEqual(oTag.name,'tag_name')

    def test_tag_items(self):
       oTag = html.tag('tag_name')
       self.assertEqual(oTag.items,None)
       oTag.add_item('Item One')
       self.assertEqual(oTag.items[0],'Item One')
       oTag.add_item('Item Two')
       self.assertEqual(oTag.items[0],'Item One')
       self.assertEqual(oTag.items[1],'Item Two')

    def test_tag_create_empty_items(self):
       oTag = html.tag('tag')
       self.assertEqual(oTag.create(),['<tag>','</tag>'])

    def test_tag_create_empty_items_indent(self):
       oTag = html.tag('tag')
       self.assertEqual(oTag.create(indent=2,level=1),['  <tag>','  </tag>'])

    def test_tag_create_with_items_indent(self):
       lResult = []
       lResult.append('  <tag1>')
       lResult.append('    <tag2>')
       lResult.append('      <tag3>')
       lResult.append('      </tag3>')
       lResult.append('    </tag2>')
       lResult.append('  </tag1>')
       oTag3 = html.tag('tag3')
       oTag2 = html.tag('tag2')
       oTag1 = html.tag('tag1')
       oTag2.add_item(oTag3)
       oTag1.add_item(oTag2)
       self.assertEqual(oTag1.create(indent=2,level=1),lResult)

    def test_tag_create_with_source(self):
       lResult = []
       lResult.append('<tag src="source">')
       lResult.append('</tag>')
       oTag = html.tag('tag')
       oTag.source = 'source'
       self.assertEqual(oTag.create(),lResult)

if __name__ == '__main__':
    unittest.main()
