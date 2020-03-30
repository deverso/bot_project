from Tkinter import Tk, Label, Button
import time, threading
from pynput.keyboard import Key, Controller

class BotProject:
  DANCE_INTERVAL = 300
  Keyboard = None

  def __init__(self, master):
    self.master = master
    self.mount_window(master)
    self.Keyboard = Controller()

  def mount_window(self, master):
    master.title("Bot Project")
    self.label = Label(master, text="Choose an action:")
    self.label.pack()

    self.btn_start_dance = Button(master, text="Start dance", command=self.start_dance)
    self.btn_start_dance.pack()

    # TODO
    # self.btn_stop_dance = Button(master, text="Stop dance", command=self.stop_dance)
    # self.btn_stop_dance.pack()

    self.close_button = Button(master, text="Close", command=master.quit)
    self.close_button.pack()

  def dance(self):
    self.Keyboard.press(Key.ctrl)
    self.Keyboard.press(Key.left)
    self.Keyboard.release(Key.left)
    self.Keyboard.press(Key.right)
    self.Keyboard.release(Key.right)
    self.Keyboard.press(Key.up)
    self.Keyboard.release(Key.up)
    self.Keyboard.press(Key.down)
    self.Keyboard.release(Key.down)
    time.sleep(self.DANCE_INTERVAL)
    self.dance()

  def start_dance(self):
      self.dance()
      print('Started dancing')
      # self.T = threading.Timer(self.DANCE_INTERVAL, self.dance).start()

  # TODO
  # def stop_dance(self):
  #   if self.T.ident() != None:
  #     self.T.cancel()
  #     print('Stopped dancing')

root = Tk()
bot = BotProject(root)
root.mainloop()