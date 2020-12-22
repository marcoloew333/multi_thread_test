import wx
import os
import pigpio
from time import sleep
import threading

import variables as var
from background import bla
from timer import duration_timer
from stop_motor_if_running import stop_motor_if_running

# app = wx.App()
# frame = wx.Frame(None, wx.ID_ANY, 'Hello World')
# frame.Show()
# app.MainLoop()

# check if ...
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

pi = pigpio.pi()

if not pi:
    print('pigpio deamon not running...')


# def motor():
#     while var.counter < 5:
#         pi.write(17, 0)
#         sleep(1)
#         pi.write(17, 1)
#         sleep(1)


def stop(event):
    print('stop initiated...')


def pause(event):
    print('pause initiated...')


# CLASS BASED
def pause_motor():
    print('motor paused')
    stop_motor_if_running()


# class MotorControl(threading.Thread):
#     """
#     Class to do the following: Start motor
#     """
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         print('started')
#         start_timer = threading.Thread(target=duration_timer(10), name='timer')
#         start_timer.daemon = True
#         start_bla = threading.Thread(target=bla(), name='bla')
#         start_bla.daemon = True
#         start_mot = threading.Thread(target=motor('event'), name='motor')
#
#         start_timer.start()
#         start_bla.start()
#         start_mot.start()
#         print('ended')


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.b_test = wx.Button(self.panel, wx.ID_ANY, 'STOP', pos=(6, 6))
        self.c_test = wx.Button(self.panel, wx.ID_ANY, 'Start', pos=(100, 6))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        self.Bind(wx.EVT_BUTTON, self.asdf, self.c_test)
        self.b_state = wx.Button(self.panel, wx.ID_ANY, 'Disable', pos=(6, 40))
        self.Bind(wx.EVT_BUTTON, self.on_state, self.b_state)
        self.cb_discount = wx.CheckBox(self.panel, wx.ID_ANY, 'Discount', pos=(100, 44))
        self.cb_radio_button = wx.RadioButton(self.panel, wx.ID_ANY, 'Radio', pos=(200, 40))
        self.cb_radio_box = wx.RadioBox(self.panel, wx.ID_ANY, 'Radio', pos=(300, 40), choices=['1', '2', '3'])
        self.tc_test = wx.TextCtrl(self.panel, wx.ID_ANY, '', pos=(6, 80), size=(80, -1))

        self.tc_ctr = wx.TextCtrl(self.panel, wx.ID_ANY, "1", (100, 80), (35, -1))
        spin_height = self.tc_ctr.GetSize().height
        spin_position = self.tc_ctr.GetPosition().x + self.tc_ctr.GetSize().width + 2
        self.sb_ctr = wx.SpinButton(self.panel, wx.ID_ANY, (spin_position, int(80-spin_height)), (spin_height*2, spin_height*3), wx.SP_VERTICAL)
        self.sb_ctr.SetRange(1, 100)
        self.sb_ctr.SetValue(1)
        self.Bind(wx.EVT_SPIN, self.on_spin, self.sb_ctr)
        self.Bind(wx.EVT_SPIN, self.on_spin, self.sb_ctr)

        wx.StaticText(self.panel, wx.ID_ANY, 'static text', pos=(6, 160))

    def motor(self, event):
        while var.counter < 5:
            pi.write(17, 0)
            sleep(1)
            pi.write(17, 1)
            sleep(1)

    def counter(self, event):
        bla()

    def asdf(self):
        self.motor('event')
        # self.counter('event')

    def on_test(self, event):
        print('Button Pressed')
        print('Radio Box Selection:', self.cb_radio_box.GetStringSelection())
        print('Radio Button enabled?', self.cb_radio_button.GetValue())
        print('Checkbox enabled?', self.cb_discount.IsChecked())
        # event.Skip()

    def on_spin(self, event):
        self.tc_ctr.SetValue(str(event.GetPosition()))

    def on_state(self, event):
        if self.b_state.GetLabel() == 'Disable':
            self.b_test.Disable()
            self.b_state.SetLabel('Enable')
        else:
            self.b_test.Enable()
            self.b_state.SetLabel('Disable')


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, title='wxPython Test')
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == '__main__':
    print('main')
    app = MyApp()
    app.MainLoop()
