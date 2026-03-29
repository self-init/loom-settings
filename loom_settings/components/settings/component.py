from ..base import BaseComponent
from .schema import SettingsSchema
from pathlib import Path
from importlib.resources import files

class SettingsComponent(BaseComponent):
	id = "settings"
	name = "Settings"

	def initialize(self):
		self.schemas = self.scan_for_schemas()

	def on_activate(self):
		pass

	def on_deactivate(self):
		pass

	def scan_for_schemas(self):
		dir = files("loom_settings") / "schemas"
		schemas = []
		for path in dir.iterdir():
			if path.is_file():
				schemas.append(SettingsSchema.load_from_file(path))
		return schemas
