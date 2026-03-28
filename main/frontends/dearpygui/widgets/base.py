from abc import ABC, abstractmethod
import dearpygui.dearpygui as dpg

class BaseWidget(ABC):
	@abstractmethod
	def initialize(self, widget, parent):
		pass

	def table_helper(self, widget, parent):
		output_cell=None
		with dpg.table(parent=parent, header_row=False, borders_innerV=False,borders_outerV=False,borders_outerH=False):
			dpg.add_table_column(init_width_or_weight=0.6)
			dpg.add_table_column(init_width_or_weight=0.4)

			with dpg.table_row():
				with dpg.table_cell():
					dpg.add_text(widget.label)
				output_cell=dpg.add_table_cell()
				# with dpg.table_cell():
				# 	dpg.add_input_text(width=-1)
		return output_cell
