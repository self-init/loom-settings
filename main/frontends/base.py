from abc import ABC, abstractmethod

class BaseFrontend(ABC):
	"""The base frontend is the interface which all other frontends must implement.

	Frontends provide the GUI functionality of the app by interacting with components.
	"""
	@abstractmethod
	def initialize(self):
		pass

	@abstractmethod
	def run(self):
		pass

	@abstractmethod
	def shutdown(self):
		pass

	@abstractmethod
	def register_component(self, component):
		pass

	# @abstractmethod
	# def show_error(self):
	# 	pass

	# @abstractmethod
	# def show_success(self):
	# 	pass

	# @abstractmethod
	# def show_confirm(self):
	# 	pass
