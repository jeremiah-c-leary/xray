


import html

def build_head():

  # Generate head
  oHeadTag = html.head()

  oTag = html.meta()
  oTag.add_meta_item('charset="utf-8"')
  oHeadTag.add_tag(oTag)

  oTag = html.meta()
  oTag.add_meta_item('name="viewport"')
  oTag.add_meta_item('content="width-device-width, initial-scale=1"')
  oHeadTag.add_tag(oTag)

  oTag = html.link()
  oTag.rel = 'stylesheet'
  oTag.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
  oHeadTag.add_tag(oTag)

  oTag = html.script('https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
  oHeadTag.add_tag(oTag)

  oTag = html.script('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')
  oHeadTag.add_tag(oTag)

  return oHeadTag

def build_drop_menu(sName,lMenuItems):

  oLi = html.li()

  oA = html.a(sName)
  oA.add_class('dropdown-toggle')
  oA.href = '#'
  oA.dataToggle = 'dropdown'

  oLi.add_tag(oA)

  oUl = html.ul()
  oUl.add_class('dropdown-menu')

  for oMenuItem in lMenuItems:
    oUl.add_tag(oMenuItem)

  oLi.add_tag(oUl)

  return oLi



def build_navbar(sBrandLink,sBrand,lMenuItems):

  oNavTag = html.nav()
  oNavTag.add_class('navbar')
  oNavTag.add_class('navbar-inverse')
#  oNavTag.add_class('navbar-fixed-top')

  oDiv = html.div()
  oDiv.add_class('container-fluid')
  
  oTag = html.div()
  oTag.add_class('navbar-header')

  oA = html.a(sBrand)
  oA.add_class('navbar-brand')
  oA.href = sBrandLink

  oTag.add_tag(oA)
  oDiv.add_tag(oTag)

  oUl = html.ul()
  oUl.add_class('nav')
  oUl.add_class('navbar-nav')

  for oMenuItem in lMenuItems:
    oUl.add_tag(oMenuItem)

  oDiv.add_tag(oUl)
  oNavTag.add_tag(oDiv)

  return oNavTag

def menu_item(sHref,sName):

  oLi = html.li()
  oA = html.a(sName)
  oA.href = sHref
  oLi.add_tag(oA)

  return oLi

def main():


  # Generate navbar
  oFPGA_one = menu_item('fpga_one.html','One')
  oFPGA_two = menu_item('fpga_two.html','Two')
  oFPGA_three = menu_item('fpga_three.html','Three')
  oFPGAMenu = build_drop_menu('FPGA',[oFPGA_one,oFPGA_two,oFPGA_three])
  oBlockMenu = menu_item('#blocks','Block')
  oInterface_external = menu_item('#interfaces-external','External')
  oInterface_internal = menu_item('#interfaces-internal','Internal')
  oInterfaceMenu = build_drop_menu('Interfaces',[oInterface_external,oInterface_internal])
  oNavBar = build_navbar('system.html','Project A',[oFPGAMenu,oBlockMenu,oInterfaceMenu])

  # Create system body
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  oParagraph=html.p('This is the system page')
  oBody.add_tag(oParagraph)

  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('system.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()

  # Create FPGA one page
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  oParagraph=html.p('This is FPGA one')
  oBody.add_tag(oParagraph)

  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('fpga_one.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()

  # Create FPGA two page
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  oParagraph=html.p('This is FPGA two')
  oBody.add_tag(oParagraph)

  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('fpga_two.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()

  # Create FPGA three page
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  oParagraph=html.p('This is FPGA three')
  oBody.add_tag(oParagraph)

  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('fpga_three.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()


  print oHeadTag.create()


if __name__ == '__main__':
    main()


