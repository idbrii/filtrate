import wx

test_list_file = 'sampletestlist.txt'

def __create_content(self):
    __create_checkboxes(self, test_list_file)

def __create_checkboxes(self, filename):
    """
    __create_checkboxes(filename) --> None
    Creates the checkboxes according to filename and adds them to self
    """
    self.checkboxes = {}
    for text in open(filename):
        self.checkboxes[text] = ( wx.CheckBox(self, -1, text) )
        pass

def add_dynamic_checkboxes(self, sizer):
    __create_content(self)
    for checkbox in self.checkboxes.values():
        sizer.Add(checkbox, 0, 0, 0)
