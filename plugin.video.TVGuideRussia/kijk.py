
import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
	utils.addDir('Shant TV','https://tv.yandex.ru/213/channels/1725',284,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/11-%D0%B9_%D0%BB%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F-1.svg_.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Pervyy','https://tv.yandex.ru/213/channels/146',246,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/11-%D0%B9_%D0%BB%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F-1.svg_.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Russia 1','https://tv.yandex.ru/213/channels/711',255,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%B9.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
	utils.addDir('Russia 24','https://tv.yandex.ru/213/channels/1683',259,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
	utils.addDir('Russia Kultura','https://tv.yandex.ru/213/channels/187',260,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
	utils.addDir('HTB','https://tv.yandex.ru/213/channels/162',261,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
	utils.addDir('HTB Mir','https://tv.yandex.ru/213/channels/726',262,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
	utils.addDir('Match! TV','https://tv.yandex.ru/213/channels/1593',256,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Nash Sport','https://tv.yandex.ru/213/channels/1669',263,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Planeta','https://tv.yandex.ru/213/channels/1671',264,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Arena','https://tv.yandex.ru/213/channels/1667',265,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Boyets','https://tv.yandex.ru/213/channels/454',266,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Igra','https://tv.yandex.ru/213/channels/1668',267,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Futbol 1','https://tv.yandex.ru/213/channels/664',268,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Futbol 2','https://tv.yandex.ru/213/channels/563',269,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Futbol 3','https://tv.yandex.ru/213/channels/1039',270,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Match! Nash Futbol','https://tv.yandex.ru/213/channels/499',271,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('EuroSport 1','https://tv.yandex.ru/213/channels/737',272,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('EuroSport 2','https://tv.yandex.ru/213/channels/850',273,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('KHL','https://tv.yandex.ru/213/channels/481',274,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Extreme Sports','https://tv.yandex.ru/213/channels/288',275,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Viasat Sport','https://tv.yandex.ru/213/channels/455',276,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Premiere','https://tv.yandex.ru/213/channels/566',277,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Kinohit','https://tv.yandex.ru/213/channels/542',278,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Nashe Novoye Kino','https://tv.yandex.ru/213/channels/485',279,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Evrokino','https://tv.yandex.ru/213/channels/352',280,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Russkiy Illyuzion','https://tv.yandex.ru/213/channels/53',281,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('TV1000','https://tv.yandex.ru/213/channels/127',282,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('TV1000 Russische Cinema','https://tv.yandex.ru/213/channels/267',283,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('TV1000 Action','https://tv.yandex.ru/213/channels/125',285,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('TV1000 Comedy','https://tv.yandex.ru/213/channels/1011',286,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('TV1000 Megahit','https://tv.yandex.ru/213/channels/1012',287,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Muzhskoye kino','https://tv.yandex.ru/213/channels/1584',288,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Sony TV','https://tv.yandex.ru/213/channels/1034',289,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Sony Sci-Fi','https://tv.yandex.ru/213/channels/516',290,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Sony Turbo','https://tv.yandex.ru/213/channels/935',291,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Illyuzion +','https://tv.yandex.ru/213/channels/123',292,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('AMC','https://tv.yandex.ru/213/channels/608',293,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('CBS Drama','https://tv.yandex.ru/213/channels/911',294,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Nostalgiya','https://tv.yandex.ru/213/channels/783',295,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Mnogo TV','https://tv.yandex.ru/213/channels/799',296,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Komediya','https://tv.yandex.ru/213/channels/1620',297,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Paramount Comedy','https://tv.yandex.ru/213/channels/920',298,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('2x2','https://tv.yandex.ru/213/channels/323',299,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Amedia 1','https://tv.yandex.ru/213/channels/1371',301,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Amedia 2','https://tv.yandex.ru/213/channels/918',302,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Amedia Premium','https://tv.yandex.ru/213/channels/1372',303,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Fox Russia','https://tv.yandex.ru/213/channels/659',304,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Fox Life','https://tv.yandex.ru/213/channels/615',305,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Dom Kino','https://tv.yandex.ru/213/channels/834',306,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('CTC','https://tv.yandex.ru/213/channels/79',307,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('CTC Love','https://tv.yandex.ru/213/channels/1322',308,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('THT 4','https://tv.yandex.ru/213/channels/1649',309,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Moya Planeta','https://tv.yandex.ru/213/channels/675',310,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')

	utils.addDir('Nat Geo Wild','https://tv.yandex.ru/213/channels/223',311,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	utils.addDir('Discovery Channel','https://tv.yandex.ru/213/channels/225',312,'','https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/Images/iaqUpVfm.jpg',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
	
	xbmcplugin.endOfDirectory(utils.addon_handle)

def ListPervyy(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/146" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')			
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListRussia1(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/711" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListMatch(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1593" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListRussia24(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1683" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListRussiaKultura(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/187" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListHTB(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/162" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListHTBMir(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/726" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListNashSport(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1669" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListPlaneta(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1671" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListArena(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1667" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListBoyets(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/454" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListIgra(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1668" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListFutbol1(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/664" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListFutbol2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/563" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListFutbol3(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1039" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListNashFutbol(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/499" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListEuroSport1(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/737" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListEuroSport2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/850" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListKHL(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/481" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListExtremeSports(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/288" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListViasatSport(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/455" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListPremiere(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/566" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListKinohit(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/542" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListNasheNovoyeKino(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/485" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListEvrokino(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/352" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListRusskiyIllyuzion(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/53" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTV1000(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/127" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTV1000RussischeCinema(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/267" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListShantTV(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1725" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTV1000Action(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/125" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTV1000Comedy(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1011" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTV1000Megahit(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1012" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListMuzhskoyeKino(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1584" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListSonyTV(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1034" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListSonySciFi(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/516" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListSonyTurbo(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/935" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListIllyuzion(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/123" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListAMC(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/608" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListCBSDrama(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/911" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListNostalgiya(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/783" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListMnogoTV(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/799" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListKomediya(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1620" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListParamountComedy(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/920" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def List2x2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/323" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListAmedia1(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1371" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListAmedia2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/918" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListAmediaPremium(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/918" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListFoxRussia(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/659" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListFoxLife(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/615" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListDomKino(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/834" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListCTC(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/79" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListCTCLove(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1322" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListTHT4(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/1649" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListMoyaPlaneta(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/675" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListNatGeoWild(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/223" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListDiscoveryChannel(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="link tv-filter-days__link" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for pagina, name, in match:
            name = utils.cleantext(name)
            pagina = "https://tv.yandex.ru/213/channels/325" + pagina
            utils.addDir(name, pagina, 258, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
	
def ListGuide(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<span class="tv-event__time-text">(.*?)</span></span><div class="tv-event__title"><div class="tv-event__title-inner">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for time, titel in match:
        name = '[COLOR red]' + time + '[/COLOR]' + ' | ' + ' ' + titel
        utils.addDir(name, url, '', 'https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/images/guide.png', Folder=False)
    xbmcplugin.endOfDirectory(utils.addon_handle)
