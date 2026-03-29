from dataclasses import dataclass
from types import NoneType

@dataclass
class SettingsWidgetType:
	name: str
	properties: list[str]
	value_type: type
	fallback: str = "string"

SETTINGS_WIDGET_REGISTRY = {
	"string": 	SettingsWidgetType("string", ["min_len", "max_len"], str),
	"int": 		SettingsWidgetType("int", ["min","max"], int),
	"float": 	SettingsWidgetType("float", ["min","max"], float),
	"section":  SettingsWidgetType("section", [], NoneType)
}
