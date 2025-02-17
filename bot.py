import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter

nonebot.init(command_start=[""])
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)

nonebot.load_builtin_plugins("echo")
# nonebot.load_plugin("nonebot_plugin_help")
nonebot.load_plugins("src/plugins")

if __name__ == "__main__":
    nonebot.run()
