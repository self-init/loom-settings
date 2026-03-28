import dearpygui.dearpygui as dpg
from ..base import BaseFrontend

from .components.settings import SettingsComponentView

VIEWS = {
	"settings": SettingsComponentView
}

class DearPyGuiFrontend(BaseFrontend):
	"""Simple Frontend implemented in Dear PyGui"""
	def initialize(self):
		dpg.create_context()
		dpg.setup_dearpygui()

		self.window = dpg.window(label="Example Window",tag="primary")

		with self.window:
			self.tab_bar = dpg.add_tab_bar()

		dpg.create_viewport(title='Custom Title', width=600, height=300)

		dpg.set_primary_window("primary", True)

		dpg.show_viewport()

	def run(self):
		dpg.start_dearpygui()

	def shutdown(self):
		dpg.destroy_context()

	def register_component(self, component):
		if component.id in VIEWS:
			tab = dpg.add_tab(label=component.name, parent=self.tab_bar)
			view = VIEWS[component.id]()
			view.initialize(component, tab)
