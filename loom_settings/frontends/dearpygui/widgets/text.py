from .base import BaseWidget
import dearpygui.dearpygui as dpg

class TextWidget(BaseWidget):
	def initialize(self, widget, parent):
		with dpg.table(parent=parent, header_row=False, borders_innerV=False,borders_outerV=False,borders_outerH=False):
			dpg.add_table_column(init_width_or_weight=0.6)
			dpg.add_table_column(init_width_or_weight=0.4)

			with dpg.table_row():
				with dpg.table_cell():
					dpg.add_text(widget.label)
				with dpg.table_cell():
					dpg.add_input_text(width=-1)

		# with dpg.group(parent=parent,horizontal=True):
		# 	dpg.add_text(widget.label)
		# 	dpg.add_spacer(width=-1)
		# 	dpg.add_input_text(width=100)
