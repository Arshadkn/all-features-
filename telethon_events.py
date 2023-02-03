import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"HyDrix-Tools-Bot-New/Telethon/{plugin_name}.py")
    name = "HyDrix-Tools-Bot-New.Telethon.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["HyDrix-Tools-Bot-New.Telethon." + plugin_name] = load
    print("Hydrix Tool Bot has Imported " + plugin_name)
