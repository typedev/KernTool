# -*- coding: utf-8 -*-

import sys
from vanilla import *
from mojo.UI import *
from defconAppKit.windows.baseWindow import BaseWindowController
from AppKit import *
from mojo.extensions import *
import tdKernToolEssentials
reload(tdKernToolEssentials)
from tdKernToolEssentials import *

class KernPreferences(BaseWindowController):
	def __init__(self):

		self.w = FloatingWindow((430, 100), title = 'Kern Preferences')

		ID_KERNING_GROUP = getExtensionDefault(PREFKEY_GroupName, fallback = '@MMK')
		ID_GROUP_DIRECTION_POSITION_LEFT = getExtensionDefault(PREFKEY_LeftID, fallback = '_L_')
		ID_GROUP_DIRECTION_POSITION_RIGHT = getExtensionDefault(PREFKEY_RightID, fallback = '_R_')

		self.w.lblMMKname = TextBox((30,10,130,21),'Group Name ID')
		self.w.editMMKname = EditText((150,10,130,21),text = ID_KERNING_GROUP)
		self.w.lblLeftID = TextBox((30, 40, 100, 21), 'Left ID')
		self.w.editLeftId = EditText((150, 40, 130, 21), text = ID_GROUP_DIRECTION_POSITION_LEFT)
		self.w.lblRightID = TextBox((30, 70, 100, 21), 'Right ID')
		self.w.editRightId = EditText((150, 70, 130, 21), text = ID_GROUP_DIRECTION_POSITION_RIGHT)

		self.w.btnApply = Button((320, 40, -20, 20), "Apply", callback=self.btnApplyCallback)

		self.w.open()

	def btnApplyCallback(self, sender):
		setExtensionDefault(PREFKEY_GroupName, self.w.editMMKname.get())
		setExtensionDefault(PREFKEY_LeftID, self.w.editLeftId.get())
		setExtensionDefault(PREFKEY_RightID, self.w.editRightId.get())
		self.w.close()

KernPreferences()


