from .discovery import scan_for_components
from ..components import SettingsComponent

INTERNAL_COMPONENTS = {
	"settings": SettingsComponent,
}

class AppCore:
	def __init__(self, frontend):
		self.frontend = frontend()
		self.components = {}

	def start(self):
		self.components = INTERNAL_COMPONENTS | scan_for_components()
		print(self.components)
		self.frontend.initialize()
		for component in self.components.values():
			c = component()
			c.initialize()
			self.frontend.register_component(c)
		self.frontend.run()
