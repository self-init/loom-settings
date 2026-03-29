from importlib.resources import files
import importlib.util
import inspect
from pathlib import Path

from ..components.base import BaseComponent

COMPONENT_DIRS = [
	#Path(str(files("loom_settings") / "components")),
	Path("/usr/share/loom-settings/components"),
	Path("/etc/loom-settings/components"),
	Path("~/.config/loom-settings/components").expanduser()
]

def discover(directory: Path, base_class: type) -> list[type]:
	found = []
	if not directory.exists():
		return found

	for path in directory.glob("*/__init__.py"):
		if path.parent.stem.startswith("_"):
			continue

		try:
			spec = importlib.util.spec_from_file_location(path.parent.stem, path)
			if spec is None:
				continue
			module = importlib.util.module_from_spec(spec)
			if spec.loader is None:
				continue
			spec.loader.exec_module(module)

			for _, obj in inspect.getmembers(module, inspect.isclass):
				if (
					issubclass(obj, base_class)
					and obj is not base_class
					and not inspect.isabstract(obj)
				):
					found.append(obj)
		except Exception as e:
			print(f"Warning: failed to load {path}: {e}")
			continue

	return found

def scan_for_components():
	components = {}
	for directory in COMPONENT_DIRS:
		discovered_components = discover(directory, BaseComponent)
		for comp in discovered_components:
			components[comp.id] = comp
	return components
