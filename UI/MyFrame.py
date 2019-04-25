
import wx
import wx.xrc
from UI.ButtonAction import ButtonAction

class MyFrame ( wx.Frame ):

	def __init__( self, parent, title):
		self.s = ButtonAction()
		self.text = []
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 500,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		gSizer18 = wx.GridSizer( 9, 9, 5, 5 )

		for i in range(1,82):
			self.text.append(wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,45 ), 0 ))
			self.text[i-1].SetMaxLength( 1 )
			gSizer18.Add(self.text[i-1])

		bSizer7.Add( gSizer18, 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Answer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcome to play Sudoku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer7.Add( self.m_staticText1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClicked1 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnClicked2 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnClicked3 )

	def OnClicked1(self, event):
		for i in range(len(self.text)):
			self.text[i].Remove(0,1)
		self.s.insert(self.text)

	def OnClicked2(self, event):
		self.s.check(self.text, self.m_staticText1)

	def OnClicked3(self, event):
		self.s.show(self.text)

	def __del__( self ):
		pass


class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(parent = None, title = 'Sudoku')
		self.frame.Show()

		return True

