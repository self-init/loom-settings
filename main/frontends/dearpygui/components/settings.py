from .base import BaseComponentView
import dearpygui.dearpygui as dpg
from ..widgets.text import TextWidget

class SettingsComponentView(BaseComponentView):
	def initialize(self, component, parent):
		self.tab_bar = dpg.add_tab_bar(parent=parent)
		for schema in component.schemas:
			schema_tab = dpg.add_tab(label=schema.name,parent=self.tab_bar)
			for entry in schema.widgets:
				if entry.type.name == "string":
					w = TextWidget()
					w.initialize(entry, schema_tab)
