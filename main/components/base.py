from abc import ABC, abstractmethod

class BaseComponent(ABC):
	"""Component interface implemented by all other components.

	Components are self-contained feature modules that each handle a distinct
	area of system management.
	"""
	id: str
	name: str

	@abstractmethod
	def initialize(self):
		pass

	@abstractmethod
	def on_activate(self):
		pass

	@abstractmethod
	def on_deactivate(self):
		pass

	def load_adapters(self):
		pass
