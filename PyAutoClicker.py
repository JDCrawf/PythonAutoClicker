from time import sleep
import threading
from pynput.mouse    import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 10 # in seconds
max_delay = 10
min_delay = 1
button = Button.left
start_stop_key  = KeyCode(char='o')
exit_key        = KeyCode(char='p')
speed_up_key    = KeyCode(char='+')
slow_down_key   = KeyCode(char='-')

class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super(ClickMouse, self).__init__()
		self.delay       = delay
		self.button      = button
		self.running     = False
		self.program_run = True

	def start_clicking(self):
		self.running = True

	def stop_clicking(self):
		self.running = False

	def exit(self):
		self.stop_clicking()
		self.program_run = False

	def run(self):
		while self.program_run:
			while self.running:
				mouse.click(self.button)
				#print("click")
				sleep(self.delay)
			sleep(1)

mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()

def on_press(key):
	if key == start_stop_key:
		if thread.running:
			thread.stop_clicking()
		else:
			thread.start_clicking()
	elif key == speed_up_key:
		thread.delay = max(thread.delay - 1, min_delay)
		#print("delay: " + str(thread.delay))
	elif key == slow_down_key:
		thread.delay = min(thread.delay + 1, max_delay)
		#print("delay: " + str(thread.delay))
	elif key == exit_key:
		thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
	listener.join()