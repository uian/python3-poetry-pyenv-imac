# from nornir.core.plugins import registry

# for name, plugin in registry.items():
#     print(f"{name}: {plugin}")

# from nornir.core.configuration import Config
# from nornir.core.plugins import get_plugin

# config = Config()

# for plugin_name in config.plugins.keys():
#     plugin = get_plugin(plugin_name)
#     print(f"{plugin_name}: {plugin.__module__}")
# import nornir
# print(nornir.__version__)
# from nornir.core.plugins import PluginManager

# pm = PluginManager()
# print(pm.list_plugin_names())/
# 引入nornir的插件

from nornir.core.plugins import plugin 
from nornir.core.plugins import listed_plugin_objects

for plugin in listed_plugin_objects():
    print(f"Name: {plugin.name}")
    print(f"Description: {plugin.description}")
    print(f"Package: {plugin.package}\n")



