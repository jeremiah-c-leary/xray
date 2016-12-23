
import re

class file():

    def __init__(self):
        self.objects = []

    def process(self, sFilename):
        self.sParagraph = ""
        self.header = ""

        with open (sFilename,'r') as oFile:
            self.lLines = [line.rstrip() for line in oFile]

        for sLine in self.lLines:
            # Search for paragraphs
            if re.search('^$',sLine) and self.sParagraph != "":
                self.objects.append(paragraph(self.sParagraph))
                self.sParagraph = ""
            else:
                if self.sParagraph == "":
                    self.sParagraph += sLine
                else:
                    self.sParagraph += "  " + sLine
            # Search for headers
            if re.search('^=+$',sLine):
                self.objects.append(heading(self.header,1))
                self.sParagraph = ""
            if re.search('^-+$',sLine):
                self.objects.append(heading(self.header,2))
                self.sParagraph = ""
            if re.search('^~+$',sLine):
                self.objects.append(heading(self.header,3))
                self.sParagraph = ""
            if re.search('^\^+$',sLine):
                self.objects.append(heading(self.header,4))
                self.sParagraph = ""
            if re.search('^\++$',sLine):
                self.objects.append(heading(self.header,5))
                self.sParagraph = ""
            self.header = sLine

            



class heading():

    def __init__(self, sTitle, iLevel):
        self.sTitle = sTitle
        self.iLevel = iLevel


class paragraph():
    def __init__(self, sParagraph):
        self.sParagraph = sParagraph

