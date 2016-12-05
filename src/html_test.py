
import html
import unittest

class testHtmlMethods(unittest.TestCase):

    def test_html_object_exists(self):
        self.assertTrue(html.htmlFile())

    def test_empty_body_on_html_create(self):
        oHtml = html.htmlFile()
        self.assertFalse(oHtml.item)

    def test_add_to_html(self):
        oHtml = html.htmlFile()
        oHtml.add_item('This is body text')
        self.assertEqual(oHtml.item, ['This is body text'])

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
	self.assertEqual(oHeader.item[0].source,'Hello')

    def test_script_create(self):
        oScript = html.script('Hello')
        self.assertEqual(oScript.create(),'<script>Hello</script>')


    def test_add_bootstrap_to_header(self):
	oHeader = html.header()
	oHeader.add_bootstrap()
	self.assertEqual(oHeader.item[0],'<meta charset="utf-8">')
	self.assertEqual(oHeader.item[1],'<meta name="viewport" content="width=device-width, initial-scale=1">')
	self.assertEqual(oHeader.item[2],'<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
	self.assertEqual(oHeader.item[3].source,'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
	self.assertEqual(oHeader.item[4].source,'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')

    def test_header_create_with_empty_item_list(self):
        oHeader = html.header()
        self.assertEqual(oHeader.create(),['<head>','</head>'])

    def test_header_create_with_script(self):
        oHeader = html.header()
        oHeader.add_item(html.script('Hello'))
        self.assertEqual(oHeader.create(),['<head>','<script>Hello</script>','</head>'])

if __name__ == '__main__':
    unittest.main()
