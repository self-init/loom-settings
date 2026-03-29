from abc import ABC, abstractmethod

class BaseComponentView(ABC):
	@abstractmethod
	def initialize(self, component, parent):
		pass



	# @abstractmethod
	# def on_activate(self):
	# 	pass

	# @abstractmethod
	# def on_deactivate(self):
	# 	pass
