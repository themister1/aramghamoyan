import urllib,urllib2,re,uuid,time
import extract
import xbmcgui,xbmcplugin
import os
from addon.common.net import Net
net=Net()

AddonTitle="HAYbox Info"
thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.hayboxnews')
mediaPath = os.path.join(addonPath, 'media')
dokifanart = os.path.join(addonPath, 'fanart.jpg')
databasePath = xbmc.translatePath('special://database')
base='http://xml.dokitv.nl/'
dialog = xbmcgui.Dialog()

import utils

#######################################################################
#                          CLASSES
#######################################################################

class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi
        



        
#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
    xbmc.executebuiltin("Container.SetViewMode(500)")	
    addItem('[B]HAYbox Info[/B]', 'url', 11,os.path.join(mediaPath, "thumbs.png"))					    
#######################################################################
#						Add to menus
#######################################################################

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


def addDir(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
    
def addDir2(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False,Folder=True):
        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)
        if showcontext:
            contextMenu = []
            if showcontext == 'source':
                if name in str(SOURCES):
                    contextMenu.append(('Remove from Sources','XBMC.RunPlugin(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name))))
            elif showcontext == 'download':
                contextMenu.append(('Download','XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            elif showcontext == 'fav':
                contextMenu.append(('Remove from DutchMusic Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
                                    
            if not name in FAV:
                contextMenu.append(('Add to DutchMusic Favorites','XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        liz.setArt({'fanart': dokifanart})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=Folder)

        return ok
    
def addItem(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage,)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setArt({'fanart': dokifanart})
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

#######################################################################
#						Parses Choice
#######################################################################
      
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
			params=sys.argv[2]
			cleanedparams=params.replace('?','')
			if (params[len(params)-1]=='/'):
					params=params[0:len(params)-2]
			pairsofparams=cleanedparams.split('&')
			param={}
			for i in range(len(pairsofparams)):
					splitparams={}
					splitparams=pairsofparams[i].split('=')
					if (len(splitparams))==2:
							param[splitparams[0]]=splitparams[1]
							
	return param   

#######################################################################
#						Work Functions
#######################################################################

def DownloaderClass(url,dest, useReq = False):
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Bestanden downloaden.",'')

    if useReq:
        import urllib2
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://wallpaperswide.com/')
        f       = open(dest, mode='wb')
        resp    = urllib2.urlopen(req)
        content = int(resp.headers['Content-Length'])
        size    = content / 100
        total   = 0
        while True:
            if dp.iscanceled(): 
                raise Exception("Canceled")                
                dp.close()

            chunk = resp.read(size)
            if not chunk:            
                f.close()
                break

            f.write(chunk)
            total += len(chunk)
            percent = min(100 * total / content, 100)
            dp.update(percent)       
    else:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()				

def Nieuws():
	text = ''
	twit = 'https://raw.githubusercontent.com/aramghamoyan/aramghamoyan/master/HAYbox%20XMLS/newsflits.xml'
	req = urllib2.Request(twit)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	match=re.compile("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)
	for status, dte in match:
	    try:
			    status = status.decode('ascii', 'ignore')
	    except:
			    status = status.decode('utf-8','ignore')
	    dte = dte[:-15]
	    status = status.replace('&amp;','')
	    dte = '[COLOR red][B]'+dte+'[/B][/COLOR]'
	    text = text+dte+'\n'+status+'\n'+'\n'
	showText('[COLOR red]HAYbox TV Nieuws Flits[/COLOR]', text)	

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
	try:
	    xbmc.sleep(10)
	    retry -= 1
	    win.getControl(1).setLabel(heading)
	    win.getControl(5).setText(text)
	    return
	except:
	    pass
					
		
		
		
#######################################################################
#						START MAIN
#######################################################################              


params=get_params()
url=None
name=None
mode=None
fanart=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:    
		fanart=urllib.unquote_plus(params["fanart"])
except: 
		pass		

if mode==None or url==None or len(url)<1:
        mainMenu()
 	
elif mode==11:	
	Nieuws()	

xbmcplugin.endOfDirectory(int(sys.argv[1]))

