
import html
import unittest

class testHtmlMethods(unittest.TestCase):

    def test_html_object_exists(self):
        self.assertTrue(html.html())

    def test_empty_body_on_html_create(self):
        oHtml = html.html()
        self.assertFalse(oHtml.tags)

    def test_add_to_html(self):
        oHtml = html.html()
        oHtml.add_tag('This is body text')
        self.assertEqual(oHtml.tags, ['This is body text'])

    def test_body_object_exists(self):
        self.assertTrue(html.body())

    def test_header_object_exists(self):
        self.assertTrue(html.head())

    def test_script_object_exists(self):
        self.assertTrue(html.script('Hello'))

    def test_script_object_source_item(self):
	oScript = html.script('Hello')
	self.assertEqual(oScript.source,'Hello')

    def test_add_script_to_header(self):
	oScript = html.script('Hello')
	oHeader = html.head()
	oHeader.add_tag(oScript)
	self.assertEqual(oHeader.tags[0].source,'Hello')

    def test_script_create(self):
        oScript = html.script('Hello')
        self.assertEqual(oScript.create(),['<script src="Hello">','</script>'])

    def test_add_bootstrap_to_header(self):
	oHeader = html.head()
	oHeader.add_bootstrap()
	self.assertEqual(oHeader.tags[0].meta_items[0],'charset="utf-8"')
	self.assertEqual(oHeader.tags[1].meta_items[0],'name="viewport"')
	self.assertEqual(oHeader.tags[1].meta_items[1],'content="width=device-width, initial-scale=1"')
	self.assertEqual(oHeader.tags[2].rel,'stylesheet')
        self.assertEqual(oHeader.tags[2].href,'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css')
	self.assertEqual(oHeader.tags[3].source,'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
	self.assertEqual(oHeader.tags[4].source,'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')

    def test_header_create_with_empty_item_list(self):
        oHeader = html.head()
        self.assertEqual(oHeader.create(),['<head>','</head>'])

    def test_header_create_with_script(self):
        oHeader = html.head()
        oHeader.add_tag(html.script('Hello'))
        self.assertEqual(oHeader.create(),['<head>','<script src="Hello">','</script>','</head>'])

    def test_meta(self):
        oMeta = html.meta()
        oMeta.add_tag('name="viewport"')
        self.assertEqual(oMeta.tags[0],'name="viewport"')

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
        self.assertEqual(oLink.create(),['<link rel="Hello" href="Goodbye">'])

    def test_meta_create(self):
        oMeta = html.meta()
        oMeta.add_meta_item('one')
        self.assertEqual(oMeta.create(),['<meta one>'])
        oMeta.add_meta_item('two')
        self.assertEqual(oMeta.create(),['<meta one two>'])
        oMeta.add_meta_item('three')
        self.assertEqual(oMeta.create(),['<meta one two three>'])

    def test_header_create_with_bootstrap(self):
        lResult = []
        lResult.append('  <head>')
        lResult.append('    <meta charset="utf-8">')
        lResult.append('    <meta name="viewport" content="width=device-width, initial-scale=1">')
        lResult.append('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
        lResult.append('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js">')
        lResult.append('    </script>')
        lResult.append('    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js">')
        lResult.append('    </script>')
        lResult.append('  </head>')
        oHeader = html.head()
        oHeader.add_bootstrap()
        self.assertEqual(oHeader.create(indent=2,level=1),lResult)

    def test_html_create_with_bootstrap(self):
        lResult = []
        lResult.append('<html lang="en">')
        lResult.append('  <head>')
        lResult.append('    <meta charset="utf-8">')
        lResult.append('    <meta name="viewport" content="width=device-width, initial-scale=1">')
        lResult.append('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
        lResult.append('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js">')
        lResult.append('    </script>')
        lResult.append('    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js">')
        lResult.append('    </script>')
        lResult.append('  </head>')
        lResult.append('</html>')
        oHeader = html.head()
        oHeader.add_bootstrap()
        oHtml = html.html()
        oHtml.add_tag(oHeader)
        self.assertEqual(oHtml.create(indent=2),lResult)

    def test_tag_name(self):
       oTag = html.tag('tag_name')
       self.assertEqual(oTag.name,'tag_name')

    def test_tag_items(self):
       oTag = html.tag('tag_name')
       self.assertEqual(oTag.tags,None)
       oTag.add_tag('Item One')
       self.assertEqual(oTag.tags[0],'Item One')
       oTag.add_tag('Item Two')
       self.assertEqual(oTag.tags[0],'Item One')
       self.assertEqual(oTag.tags[1],'Item Two')

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
       oTag2.add_tag(oTag3)
       oTag1.add_tag(oTag2)
       self.assertEqual(oTag1.create(indent=2,level=1),lResult)

    def test_tag_class(self):
       oTag = html.tag('tag')
       oTag.add_class('class1')
       self.assertEqual(oTag.create(),['<tag class="class1">','</tag>'])
       oTag.add_class('class2')
       self.assertEqual(oTag.create(),['<tag class="class1 class2">','</tag>'])
       oTag.add_class('class3')
       self.assertEqual(oTag.create(),['<tag class="class1 class2 class3">','</tag>'])

    def test_tag_create_with_source(self):
       lResult = []
       lResult.append('<tag src="source">')
       lResult.append('</tag>')
       oTag = html.tag('tag')
       oTag.source = 'source'
       self.assertEqual(oTag.create(),lResult)


    def test_basic_html_structure(self):
       lResult = []
       lResult.append('<html lang="en">')
       lResult.append('  <head>')
       lResult.append('  </head>')
       lResult.append('  <body>')
       lResult.append('  </body>')
       lResult.append('</html>')
       oHtml = html.html()
       oHtml.add_tag(html.head())
       oHtml.add_tag(html.body())
       self.assertEqual(oHtml.create(indent=2),lResult)

    def test_nav_bar_creation(self):
       lResult = []
       lResult.append('<nav class="navbar navbar-inverse navbar-fixed-top">')
       lResult.append('  <div class="container-fluid">')
       lResult.append('    <div class="navbar-header">')
       lResult.append('      <a href="#" class="navbar-brand">')
       lResult.append('        Block C')
       lResult.append('      </a>')
       lResult.append('    </div>')
       lResult.append('    <ul class="nav navbar-nav">')
       lResult.append('      <li>')
       lResult.append('        <a href="#block-overview">')
       lResult.append('          Overview')
       lResult.append('        </a>')
       lResult.append('      </li>')
       lResult.append('      <li>')
       lResult.append('        <a href="#block-features">')
       lResult.append('          Features')
       lResult.append('        </a>')
       lResult.append('      </li>')
       lResult.append('      <li>')
       lResult.append('        <a href="#block-interface-diagram">')
       lResult.append('          Interface Diagram')
       lResult.append('        </a>')
       lResult.append('      </li>')
       lResult.append('      <li>')
       lResult.append('        <a href="#block-interfaces">')
       lResult.append('          Interfaces')
       lResult.append('        </a>')
       lResult.append('      </li>')
       lResult.append('      <li>')
       lResult.append('        <a href="#block-block-diagram">')
       lResult.append('          Block Diagram')
       lResult.append('        </a>')
       lResult.append('      </li>')
       lResult.append('    </ul>')
       lResult.append('  </div>')
       lResult.append('</nav>')
       oNav = html.nav()
       oNav.add_class('navbar')
       oNav.add_class('navbar-inverse')
       oNav.add_class('navbar-fixed-top')
       oDiv = html.div()
       oDiv.add_class('container-fluid')
       oNav.add_tag(oDiv)
       oLink = html.a('Block C')
       oLink.add_class('navbar-brand')
       oLink.href = '#'
       oDiv = html.div()
       oDiv.add_class('navbar-header')
       oDiv.add_tag(oLink)
       oNav.tags[0].add_tag(oDiv)
       oUl = html.ul()
       oUl.add_class('nav')
       oUl.add_class('navbar-nav')
       # Create overview list element
       oLi = html.li()
       oLink = html.a('Overview')
       oLink.href = '#block-overview'
       oLi.add_tag(oLink)
       oUl.add_tag(oLi)
       # Create Features list element
       oLi = html.li()
       oLink = html.a('Features')
       oLink.href = '#block-features'
       oLi.add_tag(oLink)
       oUl.add_tag(oLi)
       # Create Interface Diagrams list element
       oLi = html.li()
       oLink = html.a('Interface Diagram')
       oLink.href = '#block-interface-diagram'
       oLi.add_tag(oLink)
       oUl.add_tag(oLi)
       # Create Interfaces list element
       oLi = html.li()
       oLink = html.a('Interfaces')
       oLink.href = '#block-interfaces'
       oLi.add_tag(oLink)
       oUl.add_tag(oLi)
       # Create Block Diagram list element
       oLi = html.li()
       oLink = html.a('Block Diagram')
       oLink.href = '#block-block-diagram'
       oLi.add_tag(oLink)
       oUl.add_tag(oLi)
       # Add UL to Nav
       oNav.tags[0].add_tag(oUl)
       self.assertEqual(oNav.create(indent=2),lResult)

if __name__ == '__main__':
    unittest.main()
