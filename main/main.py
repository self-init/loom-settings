from frontends.dearpygui.frontend import DearPyGuiFrontend
from components import SettingsComponent

class App:
	def __init__(self, frontend):
		pass

	def run(self):
		dpgfrontend = DearPyGuiFrontend()
		dpgfrontend.initialize()
		sc = SettingsComponent()
		sc.initialize()
		dpgfrontend.register_component(sc)
		dpgfrontend.run()

App("").run()
