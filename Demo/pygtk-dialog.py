#!/usr/bin/env python
 
# example helloworld2.py
 
import pygtk
pygtk.require('2.0')
import gtk

class ConfirmDialog(gtk.Dialog):

    def __init__(self,  message=''):
        #super(ConfirmDialog, self).__init__('', None, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, ())
        #self.label = gtk.Label(message)
        #self.set_position(gtk.WIN_POS_CENTER)
        #self.set_title("Warnning: " + message)
        #self.resize(200,100)
        #self.add_child(self.label)
        #self.label.show()
        #self.add_button('Cancel', gtk.RESPONSE_OK)
        #self.add_button('OK', gtk.RESPONSE_CANCEL)
        super(ConfirmDialog,self).__init__('',None)
        self.btn_OK = gtk.Button("OK")
        self.btn_OK.connect(GTK_SIGNAL_CLICKED, lambda _: self.destroy())
        self.btn_Cancel = gtk.Button("Cancel")
        self.label = gtk.Label('warnning')
        vbox = gtk.VBox(False, 20)
        #vbox.
        vbox.pack_start(self.label)
        vbox.pack_start(self.btn_OK)
        #self.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.add(vbox)

    def run_and_close(self):
        resp_id = self.run()
        print resp_id
        self.destroy()
        return resp_id

class HelloWorld2:
    def callback(self):
        dlg = ConfirmDialog(message = 'aaaaaaaaaaa')
        dlg.run_and_close()

 
    # another callback
    def delete_event(self, widget, event, data=None):
        self.callback()
        gtk.main_quit()
        return False
 
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(320,240)
        self.window.connect("delete_event", self.delete_event)
        self.window.show()
 
def main():
    gtk.main()
 
if __name__ == "__main__":
    hello = HelloWorld2()
    main()
