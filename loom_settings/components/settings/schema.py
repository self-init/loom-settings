from dataclasses import dataclass
from typing import Any
import tomlkit

from .widgets import SETTINGS_WIDGET_REGISTRY

class SettingsSchema:
	"""Schemas describe the layout and parameters of a program's config file(s)."""
	def __init__(self):
		self.name: str
		self.id: str
		self.description: str
		self.reload_cmd: str
		self.doc_url: str
		self.files = {}
		self.widgets = []

	@classmethod
	def load_from_file(cls, path):
		with open(path, "r") as f:
			doc = tomlkit.load(f)
			schema = SettingsSchema()
			schema.name = doc.value["meta"]["name"]
			schema.id = doc.value["meta"]["id"]
			schema.build_widgets(doc)
		return schema

	def build_files(self, data):
		for file in data["file"]:
			pass

	def build_widgets(self, data):
		for entry in data["setting"]:
			# f = SettingsSchemaFileEntry(
			# 	"","",""
			# )
			entry = SettingsSchemaEntry(
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

class SettingsSchemaEntry:
	def __init__(self, label, key, type, properties):
		self.label = label
		self.key = key
		self.type = type
		self.properties = properties
		self.cached_value = None
		self.is_dirty = False

	def update(self, value):
		self.cached_value = value
		self.is_dirty = True
