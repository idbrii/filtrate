#!/usr/bin/env python

import wx
import generated

class RegRunner(generated.rr_MainFrame):
    def __init__(self, *args, **kwds):
        generated.rr_MainFrame.__init__(self, *args, **kwds)

        self.__create_content()

    def __create_content(self):
        self.__create_checkboxes('buildtypes.txt')

    def __create_checkboxes(self, filename):
        """
        __addCheckboxes(filename) --> None
        Creates the checkboxes according to filename and adds them to self
        """
        self.checkboxes = []
        for text in ("some reg test", "another test"):
            self.checkboxes.append( wx.CheckBox(self, -1, text) )

    def __add_dynamic_checkboxes(self, sizer):
        print "hi yanna"
        for checkbox in self.checkboxes:
            #sizer.Add(checkbox, 0, 0, 0)
            sizer.Add(checkbox, 1, wx.EXPAND, 0)

# end of class RegRunner


class RRApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = RegRunner(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class RRApp

if __name__ == "__main__":
    RegRunner = RRApp(0)
    RegRunner.MainLoop()
