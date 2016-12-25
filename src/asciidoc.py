
import re
import html


class file():

    def __init__(self):
        self.objects = []

    def process(self, sFilename):
        self.sParagraph = ""
        self.header = ""
        self.tableFlag = False

        with open(sFilename, 'r') as oFile:
            self.lLines = [line.rstrip() for line in oFile]

        for sLine in self.lLines:
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

    def build_html(self):
        lHtml = []
        for oObject in self.objects:
            lHtml.append(oObject.build_html())
        return lHtml


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
