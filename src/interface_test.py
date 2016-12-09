import interface
import unittest

class testInterfaceMethos(unittest.TestCase):

    def test_interface_creation(self):
        oInterface = interface.create('Watchdog')
        self.assertEqual(oInterface.name,'Watchdog')

    def test_signal_creation(self):
        oSignal = interface.signal('Signal Name',4,'Signal Description')
        self.assertEqual(oSignal.name,'Signal Name')
        self.assertEqual(oSignal.width,4)
        self.assertEqual(oSignal.description,'Signal Description')

    def test_protocol_creation(self):
        oProtocol = interface.protocol('First Protocol')
        self.assertEqual(oProtocol.name,'First Protocol')

    def test_protocol_paragraphs(self):
        oProtocol = interface.protocol('First Protocol')
        oProtocol.add_paragraph('This is the first paragraph.  This is not very long.')
        oProtocol.add_paragraph('This is the second paragraph.  This is also not very long.')
        self.assertEqual(oProtocol.paragraphs[0],'This is the first paragraph.  This is not very long.')
        self.assertEqual(oProtocol.paragraphs[1],'This is the second paragraph.  This is also not very long.')

    def test_protocol_image_link(self):
        oProtocol = interface.protocol('First Protocol')
        self.assertEqual(oProtocol.imageLink,None)
        oProtocol.imageLink = 'This is an image link'
        self.assertEqual(oProtocol.imageLink,'This is an image link')

    def test_interface_with_signals(self):
        oInterface = interface.create('First Interface')
        oSignal = interface.signal('Signal Name1',1,'Signal Description1')
        self.assertEqual(oSignal.name,'Signal Name1')
        self.assertEqual(oSignal.width,1)
        self.assertEqual(oSignal.description,'Signal Description1')
        oInterface.add_signal(oSignal)
        oSignal = interface.signal('Signal Name2',4,'Signal Description2')
        self.assertEqual(oSignal.name,'Signal Name2')
        self.assertEqual(oSignal.width,4)
        self.assertEqual(oSignal.description,'Signal Description2')
        oInterface.add_signal(oSignal)
        self.assertEqual(oInterface.signals[0].name,'Signal Name1')
        self.assertEqual(oInterface.signals[1].name,'Signal Name2')
        self.assertEqual(oInterface.signals[0].width,1)
        self.assertEqual(oInterface.signals[1].width,4)
        self.assertEqual(oInterface.signals[0].description,'Signal Description1')
        self.assertEqual(oInterface.signals[1].description,'Signal Description2')

    def test_signal_create_html(self):
        lResults = []
        lResults.append('<tr>')
        lResults.append('<td>signal 1</td><td>4</td><td>This is a description</td>')
        lResults.append('</tr>')
        oSignal = interface.signal('signal 1',4,'This is a description')
        self.assertEqual(oSignal.create(),lResults)

    def test_protocol_create_html(self):
        lResults = []
        lResults.append('<h3>Interface 1</h3>')
        lResults.append('<p>This is paragraph 1</p>')
        lResults.append('<p>This is paragraph 2</p>')
        lResults.append('<table class="table table-striped table-bordered">')
        lResults.append('<tr>')
        lResults.append('<th>Signal</th><th>Width</th><th>Description</th>')
        lResults.append('</tr>')
        lResults.append('<tr>')
        lResults.append('<td>Signal 1</td><td>4</td><td>This is a description</td>')
        lResults.append('</tr>')
        lResults.append('<tr>')
        lResults.append('<td>Signal 2</td><td>16</td><td>This is another description</td>')
        lResults.append('</tr>')
        lResults.append('</table>')
        lResults.append('<h4>Protocol 1</h4>')
        lResults.append('<p>This is a protocol paragraph</p>')
        lResults.append('<img src="image source" class="img-responsive">')
        oSignal = interface.signal('Signal 1',4,'This is a description')
        oInterface = interface.create('Interface 1')
        oInterface.add_signal(oSignal)
        oSignal = interface.signal('Signal 2',16,'This is another description')
        oInterface.add_signal(oSignal)
        oProtocol = interface.protocol('Protocol 1')
        oProtocol.add_paragraph('This is a protocol paragraph')
        oProtocol.imageLink = 'image source'
        oInterface.add_protocol(oProtocol)
        oInterface.add_paragraph('This is paragraph 1')
        oInterface.add_paragraph('This is paragraph 2')
        self.assertEqual(oInterface.create(),lResults)

if __name__ == '__main__':
    unittest.main()

