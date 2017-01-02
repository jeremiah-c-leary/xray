
import sys
sys.path.append('../..')
import unittest
import register
import os


class testRegisterMethods(unittest.TestCase):

    def test_field_exists(self):
        self.assertEqual(register.field(sType='RW', sBits='0', sDefault='0x0').sType,'RW')

    def test_field_description(self):
        oField = register.field(sType='RW', sBits='0', sDefault='0x0')
        oField.add_description('This is a description')
        self.assertEqual(oField.lDescription,['This is a description'])
        oField.add_description('This is more description')
        self.assertEqual(oField.lDescription,['This is a description','This is more description'])

    def test_field_bit(self):
        oField = register.field(sType='RO', sBits='0', sDefault='0x0')
        self.assertEqual(oField.sBits,'0')

    def test_field_single_bit_width(self):
        oField = register.field(sType='RO', sBits='0', sDefault='0x0')
        self.assertEqual(oField.iWidth, 1)

    def test_field_multiple_bit_width(self):
        oField = register.field(sType='RO', sBits='15:0', sDefault='0x0')
        self.assertEqual(oField.iWidth, 16)
        oField = register.field(sType='RO', sBits='10:8', sDefault='0x0')
        self.assertEqual(oField.iWidth, 3)

    def test_field_default(self):
        oField = register.field(sType='RW', sBits='15:0', sDefault='0xF')
        self.assertEqual(oField.sDefault,'0xF')

    def test_register_exists(self):
        oRegister = register.register(sName='Reg1', iWidth=10, sUniqueId='UID_1')
        self.assertEqual(oRegister.sName,'Reg1')

    def test_register_unique_id(self):
        oRegister = register.register(sName='Reg1', iWidth=10, sUniqueId='UID_1')
        self.assertEqual(oRegister.sUniqueId, 'UID_1')

    def test_register_width(self):
        oRegister = register.register(sName='Reg1', iWidth=32, sUniqueId='UID_1')
        self.assertEqual(oRegister.iWidth,32)

    def test_register_description(self):
        oRegister = register.register(sName='Reg1', iWidth=32, sUniqueId='UID_1')
        oRegister.add_description('This is a reg description')
        self.assertEqual(oRegister.lDescription,['This is a reg description'])
        
    def test_register_with_one_field(self):
        oRegister = register.register(sName='Reg1', iWidth=32, sUniqueId='UID_1')
        oRegister.add_description('This is a reg description')
        oField = register.field(sType='RW', sBits='15:0', sDefault='0xF')
        oRegister.add_field(oField)
        self.assertEqual(oRegister.lFields[0].sType,'RW')

    def test_register_with_three_fields(self):
        oRegister = register.register(sName='Reg1', iWidth=32, sUniqueId='UID_1')
        oRegister.add_description('This is a reg description')
        oField = register.field(sType='RW', sBits='15:0', sDefault='0xFFFF')
        oRegister.add_field(oField)
        oField = register.field(sType='RO', sBits='20:16', sDefault='0xF')
        oRegister.add_field(oField)
        oField = register.field(sType='RW', sBits='31:21', sDefault='0xFFF')
        oRegister.add_field(oField)
        self.assertEqual(oRegister.lFields[0].sBits,'15:0')
        self.assertEqual(oRegister.lFields[1].sBits,'20:16')
        self.assertEqual(oRegister.lFields[2].sBits,'31:21')

    def test_register_map_entry(self):
        oRegister = register.register(sName='Register 1', iWidth=32, sUniqueId='UID_1')
        oMapEntry = register.map_entry('0x1', 'Register 1a', oRegister)
        self.assertEqual(oMapEntry.sAddress,'0x1')
        self.assertEqual(oMapEntry.sName,'Register 1a')
        self.assertEqual(oMapEntry.oObject.sName,'Register 1')

    def test_register_map_exists(self):
        oMap = register.map(sName='blah')

    def test_register_map_with_one_register(self):
        oMap = register.map(sName='blah')
        oRegister = register.register(sName='Register 1', iWidth=32, sUniqueId='UID_1')
        oMap.add_entry(sAddress='0x1', sName='Register 1a', oObject=oRegister)
        self.assertEqual(oMap.lObjects[0].sName, 'Register 1a')
        self.assertEqual(oMap.lObjects[0].oObject.sName, 'Register 1')
        
    def test_register_map_with_map(self):
        oSubMap = register.map(sName='Sub Map Name')
        oRegister = register.register(sName='Register 1', iWidth=32, sUniqueId='UID_1')
        oSubMap.add_entry(sAddress='0x1', sName='Register 1a', oObject=oRegister)
        oMap = register.map(sName='top map')
        oMap.add_entry('0x0', 'Sub Map', oSubMap)
        self.assertEqual(oMap.lObjects[0].sName, 'Sub Map')
        self.assertEqual(oMap.lObjects[0].oObject.sName, 'Sub Map Name')
        self.assertEqual(oMap.lObjects[0].oObject.lObjects[0].sName, 'Register 1a')
        self.assertEqual(oMap.lObjects[0].oObject.lObjects[0].oObject.sName, 'Register 1')

if __name__ == '__main__':
    unittest.main()
