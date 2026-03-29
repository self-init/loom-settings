from .frontends.dearpygui.frontend import DearPyGuiFrontend
from .core import AppCore

def main():
	AppCore(DearPyGuiFrontend).start()
