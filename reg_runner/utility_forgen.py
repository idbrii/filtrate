import wx

def __create_content(self):
    __create_checkboxes(self, 'buildtypes.txt' )

def __create_checkboxes(self, filename):
    """
    __create_checkboxes(filename) --> None
    Creates the checkboxes according to filename and adds them to self
    """
    self.checkboxes = []
    for text in ("some reg test", "another test"):
        self.checkboxes.append( wx.CheckBox(self, -1, text) )
        pass

def add_dynamic_checkboxes(self, sizer):
    __create_content(self)
    for checkbox in self.checkboxes:
        sizer.Add(checkbox, 0, 0, 0)
