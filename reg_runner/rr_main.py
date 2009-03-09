#!/usr/bin/env python

import wx
import generated

class RegRunner(generated.rr_MainFrame):
    def __init__(self, *args, **kwds):
        generated.rr_MainFrame.__init__(self, *args, **kwds)

    def handle_disabletests(self, event): # wxGlade: rr_MainFrame.<event_handler>
        event.Skip()

    def handle_enabletests(self, event): # wxGlade: rr_MainFrame.<event_handler>
        event.Skip()

    def handle_execute(self, event): # wxGlade: rr_MainFrame.<event_handler>
        event.Skip()

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
