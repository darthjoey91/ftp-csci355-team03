#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Thu Mar 19 16:33:14 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
import os
from ftp import login,quit,getFile,upFile,listFiles,GetCurrentDir,SetCurrentDir,deleteFile,deleteDir,CreateNewDir

class MyFrame(wx.Frame):
    address = ''
    user = ''
    pwd = ''
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Host Address:"))
        self.txtHostAddress = wx.TextCtrl(self, wx.ID_ANY, "")
        self.btnConnect = wx.Button(self, wx.ID_ANY, _("Connect..."))
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Current Path:"))
        self.txtPath = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.listboxFiles = wx.ListBox(self, wx.ID_ANY, choices=[])
        self.btnUpload = wx.Button(self, wx.ID_ANY, _("Upload File..."))
        self.btnDownload = wx.Button(self, wx.ID_ANY, _("Download File..."))
        self.static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        self.btnOpenDir = wx.Button(self, wx.ID_ANY, _("Open Folder"))
        self.btnNewDir = wx.Button(self, wx.ID_ANY, _("New Folder..."))
        self.btnDelDir = wx.Button(self, wx.ID_ANY, _("Delete Folder"))
        self.static_line_3 = wx.StaticLine(self, wx.ID_ANY)
        self.btnProperties = wx.Button(self, wx.ID_ANY, _("Properties..."))
        self.gauge_1 = wx.Gauge(self, wx.ID_ANY, 10)

        self.__set_properties()
        self.__do_layout()

        # self.Bind(wx.EVT_TEXT, self.txtHostAddress_Changed, self.txtHostAddress)
        self.Bind(wx.EVT_BUTTON, self.btnConnect_Click, self.btnConnect)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.listboxFiles_DoubleClick, self.listboxFiles)
        # self.Bind(wx.EVT_LISTBOX, self.listboxFiles_Click, self.listboxFiles)
        self.Bind(wx.EVT_BUTTON, self.btnUpload_Click, self.btnUpload)
        self.Bind(wx.EVT_BUTTON, self.btnDownload_Click, self.btnDownload)
        self.Bind(wx.EVT_BUTTON, self.btnOpenDir_Click, self.btnOpenDir)
        self.Bind(wx.EVT_BUTTON, self.btnNewDir_Click, self.btnNewDir)
        self.Bind(wx.EVT_BUTTON, self.btnDelDir_Click, self.btnDelDir)
        self.Bind(wx.EVT_BUTTON, self.btnProperties_Click, self.btnProperties)
        # end wxGlade

        login()
        self.showFiles()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("FTP Client"))
        self.SetSize((600, 300))
        self.label_3.SetMinSize((100, 17))
        self.txtHostAddress.SetMinSize((400, 27))
        self.btnConnect.SetMinSize((100, 29))
        self.static_line_1.SetMinSize((600, 5))
        self.label_1.SetMinSize((100, 17))
        self.txtPath.SetMinSize((350, 27))
        self.listboxFiles.SetMinSize((450, 218))
        self.btnUpload.SetMinSize((150, 29))
        self.btnDownload.SetMinSize((150, 30))
        self.static_line_2.SetMinSize((148, 5))
        self.btnOpenDir.SetMinSize((150, 29))
        self.btnNewDir.SetMinSize((150, 29))
        self.btnDelDir.SetMinSize((150, 29))
        self.static_line_3.SetMinSize((148, 5))
        self.btnProperties.SetMinSize((150, 29))
        self.gauge_1.SetMinSize((600, 15))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.txtHostAddress, 0, 0, 0)
        sizer_2.Add(self.btnConnect, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND | wx.SHAPED, 0)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_8.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.txtPath, 0, 0, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_7.Add(self.listboxFiles, 0, 0, 0)
        sizer_6.Add(sizer_7, 3, wx.EXPAND, 0)
        sizer_9.Add(self.btnUpload, 0, 0, 0)
        sizer_9.Add(self.btnDownload, 0, 0, 0)
        sizer_9.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_9.Add(self.btnOpenDir, 0, 0, 0)
        sizer_9.Add(self.btnNewDir, 0, 0, 0)
        sizer_9.Add(self.btnDelDir, 0, 0, 0)
        sizer_9.Add(self.static_line_3, 0, wx.EXPAND, 0)
        sizer_9.Add(self.btnProperties, 0, 0, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 8, wx.EXPAND, 0)
        sizer_1.Add(self.gauge_1, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    # def txtHostAddress_Changed(self, event):  # wxGlade: MyFrame.<event_handler>
    #     print "Event handler 'txtHostAddress_Changed' not implemented!"
    #     event.Skip()

    def btnConnect_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        event.Skip()
        # address = self.txtHostAddress.GetLineText(0)
        # print address

        # if address == '':
        #     wx.MessageBox('Please enter address first')
        #     return

        # user = wx.TextEntryDialog(None,'Enter username','Login','')
        # if user.ShowModal() == wx.ID_OK:
        #     user = user.GetValue()
        #     pwd = wx.TextEntryDialog(None,'Enter password','Login','')
        #     if pwd.ShowModal() == wx.ID_OK:
        #         pwd = pwd.GetValue()
        #     if not pwd or not user:
        #         wx.MessageBox('username/password cannot be blank')
        #         return
        # if login(address, user, pwd) == False:
        #     wx.MessageBox('Check login credentials')
        #     return
        # else:
        #     wx.MessageBox('Login Successful')
        #     self.showFiles()

    def listboxFiles_DoubleClick(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Entered view dir"

        if self.listboxFiles.GetStringSelection() == '<--':
            SetCurrentDir('..')
        else:
            currDir = GetCurrentDir()
            # print currDir
            SetCurrentDir(self.listboxFiles.GetStringSelection())
            # print self.listboxFiles.GetStringSelection()
        
        # GetCurrentDir()

        self.listboxFiles.Clear()

        font = wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)

        self.listboxFiles.SetItemFont(1,font)

        if GetCurrentDir() != '/':
            self.listboxFiles.Append('<--')
            self.listboxFiles.SetItemFont(0,font)
        else:
            self.listboxFiles.Delete(0)

        self.showFiles()

    # def listboxFiles_Click(self, event):  # wxGlade: MyFrame.<event_handler>
    #     print "Event handler 'listboxFiles_Click' not implemented!"
    #     event.Skip()

    def btnUpload_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        filename = ''
        dlg = wx.FileDialog(self, message="Choose a file")
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        if not filename:
           return
        upFile(filename)
        self.listboxFiles.Clear()
        self.showFiles()
        # event.Skip()

    def btnDownload_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        filename = self.listboxFiles.GetStringSelection()

        msg = "Save " + filename + " file"

        save_dlg = wx.FileDialog(self, msg,"",filename,"",wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if save_dlg.ShowModal() == wx.ID_CANCEL:
            return

        path = save_dlg.GetPath()

        print path

        getFile(path)

    def btnOpenDir_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        self.listboxFiles_DoubleClick(event)

    def btnNewDir_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(GetCurrentDir())

        dir_name = wx.TextEntryDialog(None,'Enter directory name','Name','')

        if dir_name.ShowModal() == wx.ID_CANCEL:
            return

        CreateNewDir(dir_name.GetValue())

        self.listboxFiles.Clear()
        self.showFiles()

    def btnDelDir_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'btnDelDir_Click' not implemented!"
        event.Skip()

    def btnProperties_Click(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'btnProperties_Click' not implemented!"
	dlg = MyDialog(self)
	if dlg.ShowModal() == wx.ID_OK:
		print "TODO: Assign Properties"
	dlg.Destroy()
        event.Skip()

    def showFiles(self):
        data = listFiles()

        for x in data:
            self.listboxFiles.Append(x)

# end of class MyFrame

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.chkOwnRead = wx.CheckBox(self, wx.ID_ANY, _("Read"))
        self.chkOwnWrite = wx.CheckBox(self, wx.ID_ANY, _("Write"))
        self.chkOwnExe = wx.CheckBox(self, wx.ID_ANY, _("Execute"))
        self.sizer_16_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Owner Permissions"))
        self.chkGrpRead = wx.CheckBox(self, wx.ID_ANY, _("Read"))
        self.chkGrpWrite = wx.CheckBox(self, wx.ID_ANY, _("Write"))
        self.chkGrpExe = wx.CheckBox(self, wx.ID_ANY, _("Execute"))
        self.sizer_17_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Group Permissions"))
        self.chkPubRead = wx.CheckBox(self, wx.ID_ANY, _("Read"))
        self.chkPubWrite = wx.CheckBox(self, wx.ID_ANY, _("Write"))
        self.chkPubExe = wx.CheckBox(self, wx.ID_ANY, _("Execute"))
        self.sizer_18_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Public Permissions"))
        self.btnPropOK = wx.Button(self, wx.ID_ANY, _("OK"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.btnPropOK_Click, self.btnPropOK)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(_("Properties"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_18_staticbox.Lower()
        sizer_18 = wx.StaticBoxSizer(self.sizer_18_staticbox, wx.HORIZONTAL)
        self.sizer_17_staticbox.Lower()
        sizer_17 = wx.StaticBoxSizer(self.sizer_17_staticbox, wx.HORIZONTAL)
        self.sizer_16_staticbox.Lower()
        sizer_16 = wx.StaticBoxSizer(self.sizer_16_staticbox, wx.HORIZONTAL)
        sizer_16.Add(self.chkOwnRead, 0, 0, 0)
        sizer_16.Add(self.chkOwnWrite, 0, 0, 0)
        sizer_16.Add(self.chkOwnExe, 0, 0, 0)
        sizer_15.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_17.Add(self.chkGrpRead, 0, 0, 0)
        sizer_17.Add(self.chkGrpWrite, 0, 0, 0)
        sizer_17.Add(self.chkGrpExe, 0, 0, 0)
        sizer_15.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_18.Add(self.chkPubRead, 0, 0, 0)
        sizer_18.Add(self.chkPubWrite, 0, 0, 0)
        sizer_18.Add(self.chkPubExe, 0, 0, 0)
        sizer_15.Add(sizer_18, 1, wx.EXPAND, 0)
        sizer_15.Add(self.btnPropOK, 0, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_15)
        sizer_15.Fit(self)
        self.Layout()
        # end wxGlade

    def btnPropOK_Click(self, event):  # wxGlade: MyDialog.<event_handler>
        print "Event handler 'btnPropOK_Click' not implemented!"
	self.EndModal(wx.ID_OK)
        event.Skip()

# end of class MyDialog
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    gettext.install("FTP_Client") # replace with the appropriate catalog name

    FTP_Client = MyApp(0)
    FTP_Client.MainLoop()
