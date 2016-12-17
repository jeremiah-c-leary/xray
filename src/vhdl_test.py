import html
import vhdl
import unittest


class testVhdl(unittest.TestCase):

    def test_port_creation(self):
        oPort = vhdl.port('name1','direction','type','comment')
        self.assertEqual(oPort.name,'name1')
        self.assertEqual(oPort.direction,'direction')
        self.assertEqual(oPort.type,'type')
        self.assertEqual(oPort.comment,'comment')

    def test_port_html(self):
        oPort = vhdl.port('name1','direction','type','comment')
        lExpected = []
        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('name1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('direction')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('type')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment')
        lExpected.append('</td>')
        lExpected.append('</tr>')
        self.assertEqual(oPort.build_html().create(),lExpected)

    def test_interface_creation(self):
        oInterface = vhdl.interface('name2')
        self.assertEqual(oInterface.name,'name2')

    def test_interface_with_ports(self):
        oInterface = vhdl.interface('name3')
        oInterface.add_port(vhdl.port('port1','in','std_logic','comment1'))
        oInterface.add_port(vhdl.port('port2','out','std_logic_vector(13 downto 0)','comment2'))
        self.assertEqual(oInterface.name,'name3')
        self.assertEqual(oInterface.ports[0].name,'port1')
        self.assertEqual(oInterface.ports[0].direction,'in')
        self.assertEqual(oInterface.ports[0].type,'std_logic')
        self.assertEqual(oInterface.ports[0].comment,'comment1')
        self.assertEqual(oInterface.ports[1].name,'port2')

    def test_interface_with_port_html(self):
        oInterface = vhdl.interface('name3')
        oInterface.add_port(vhdl.port('port1','in','std_logic','comment1'))
        oInterface.add_port(vhdl.port('port2','out','std_logic_vector(13 downto 0)','comment2'))
        oInterface.add_port(vhdl.port('port3','out','std_logic_vector(0 to 6)','comment3'))
        lExpected = []
        lExpected.append('<tr>')
        lExpected.append('<td colspan="5">')
        lExpected.append('name3')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('in')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment1')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port2')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('14')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('out')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic_vector')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment2')
        lExpected.append('</td>')
        lExpected.append('</tr>')


        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port3')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('7')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('out')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic_vector')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment3')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lResults = []
        for oTag in oInterface.build_html():
            lResults.extend(oTag.create())
        self.assertEqual(lExpected,lResults)


    def test_port_map_creation(self):
        oPortMap = vhdl.port_map()
        self.assertEqual(oPortMap.interfaces,None)

    def test_port_map_with_interfaces(self):
        oPortMap = vhdl.port_map()
        oPortMap.add_interface(vhdl.interface('name1'))
        oPortMap.add_interface(vhdl.interface('name2'))
        oPortMap.add_interface(vhdl.interface('name3'))
        self.assertEqual(oPortMap.interfaces[0].name,'name1')
        self.assertEqual(oPortMap.interfaces[1].name,'name2')
        self.assertEqual(oPortMap.interfaces[2].name,'name3')

    def test_port_map_with_interface_html(self):
        oPortMap = vhdl.port_map()
        oInterface = vhdl.interface('name1')
        oInterface.add_port(vhdl.port('port1','in','std_logic','comment1'))
        oPortMap.add_interface(oInterface)
        oInterface = vhdl.interface('name2')
        oInterface.add_port(vhdl.port('port2','out','std_logic_vector(13 downto 0)','comment2'))
        oPortMap.add_interface(oInterface)

        lExpected = []

        lExpected.append('<table>')
        lExpected.append('<tr>')
        lExpected.append('<th>')
        lExpected.append('Name')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Size')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Direction')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Type')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Description')
        lExpected.append('</th>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td colspan="5">')
        lExpected.append('name1')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('in')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment1')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td colspan="5">')
        lExpected.append('name2')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port2')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('14')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('out')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic_vector')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment2')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('</table>')

        blah = oPortMap.build_html()
        self.assertEqual(oPortMap.build_html().create(),lExpected)


    def test_entity_creation(self):
        oEntity = vhdl.entity()
        self.assertEqual(oEntity.name,None)

    def test_entity_with_port_map(self):
        oEntity = vhdl.entity('entity1')
        oPortMap = vhdl.port_map()
        oPortMap.add_interface(vhdl.interface('name10'))
        oEntity.portMap = oPortMap
        self.assertEqual(oEntity.name,'entity1')
        self.assertEqual(oEntity.portMap.interfaces[0].name,'name10')

    def test_entity_with_port_map_html(self):
        oEntity = vhdl.entity('entity1')
        oPortMap = vhdl.port_map()
        oInterface = vhdl.interface('name1')
        oInterface.add_port(vhdl.port('port1','in','std_logic','comment1'))
        oPortMap.add_interface(oInterface)
        oInterface = vhdl.interface('name2')
        oInterface.add_port(vhdl.port('port2','out','std_logic_vector(13 downto 0)','comment2'))
        oPortMap.add_interface(oInterface)

        lExpected = []

        lExpected.append('<table>')
        lExpected.append('<tr>')
        lExpected.append('<th>')
        lExpected.append('Name')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Size')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Direction')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Type')
        lExpected.append('</th>')
        lExpected.append('<th>')
        lExpected.append('Description')
        lExpected.append('</th>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td colspan="5">')
        lExpected.append('name1')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('1')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('in')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment1')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td colspan="5">')
        lExpected.append('name2')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('<tr>')
        lExpected.append('<td>')
        lExpected.append('port2')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('14')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('out')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('std_logic_vector')
        lExpected.append('</td>')
        lExpected.append('<td>')
        lExpected.append('comment2')
        lExpected.append('</td>')
        lExpected.append('</tr>')

        lExpected.append('</table>')

        oEntity.portMap = oPortMap

        lResults = []
        for oTag in oEntity.build_html():
            lResults.extend(oTag.create())
        self.assertEqual(lExpected,lResults)


if __name__ == '__main__':
    unittest.main()
