from dataclasses import dataclass
import tomlkit

from .widgets import SettingsWidgetType, SETTINGS_WIDGET_REGISTRY

class SettingsSchema:
	"""Schemas describe the layout and parameters within a program's config file(s)."""
	def __init__(self):
		self.name: str
		self.id: str
		self.description: str
		self.reload_cmd: str
		self.doc_url: str
		self.files = []
		self.widgets = []

	@classmethod
	def load_from_file(cls, path):
		with open(path, "r") as f:
			doc = tomlkit.load(f)
			schema = SettingsSchema()
			schema.name = doc["meta"]["name"]
			schema.id = doc["meta"]["id"]
			schema.build_widgets(doc)
		return schema

	def build_widgets(self, data):
		for entry in data["setting"]:
			f = SettingsSchemaFileEntry(
				"","",""
			)
			entry = SettingsSchemaSettingEntry(
				f,
				entry["label"],
				entry["key"],
				SETTINGS_WIDGET_REGISTRY[entry["type"]],
				{}
			)
			self.widgets.append(entry)

	def save(self):
		pass

	def reload(self):
		pass

	def pull(self):
		pass

@dataclass
class SettingsSchemaFileEntry:
	id: str
	adapter: str
	path: str

@dataclass
class SettingsSchemaSettingEntry:
	file: SettingsSchemaFileEntry
	label: str
	key: str
	type: SettingsWidgetType
	properties: dict

@dataclass
class SettingsSchemaSectionEntry:
	label: str
	entries: list[SettingsSchemaSettingEntry]
