# -*- coding: utf-8 -*-
#------------------------------------------------------------
# HAY Music
# (c) 2016 - Aram Ghamoyan
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.haymusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
FANART = local.getAddonInfo('fanart')

channellist=[
		("[COLOR darkorange]>>[/COLOR] HayFanat", "user/HayFanat", "https://yt3.ggpht.com/-0D1SybikhV8/AAAAAAAAAAI/AAAAAAAAAAA/7J_xG1c-bOI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Nshan Hayrapetyan", "user/nshik80", "https://yt3.ggpht.com/-Qz7OOcduSPE/AAAAAAAAAAI/AAAAAAAAAAA/CdzKOGWw6PM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Christine Pepelyan", "channel/UCvnYfFdSnfdh7gBMOc9YvOA", "https://yt3.ggpht.com/-vJ9qu4Yv5xU/AAAAAAAAAAI/AAAAAAAAAAA/uWsVCZFphLQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Tata Simonyan", "channel/UC6kYwNt9oJYJACUZfU3Ys5g", "https://yt3.ggpht.com/-Fj2S1TLDTDo/AAAAAAAAAAI/AAAAAAAAAAA/4jtjcQHpuFY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Armenchik", "user/ArmenEntertainment", "https://yt3.ggpht.com/-fCxIbC-wsoY/AAAAAAAAAAI/AAAAAAAAAAA/D-tYytk8KRc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]>>[/COLOR] Saro Tovmasyan", "channel/UC5mzVGXr0cAvhg64hJCEN8g", "https://yt3.ggpht.com/-FlBUkp5KHkA/AAAAAAAAAAI/AAAAAAAAAAA/_Nm_i7u011Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Arman Hovhannisyan", "channel/UCOYRNHKBVwxD_6qExTI4pQA", "https://yt3.ggpht.com/-O1LOlkHzoZA/AAAAAAAAAAI/AAAAAAAAAAA/ZwzJ1JBS28c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Vache Amaryan", "channel/UC1_Ag1GkP-5l34pLt2_Jrvw", "https://yt3.ggpht.com/-VWownHTxu3k/AAAAAAAAAAI/AAAAAAAAAAA/n_BC22cv96o/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Andre", "channel/UC_s3onMep3IpMmR0wFAgsSQ", "https://yt3.ggpht.com/-BUxnlMNofQw/AAAAAAAAAAI/AAAAAAAAAAA/9P_3-I-cf7E/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]>>[/COLOR] Super Sako", "channel/UCCmMrepaXt6jktLGtDAdtMw", "https://yt3.ggpht.com/-_KK7geTSWAU/AAAAAAAAAAI/AAAAAAAAAAA/6nqCLQF3W7o/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Noro", "channel/UCjDU6rCyUIBdKCCTJsJBN3g", "https://yt3.ggpht.com/-nBl6AQfyKW4/AAAAAAAAAAI/AAAAAAAAAAA/e2L9iRxzvDo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Mihran Tsarukyan", "user/MihranTsarukyan", "https://yt3.ggpht.com/-zBN0ECccoq0/AAAAAAAAAAI/AAAAAAAAAAA/dcxOjy3yLQA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]>>[/COLOR] Lilit Hovhannisyan", "user/LilitHovhannisyan", "https://yt3.ggpht.com/-hcygoXVHSL4/AAAAAAAAAAI/AAAAAAAAAAA/YCvRnjbCDVQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Martin Mkrtchyan", "user/MartinMkrtchyan", "https://yt3.ggpht.com/-9cwpvS-XuGI/AAAAAAAAAAI/AAAAAAAAAAA/aTsnbj41BzI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Razmik Amyan", "user/RazmikAmyanTv", "https://yt3.ggpht.com/-3vEgSUCvubs/AAAAAAAAAAI/AAAAAAAAAAA/wU9WhwLqWlY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Armenian Pulse", "user/armenianpulse", "https://yt3.ggpht.com/-zkmLUPxxsz8/AAAAAAAAAAI/AAAAAAAAAAA/bXbgp3u08S0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]>>[/COLOR] Music Of Armenia", "user/MusicOfArmenia", "https://yt3.ggpht.com/-odMibdRYRFg/AAAAAAAAAAI/AAAAAAAAAAA/ot-cGHbjPpI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Aram MP3", "user/AramMp3Official", "https://yt3.ggpht.com/-D8bIZD4yzDo/AAAAAAAAAAI/AAAAAAAAAAA/dki8QUm6WdM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Garik Papoyan", "user/GarikOfficialChanel", "https://yt3.ggpht.com/-Jm4S4uopdTY/AAAAAAAAAAI/AAAAAAAAAAA/sy_iEoejesk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Gevorg Martirosyan", "user/gevorgmusic", "https://yt3.ggpht.com/-fO6TjhS6T5o/AAAAAAAAAAI/AAAAAAAAAAA/jfTuLv0Zd4Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]>>[/COLOR] PlayBack", "user/MetsHayqThaBest", "https://yt3.ggpht.com/-PaeOQYbZ6pU/AAAAAAAAAAI/AAAAAAAAAAA/wMW6VZCLiaE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Lilu", "user/lilitmusic", "https://yt3.ggpht.com/-A1juZEwBrRQ/AAAAAAAAAAI/AAAAAAAAAAA/Xqa1rOK52B4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]>>[/COLOR] Duetro Studio", "user/DuetroStudio", "https://yt3.ggpht.com/--C5mA3aeB_8/AAAAAAAAAAI/AAAAAAAAAAA/d2MXrvzU5os/s100-c-k-no-mo-rj-c0xffffff/photo.jpg"),

]



# Entry point
def run():
    plugintools.log("clubtv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("clubtv.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()