
import vhdl
import unittest


class testVhdl(unittest.TestCase):

    def test_port_creation(self):
        oPort = vhdl.port('name1','direction','type','comment')
        self.assertEqual(oPort.name,'name1')
        self.assertEqual(oPort.direction,'direction')
        self.assertEqual(oPort.type,'type')
        self.assertEqual(oPort.comment,'comment')

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

if __name__ == '__main__':
    unittest.main()
