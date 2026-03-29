from abc import ABC, abstractmethod

class BaseFileAdapter(ABC):
	"""BaseFileAdapter is the interface that all other file adapters must implement.

	A file adapter is the interface by which config files are opened, read, and saved.
	It adapts the config file's format to the key value pairs of the schema.
	"""
	id: str
	path: str
	entries: list

	@abstractmethod
	def parse_file():
		pass

	@abstractmethod
	def save_file():
		pass
