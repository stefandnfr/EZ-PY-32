import drivers.ili9486py as display

refresh = [450,250,20,20]
back = [450,290,20,20]

def getMainSelectors():
	return [[160,100,160,30],[160,160,160,30],[160,220,160,30],[160,280,160,30]]

def getNetworkSelectors():
	return [refresh,back]

def getServerSelectors():
	return [refresh,back]

def getTextSelectors():
	return [refresh,back]

def getLogoSelectors():
	return [refresh,back]




def drawText(args):
	size1_longstring = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. But what happens if the displayed text is actually longer than expected? will there be an answer? Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quisque non tellus orci ac auctor. Ut consequat semper viverra nam libero justo. Risus in hendrerit gravida rutrum quisque non tellus orci. Est ultricies integer quis auctor elit sed vulputate mi. Gravida rutrum quisque non tellus orci ac. Habitasse platea dictumst quisque sagittis purus. Dictum varius duis at consectetur lorem donec. Adipiscing at in tellus integer feugiat scelerisque varius. Integer feugiat scelerisque varius morbi enim. Morbi tincidunt augue interdum velit euismod in. Auctor augue mauris augue neque gravida in. Ut lectus arcu bibendum at varius vel pharetra vel. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Vel orci porta non pulvinar neque laoreet suspendisse interdum. In fermentum et sollicitudin ac orci. Porttitor rhoncus dolor purus non enim praesent elementum facilisis. Commodo ullamcorper a lacus vestibulum. Pulvinar elementum integer enim neque volutpat. Amet risus nullam eget felis eget nunc lobortis. Adipiscing elit pellentesque habitant morbi tristique senectus et. Tristique magna sit amet purus. Malesuada nunc vel risus commodo viverra maecenas accumsan lacus vel. Metus dictum at tempor commodo ullamcorper a lacus vestibulum. Cras fermentum odio eu feugiat pretium nibh ipsum consequat. Velit aliquet sagittis id consectetur purus. Semper feugiat nibh sed pulvinar proin. Tortor consequat id porta nibh venenatis cras. Massa enim nec dui nunc mattis enim ut tellus. Velit ut tortor pretium viverra. Pellentesque elit eget gravida cum sociis natoque penatibus. Nam aliquam sem et tortor consequat id porta. Id diam vel quam elementum pulvinar etiam. Nisl purus in mollis nunc sed id semper risus in. In fermentum et sollicitudin ac orci phasellus. Now this time we are trying it againg: what happens if the displayed Text at size 1 is longer than expected? Will it still print?'
	display.Draw_Info_Box_Text(x=20,y=20,w=400,h=280,size = 2,heading="Static text",body=size1_longstring)
	display.Draw_Char(450,250,0x3,0x0,3)
	display.Draw_Char(450,290,0x0,0x0,3)

def drawMain(args):
	display.Draw_Info_Box_Text(x=130,y=20,w=225,h=50,size = 2, heading="EZ-PY32",body="")
	display.Draw_Info_Box_Text(x=160,y=100,w=160,h=30,heading="text",body="")
	display.Draw_Info_Box_Text(x=160,y=160,w=160,h=30,heading="networks",body="")
	display.Draw_Info_Box_Text(x=160,y=220,w=160,h=30,heading="logo",body="")
	display.Draw_Info_Box_Text(x=160,y=280,w=160,h=30,heading="server",body="")

MAGENTA=const(0xF81F)

def drawNetwork(args):
	wlannetworks = args[0]
	display.Draw_Info_Box_List(x=20,y=20,w=250,h=280,size = 2, heading="Networks",body=wlannetworks)
	display.Draw_Char(450,250,0x3,0x0,3)
	display.Draw_Char(450,290,0x0,0x0,3)


def drawLogo(args):
	display.printBild()
	display.Draw_Char(450,250,0x3,0x0,3)
	display.Draw_Char(450,290,0x0,0x0,3)


def drawServer(args):

	serverdata = args[0]
	display.Draw_Info_Box_Text(x=20,y=20,w=400,h=280,size = 2,heading="Server data",body=serverdata)
	display.Draw_Char(450,250,0x3,0x0,3)
	display.Draw_Char(450,290,0x0,0x0,3)