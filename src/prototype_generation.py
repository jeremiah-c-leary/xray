


import html
import interface
import vhdl

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

  lInternalInterfaces = []
  lExternalInterfaces = []

  # Generate navbar
  oFPGA_one = menu_item('fpga_one.html','One')
  oFPGA_two = menu_item('fpga_two.html','Two')
  oFPGA_three = menu_item('fpga_three.html','Three')
  oFPGAMenu = build_drop_menu('FPGA',[oFPGA_one,oFPGA_two,oFPGA_three])
  oBlockCMenu = menu_item('block_c.html','Block C')
  oBlockMenu = build_drop_menu('Block',[oBlockCMenu])
  oInterface_external = menu_item('external_interfaces.html','External')
  oInterface_internal = menu_item('internal_interfaces.html','Internal')
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

  # Create Interface
  oLedInterface = interface.interface('LED Interface')
  oLedInterface.add_paragraph('The LED Interface allows the block to use the three LEDs attached to the FPGA to indicate status to the user.')
  oLedInterface.add_signal(interface.signal('clk',1,'System clock'))
  oLedInterface.add_signal(interface.signal('green_led','1','Turns on green LED when asserted.'))
  oLedInterface.add_signal(interface.signal('red_led','1','Turns on red LED when asserted.'))
  oProtocol=interface.protocol('Operation Valid Protocol')
  oProtocol.imageLink = 'img/led_interface-operation_valid_protocol.svg'
  oLedInterface.add_protocol(oProtocol)
  oProtocol=interface.protocol('Watchdog Error Protocol')
  oProtocol.imageLink = 'img/led_interface-watchdog_error_protocol.svg'
  oLedInterface.add_protocol(oProtocol)

  lExternalInterfaces.append(oLedInterface)

  oWatchdogMonitorInterface = interface.interface('Watchdog Monitor Interface')
  oWatchdogMonitorInterface.add_paragraph('The Watchdog Monitor Interface is a single discrete that pulses for one clock every 1 us.')
  oWatchdogMonitorInterface.add_signal(interface.signal('clk',1,'System clock'))
  oWatchdogMonitorInterface.add_signal(interface.signal('alive',1,'Indicates the source is still running.'))
  oProtocol=interface.protocol('Watchdog Discrete Protocol')
  oProtocol.imageLink = 'img/watchdog_interface.svg'
  oWatchdogMonitorInterface.add_protocol(oProtocol)

  lInternalInterfaces.append(oWatchdogMonitorInterface)

  oWatchdogUptimeInterface = interface.interface('Watchdog Uptime Interface')
  oWatchdogUptimeInterface.add_paragraph('The Watchdog Uptime Interface reports the number of 1 us counts when the watchdog timer tripped.  This lets the system report uptime statistics')
  oWatchdogUptimeInterface.add_signal(interface.signal('clk',1,'System clock'))
  oWatchdogUptimeInterface.add_signal(interface.signal('watchdog_trip',1,'Pulse indicating the watchdog has tripped.'))
  oWatchdogUptimeInterface.add_signal(interface.signal('uptime_count',16,'Reports the uptime from system startup when the watchdog tripped.'))
  oProtocol=interface.protocol('Uptime Valid Protocol')
  oProtocol.imageLink = 'img/watchdog_uptime_interface-uptime_valid.svg'
  oWatchdogUptimeInterface.add_protocol(oProtocol)

  lInternalInterfaces.append(oWatchdogUptimeInterface)

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


  # Create Block C page
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  oBody.add_tag(html.h2('Overview'))
  oBody.add_tag(html.p('Block C performs the heartbeat function for the system.  This watchdog function is critical to the operation of the system.  Any irregularity in the operation of Block A will be detected and the rest of the system will be notified.'))
  oBody.add_tag(html.h2('Features'))
  oBody.add_tag(html.p('This block has the following features:'))
  oUl = html.ul()
  oUl.add_tag(html.li('Monitors time between Block A pulses'))
  oUl.add_tag(html.li('Flashes LED when Block A fails to pulse at regular intervals'))
  oUl.add_tag(html.li('Sends uptime to Block B indicated violation occured'))
  
  oBody.add_tag(oUl)

  oBody.add_tag(html.h(2,'Interface Diagram'))
  oBody.add_tag(html.img('img/block_interface.svg'))

  oBody.add_tag(html.h(2,'Port Map'))

  oEntity = vhdl.entity('entity1')
  oPortMap = vhdl.port_map()
  oInterface = vhdl.interface('name1')
  oInterface.add_port(vhdl.port('port1','in','std_logic','comment1'))
  oPortMap.add_interface(oInterface)
  oInterface = vhdl.interface('name2')
  oInterface.add_port(vhdl.port('port2','out','std_logic_vector(13 downto 0)','comment2'))
  oPortMap.add_interface(oInterface)

  oEntity.portMap = oPortMap

  oBody.add_tag(oEntity.build_html()[0])

  oBody.add_tag(html.h2('Interfaces'))

  for oInterface in lInternalInterfaces + lExternalInterfaces:
    for oTag in oInterface.build_html():
      oBody.add_tag(oTag)

  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('block_c.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()


  # Create Internal Interfaces 
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  for oInterface in lInternalInterfaces:
    for oTag in oInterface.build_html():
      oBody.add_tag(oTag)
  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('internal_interfaces.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()

  # Create External Interfaces 
  # Generate html
  oHtmlTag = html.html()
  # Generate head
  oHeadTag = build_head()
  oHtmlTag.add_tag(oHeadTag)
  oBody = html.body()
  oBody.add_tag(oNavBar)
  for oInterface in lExternalInterfaces:
    for oTag in oInterface.build_html():
      oBody.add_tag(oTag)
  oHtmlTag.add_tag(oBody)

  # Write System level HTML to file
  fHtml = open ('external_interfaces.html','w')
  fHtml.writelines(oHtmlTag.create())
  fHtml.close()


if __name__ == '__main__':
    main()


