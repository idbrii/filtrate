#!/usr/bin/env python

import wx
import generated

outputfile = 'out_tests_to_run.txt'

class RegRunner(generated.rr_MainFrame):
    def __init__(self, *args, **kwds):
        generated.rr_MainFrame.__init__(self, *args, **kwds)

    def __force_all_tests(self, value):
        for checkbox in self.checkboxes.values():
            checkbox.SetValue(value)

    def handle_disabletests(self, event): # wxGlade: rr_MainFrame.<event_handler>
        self.__force_all_tests(False)
        event.Skip()

    def handle_enabletests(self, event): # wxGlade: rr_MainFrame.<event_handler>
        self.__force_all_tests(True)
        event.Skip()

    def handle_execute(self, event): # wxGlade: rr_MainFrame.<event_handler>
        out = open(outputfile, 'w')
        for key in self.checkboxes.keys():
            if self.checkboxes[key].GetValue():
                out.write(key)
        out.close()

        ## TODO: run the regression test suite here
        ## popen(something or other)
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
