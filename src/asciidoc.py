
import re
import html
import register

def create_list(lList):
    '''Returns an empty list if one does not exist, otherwise it just returns the list it was given.'''
    if not lList:
        lList = []
    return lList

def extract_table_columns(sRow):
    '''Returns a list of row elements.'''
    lRow = []
    for sColumn in sRow.split('|')[1:]:
        lRow.append(sColumn.rstrip().lstrip())
    return lRow

def extract_options(sOptions):
    '''returns a dictionary with all options between braces.'''
    if sOptions == '[]':
        dOptions = None
    else:
        dOptions = {}
        lOptions = re.search('\[(.*)\]', sOptions).group(1).split(',')
        for sOption in lOptions:
            lScratch = sOption.split('=')
            dOptions[lScratch[0].rstrip().lstrip()] = lScratch[1].lstrip().rstrip().replace("\"", '')
    return dOptions

def extract_memory_map(lLines):
    '''Returns a memory map object given a list of strings and a list of register objects.'''
    oMemoryMap = None
    if lLines:
        dOptions = extract_options(lLines[0])
        oMemoryMap = register.map(dOptions['name'])
        # Find the starting index of the tables
        iIndex = 1
        for sLine in lLines[1:]:
            if re.search('^\|=+$', sLine):
                iIndex += 2
                break
            iIndex += 1
        # Parse the rows
        for sLine in lLines[iIndex:-1]:
            lOptions = extract_table_columns(sLine)
            oMemoryMap.add_entry(lOptions[0], lOptions[1], register.register(None, None, lOptions[2]))
    return oMemoryMap

class file():

    def __init__(self, sFileName):
        self.objects = []
        self.sFileName = sFileName
        self.oMemoryMap = None
        if self.sFileName:
          self.process(sFileName)


    def process(self, sFilename):
        self.sParagraph = ""
        self.header = ""
        self.tableFlag = False
        memoryMapFlag = False
        memoryMapTableFound = False
        lMemoryMap = None
        lRegisters = None
        registerFlag = False
        registerTableFound = False

        with open(sFilename, 'r') as oFile:
            self.lLines = [line.rstrip() for line in oFile]

        for sLine in self.lLines:
            # Search for memory map tables
            if memoryMapFlag:
                lScratch.append(sLine)
                if re.search('^\|=+$', sLine):
                    if memoryMapTableFound:
                        memoryMapFlag = False
                        self.oMemoryMap = extract_memory_map(lScratch)
                        self.objects.append(self.oMemoryMap)
                    memoryMapTableFound = not memoryMapTableFound
                continue

            # Search for memory maps
            if re.search('^memory_map:.*\[.*\]', sLine):
                memoryMapFlag = True
                lScratch = [sLine]
                continue

            # collect register definition
            if registerFlag:
                lScratch.append(sLine)
                if re.search('^\|=+$', sLine):
                    if registerTableFound:
                        registerFlag = False
                        oRegister = self.extract_register(lScratch)
                        lRegisters.append(oRegister)
                        self.objects.append(oRegister)
                    registerTableFound = not registerTableFound
                continue

            # Search for registers
            if re.search('^register:.*\[.*\]', sLine):
                registerFlag = True
                lScratch = [sLine]
                lRegisters = create_list(lRegisters)
                continue

            # Search for tables
            if self.tableFlag:
                # Search for end of table
                if re.search('^\|=+$', sLine) and self.tableFlag:
                    self.objects.append(oTable)
                    self.tableFlag = False
                    continue

                # Split table rows and add them to the Table
                oTable.add_row(map(str.strip, re.split('\|', sLine)[1:]))

                continue

            # Search for beginning of table
            if re.search('^\|=+$', sLine) and not self.tableFlag:
                oTable = table()
                self.tableFlag = True
                continue

            # Search for block images
            if re.search('^image::.*\[\]$', sLine) and self.sParagraph == "":
                self.sImagePath = re.split('[::|\[\]]', sLine)[2]
                self.objects.append(block_image(self.sImagePath))
                self.sParagraph = ""
                continue

            # Search for paragraphs
            if re.search('^$', sLine) and self.sParagraph != "":
                self.objects.append(paragraph(self.sParagraph))
                self.sParagraph = ""
                continue
            else:
                if self.sParagraph == "":
                    self.sParagraph += sLine
                else:
                    self.sParagraph += "  " + sLine
            # Search for headers
            if re.search('^=+$', sLine):
                self.objects.append(heading(self.header, 1))
                self.sParagraph = ""
            if re.search('^-+$', sLine):
                self.objects.append(heading(self.header, 2))
                self.sParagraph = ""
            if re.search('^~+$', sLine):
                self.objects.append(heading(self.header, 3))
                self.sParagraph = ""
            if re.search('^\^+$', sLine):
                self.objects.append(heading(self.header, 4))
                self.sParagraph = ""
            if re.search('^\++$', sLine):
                self.objects.append(heading(self.header, 5))
                self.sParagraph = ""
            self.header = sLine
            # Stop collecting paragraphs when a blank line is found
            if re.search('^$', sLine):
                self.sParagraph = ""
#        self.oMemoryMap = self.update_memory_map(lMemoryMap, lRegisters)
#        if self.oMemoryMap:
#            self.objects.append(self.oMemoryMap)

    def build_html(self):
        lHtml = []
        for oObject in self.objects:
            lHtml.append(oObject.build_html())
        return lHtml

    def extract_register(self, lLines):
        '''Returns a register object from a list of strings.'''

        tableFoundFlag = False

        dOptions = extract_options(lLines[0])
        sUniqueId = re.search(':(.*)\[', lLines[0]).group(1)
        oRegister = register.register(dOptions['name'],dOptions['width'], sUniqueId)
        lDescription = []

        for sLine in lLines[1:-1]:
            if not tableFoundFlag:
                lDescription.append(sLine)

            if tableFoundFlag:
                # Skip the header
                if 'Bits' in sLine and 'Description' in sLine:
                    continue
                # Process the field
                oRegister.add_field(self.extract_field(sLine))

            if re.search('^\|=+$', sLine):
                tableFoundFlag = True
            
        return oRegister

    def extract_field(self, sLine):
        '''Returns a field object from the given string.'''
        lOptions = extract_table_columns(sLine)
        return register.field(lOptions[0],lOptions[1],lOptions[2])




class heading():

    def __init__(self, sTitle, iLevel):
        self.sTitle = sTitle
        self.iLevel = iLevel

    def build_html(self):
        return html.h(self.iLevel, self.sTitle)


class paragraph():

    def __init__(self, sParagraph):
        self.sParagraph = sParagraph

    def build_html(self):
        return html.p(self.sParagraph)


class block_image():

    def __init__(self, sImagePath):
        self.sImagePath = sImagePath

    def build_html(self):
        return html.img(self.sImagePath)


class table():

    def __init__(self):
        self.lRows = []

    def add_row(self, lRow):
        self.lRows.append(lRow)

    def build_html(self):
        oTable = html.table()
        for lRow in self.lRows:
            oTr = html.tr()
            for sColumn in lRow:
                oTr.add_tag(html.td(sColumn))
            oTable.add_tag(oTr)
        return oTable
