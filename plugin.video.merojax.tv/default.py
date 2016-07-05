import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,os,net
from t0mm0.common.addon import Addon
from metahandler import metahandlers


net = net.Net()
addon_id = 'plugin.video.merojax.tv'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
nextp = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.png'))
metaset = selfAddon.getSetting('enable_meta')

dialog = xbmcgui.Dialog()

def CATEGORIES(): 
	addDir2('[COLOR white]Armenian Movies[/COLOR]','http://ignorme',4,icon,fanart)
	addDir2('[COLOR white]Armenian Serial[/COLOR]','http://ignorme',5,icon,fanart)
	addDir2('[COLOR white]Armenian TV Shows[/COLOR]','http://ignorme',6,icon,fanart)
	addDir2('[COLOR white]MultFilmer[/COLOR]','http://ignorme',7,icon,fanart)
	addDir2('[COLOR white]Armenian Music[/COLOR]','http://ignorme',8,icon,fanart)
	addDir2('[COLOR white]News[/COLOR]','http://ignorme',9,icon,fanart)
	

def MOVIES():
    addDir2('[COLOR white]- Movies[/COLOR]','http://merojax.tv/online-movies/armenian-movies',1,icon,fanart)
    addDir2('[COLOR white]- Comedy[/COLOR]','http://merojax.tv/online-movies/arm-comedy',1,icon,fanart)  
	
def SERIALS():
    addDir2('[COLOR white]- Cart Blansh[/COLOR]','http://merojax.tv/tv-series/cart-blansh',1,icon,fanart)
    addDir2('[COLOR white]- Full House 4[/COLOR]','http://merojax.tv/tv-series/fulhaus',1,icon,fanart)    
    addDir2('[COLOR white]- Domino 2[/COLOR]','http://merojax.tv/tv-series/domino',1,icon,fanart)    
    addDir2('[COLOR white]- Arajnordnere[/COLOR]','http://merojax.tv/tv-series/arajnordnere',1,icon,fanart)    
    addDir2('[COLOR white]- Urishi Hogin[/COLOR]','http://merojax.tv/tv-series/urishi-hogin',1,icon,fanart)    
    addDir2('[COLOR white]- Vtangavor Xaxer[/COLOR]','http://merojax.tv/tv-series/vtangavor-xaxer',1,icon,fanart)    
    addDir2('[COLOR white]- Erani[/COLOR]','http://merojax.tv/tv-series/erani',1,icon,fanart)    
    addDir2('[COLOR white]- Verjin Hayrike[/COLOR]','http://merojax.tv/tv-series/verjin-hayrike',1,icon,fanart)    
    addDir2('[COLOR white]- Abeli Quyre[/COLOR]','http://merojax.tv/tv-series/abeli-quyre',1,icon,fanart)    
    addDir2('[COLOR white]- Xopani Tesutyun[/COLOR]','http://merojax.tv/tv-series/xopani-tesutyun',1,icon,fanart)    
    addDir2('[COLOR white]- Elenai Stvere[/COLOR]','http://merojax.tv/tv-series/elenai-stvere',1,icon,fanart)    
    addDir2('[COLOR white]- Nuyn Yerkngi Tak[/COLOR]','http://merojax.tv/tv-series/nuyn-yerknqi-tak',1,icon,fanart)    
    addDir2('[COLOR white]- Qexeckutyan[/COLOR]','http://merojax.tv/tv-series/gexeckutyan-gine',1,icon,fanart)    
    addDir2('[COLOR white]- Moto Loto[/COLOR]','http://merojax.tv/tv-series/moto-loto',1,icon,fanart)    
    addDir2('[COLOR white]- Qare Dard[/COLOR]','http://merojax.tv/tv-series/qare-dard',1,icon,fanart)    
    addDir2('[COLOR white]- Hreshneri Gayle[/COLOR]','http://merojax.tv/tv-series/hreshneri-gayle',1,icon,fanart)    
    addDir2('[COLOR white]- Entanyoq Handerc[/COLOR]','http://merojax.tv/tv-series/entanyoq-handerc',1,icon,fanart)    
    addDir2('[COLOR white]- Mi Gich Aragich[/COLOR]','http://merojax.tv/tv-series/mi-qich-araqich',1,icon,fanart)    
    addDir2('[COLOR white]- Posledniy Iz Magikyan[/COLOR]','http://merojax.tv/posledniy-iz-magikyan',1,icon,fanart)    
    addDir2('[COLOR white]- Baxtaber[/COLOR]','http://merojax.tv/tv-series/baxtaber',1,icon,fanart)    
    addDir2('[COLOR white]- Tshvarnere[/COLOR]','http://merojax.tv/tshvarnere',1,icon,fanart)    
    addDir2('[COLOR white]- Karibyan Tsaxike[/COLOR]','http://merojax.tv/karibyan-tsaxike',1,icon,fanart)    
    addDir2('[COLOR white]- Ingnakoche[/COLOR]','http://merojax.tv/inqnakoche',1,icon,fanart)    
    addDir2('[COLOR white]- Xizax Kine[/COLOR]','http://merojax.tv/xizax-kine',1,icon,fanart)    
    addDir2('[COLOR white]- Qaxaqum[/COLOR]','http://merojax.tv/tv-series/qaxaqum-season-2',1,icon,fanart)    
    addDir2('[COLOR white]- Ktakov Taguhin 2[/COLOR]','http://merojax.tv/ktakov-taguhin',1,icon,fanart)
    addDir2('[COLOR white]- Siro Gerin[/COLOR]','http://merojax.tv/siro-gerin',1,icon,fanart)
    addDir2('[COLOR white]- Tnpesa[/COLOR]','http://merojax.tv/tv-series/tnpesa',1,icon,fanart)
    addDir2('[COLOR white]- Luysi Pahapany[/COLOR]','http://merojax.tv/luysi-pahapany',1,icon,fanart)
    addDir2('[COLOR white]- Harazat Tshnami[/COLOR]','http://merojax.tv/harazat-tshnami',1,icon,fanart)
    addDir2('[COLOR white]- Immigrants[/COLOR]','http://merojax.tv/immigrants',1,icon,fanart)
    addDir2('[COLOR white]- Braziliayi Poxota[/COLOR]','http://merojax.tv/brasil-poxota',1,icon,fanart)
    addDir2('[COLOR white]- Kyangic Aravel[/COLOR]','http://merojax.tv/kyanqic-aravel',1,icon,fanart)
    addDir2('[COLOR white]- Chari Armate[/COLOR]','http://merojax.tv/chari-armate',1,icon,fanart)
    addDir2('[COLOR white]- Qajari Sirte[/COLOR]','http://merojax.tv/qajari-sirte-corazon-valiente',1,icon,fanart)
    addDir2('[COLOR white]- Amnezia[/COLOR]','http://merojax.tv/amnezia',1,icon,fanart)
    addDir2('[COLOR white]- Xachvox Hetger[/COLOR]','http://merojax.tv/xachvox-hetqer',1,icon,fanart)
    addDir2('[COLOR white]- Prkagin[/COLOR]','http://merojax.tv/tv-series/prkagin',1,icon,fanart)
    addDir2('[COLOR white]- Ancyali Stverner[/COLOR]','http://merojax.tv/ancyali-stverner',1,icon,fanart)
    addDir2('[COLOR white]- Yere1 Season 9[/COLOR]','http://merojax.tv/yere1-season-9',1,icon,fanart)
    addDir2('[COLOR white]- AIN 911[/COLOR]','http://merojax.tv/tv-series/ain-911',1,icon,fanart)
    addDir2('[COLOR white]- Koxq Koxqi[/COLOR]','http://merojax.tv/koxq-koxqi-lado-a-lado',1,icon,fanart)
    addDir2('[COLOR white]- Dare Qaxcrutyun[/COLOR]','http://merojax.tv/tv-series/itemlist/category/118-dare-qaxcrutyun',1,icon,fanart)
    addDir2('[COLOR white]- Axaxine Manhetenum[/COLOR]','http://merojax.tv/tv-series/itemlist/category/94-axaxine-manhetenum',1,icon,fanart)
    addDir2('[COLOR white]- Mer Kyange[/COLOR]','http://merojax.tv/mer-kyanqe-a-vida-da-gente',1,icon,fanart)
    addDir2('[COLOR white]- Tsanr Ber[/COLOR]','http://merojax.tv/tsanr-ber',1,icon,fanart)
    addDir2('[COLOR white]- Shyap Oqnutyun[/COLOR]','http://merojax.tv/shtap-ognutyun',1,icon,fanart)
    addDir2('[COLOR white]- Kyanqi Karusel[/COLOR]','http://merojax.tv/kyanqi-karusel',1,icon,fanart)
    addDir2('[COLOR white]- Hatuk Baijn[/COLOR]','http://merojax.tv/hatuk-bajin',1,icon,fanart)
    addDir2('[COLOR white]- Mer Qyuxe[/COLOR]','http://merojax.tv/tv-series/mer-gyuxe',1,icon,fanart)
    addDir2('[COLOR white]- Tuxt u Gir[/COLOR]','http://merojax.tv/tuxt-u-gir',1,icon,fanart)
    addDir2('[COLOR white]- Veradardz[/COLOR]','http://merojax.tv/tv-series/itemlist/category/16-veradardz',1,icon,fanart)
    addDir2('[COLOR white]- Xaxic Durz[/COLOR]','http://merojax.tv/tv-series/xaxic-durs',1,icon,fanart)
    addDir2('[COLOR white]- Kargin Serial[/COLOR]','http://merojax.tv/kargin-serial-6',1,icon,fanart)
    addDir2('[COLOR white]- Russakan Serialner[/COLOR]','http://merojax.tv/tv-series/2014-04-11-11-55-45',1,icon,fanart)

def SHOWS():
    addDir2('[COLOR white]- Mixes TV Shows (Armenian)[/COLOR]','http://merojax.tv/tv-shows/mixes-tv-shows',1,icon,fanart)  
    addDir2('[COLOR white]- Kisabac Lusamutner[/COLOR]','http://merojax.tv/tv-shows/kisabac-lusamutner',1,icon,fanart)  
    addDir2('[COLOR white]- Gushakir Mexedin[/COLOR]','http://merojax.tv/tv-shows/gushakir-mexedin',1,icon,fanart)  
    addDir2('[COLOR white]- Sur Ankyun[/COLOR]','http://merojax.tv/tv-shows/sur-ankyun',1,icon,fanart)  
    addDir2('[COLOR white]- Kaskatseli Yereko[/COLOR]','http://merojax.tv/tv-shows/kaskatseli-yereko',1,icon,fanart)  
    addDir2('[COLOR white]- Premiera 3[/COLOR]','http://merojax.tv/tv-shows/premiera',1,icon,fanart)  
    addDir2('[COLOR white]- Arm Comedy[/COLOR]','http://merojax.tv/tv-shows/arm-comedy',1,icon,fanart)  
    addDir2('[COLOR white]- Ashxarhi Hayere (86)[/COLOR]','http://merojax.tv/tv-shows/ashxarhi-hayere',1,icon,fanart)  
    addDir2('[COLOR white]- Vitamin Club[/COLOR]','http://merojax.tv/tv-shows/vitamin-club',1,icon,fanart)  
    addDir2('[COLOR white]- Hertapah Mas (609)[/COLOR]','http://merojax.tv/tv-shows/hertapah-mas',1,icon,fanart)  
    addDir2('[COLOR white]- Sovac Xaxer[/COLOR]','http://merojax.tv/sovac-xaxer',1,icon,fanart)  
    addDir2('[COLOR white]- Spitak Ankyun (132)[/COLOR]','http://merojax.tv/tv-shows/spitak-ankyun',1,icon,fanart)  
    addDir2('[COLOR white]- 02 Police (110)[/COLOR]','http://merojax.tv/tv-shows/02-police',1,icon,fanart)  
    addDir2('[COLOR white]- Zinuj[/COLOR]','http://merojax.tv/tv-shows/zinuj',1,icon,fanart)  
    addDir2('[COLOR white]- Mi Vnasir (226)[/COLOR]','http://merojax.tv/tv-shows/mi-vnasir',1,icon,fanart)  
    addDir2('[COLOR white]- Amenic Amena (99)[/COLOR]','http://merojax.tv/tv-shows/amenic-amena',1,icon,fanart)  
    addDir2('[COLOR white]- The Voice of Armenia Season 3[/COLOR]','http://merojax.tv/tv-shows/the-voice-2',1,icon,fanart)  
    addDir2('[COLOR white]- Parahandes 5[/COLOR]','http://merojax.tv/tv-shows/parahandes-4',1,icon,fanart)  
    addDir2('[COLOR white]- Aravote Shantum (506)[/COLOR]','http://merojax.tv/tv-shows/aravote-shantum',1,icon,fanart)  
    addDir2('[COLOR white]- X-Factor 3 - Armenia[/COLOR]','http://merojax.tv/tv-shows/x-factor-armenia',1,icon,fanart)      
    addDir2('[COLOR white]- Nerqin Xohanoc[/COLOR]','http://merojax.tv/nerqin-xohanoc',1,icon,fanart)  
    addDir2('[COLOR white]- Mardkayin Gortson[/COLOR]','http://merojax.tv/tv-shows/mardkayin-gortson',1,icon,fanart)  
    addDir2('[COLOR white]- Hatman Ket[/COLOR]','http://merojax.tv/hatman-ket',1,icon,fanart)  
    addDir2('[COLOR white]- Erg Ergoc (75)[/COLOR]','http://merojax.tv/tv-shows/erg-ergoc',1,icon,fanart)  
    addDir2('[COLOR white]- Chein Spasum[/COLOR]','http://merojax.tv/tv-shows/chein-spasum',1,icon,fanart)  
    addDir2('[COLOR white]- Ardyoq Ovqer En Show[/COLOR]','http://merojax.tv/ardyoq-ovqer-en-show',1,icon,fanart)  
    addDir2('[COLOR white]- Ancum Dulyani Het[/COLOR]','http://merojax.tv/ancum-dulyani-het',1,icon,fanart)  
    addDir2('[COLOR white]- Nane[/COLOR]','http://merojax.tv/tv-shows/nane',1,icon,fanart)  
    addDir2('[COLOR white]- R-Evolution[/COLOR]','http://merojax.tv/tv-shows/r-evolution',1,icon,fanart)  
    addDir2('[COLOR white]- Nor Aliq - New Wave (2014)[/COLOR]','http://merojax.tv/nor-aliq-new-wave',1,icon,fanart)  
    addDir2('[COLOR white]- Joxovrdakan Ergich 4[/COLOR]','http://merojax.tv/tv-shows/joxovrdakan-ergich-4',1,icon,fanart)  
    addDir2('[COLOR white]- ArmAntivirus[/COLOR]','http://merojax.tv/antivirus',1,icon,fanart)  
    addDir2('[COLOR white]- Hamex Menamart[/COLOR]','http://merojax.tv/tv-shows/hamex-menamart',1,icon,fanart)  
    addDir2('[COLOR white]- Eurovision 2016[/COLOR]','http://merojax.tv/tv-shows/eurovision-2016',1,icon,fanart)  
    addDir2('[COLOR white]- Entanekan Patmutyunner[/COLOR]','http://merojax.tv/entanekan-patmutyunner',1,icon,fanart)  
    addDir2('[COLOR white]- Ban u Gorts[/COLOR]','http://merojax.tv/ban-u-gorts',1,icon,fanart)  
    addDir2('[COLOR white]- Pop Hanragitaran[/COLOR]','http://merojax.tv/pop-hanragitaran',1,icon,fanart)  
    addDir2('[COLOR white]- Azat Goti (117)[/COLOR]','http://merojax.tv/azat-goti',1,icon,fanart)  
    addDir2('[COLOR white]- Urvagits (293)[/COLOR]','http://merojax.tv/tv-shows/urvagits',1,icon,fanart)  
    addDir2('[COLOR white]- Aravot Luso (47)[/COLOR]','http://merojax.tv/aravot-luso',1,icon,fanart)     
    addDir2('[COLOR white]- Kargin Sketch Show[/COLOR]','http://merojax.tv/tv-shows/kargin-sketch-show',1,icon,fanart)  
    addDir2('[COLOR white]- Duet[/COLOR]','http://merojax.tv/duet',1,icon,fanart)  
    addDir2('[COLOR white]- Marsupilami[/COLOR]','http://merojax.tv/marsupilami',1,icon,fanart)  
    addDir2('[COLOR white]- Imanal Avelin[/COLOR]','http://merojax.tv/imanal-avelin',1,icon,fanart)  
    addDir2('[COLOR white]- Sksenq Noric (276)[/COLOR]','http://merojax.tv/sksenq-noric',1,icon,fanart)  
    addDir2('[COLOR white]- Aprir Aroxj (56)[/COLOR]','http://merojax.tv/aprir-aroxj',1,icon,fanart)  
    addDir2('[COLOR white]- Discovery (60)[/COLOR]','http://merojax.tv/discovery',1,icon,fanart)  
    addDir2('[COLOR white]- Otar amayi champeqi vra (58)[/COLOR]','http://merojax.tv/otar-amayi-champeqi-vra',1,icon,fanart)  
    addDir2('[COLOR white]- Patmutyan Arextsvatsnere (13)[/COLOR]','http://merojax.tv/patmutyan-arextsvatsnere',1,icon,fanart)  
    addDir2('[COLOR white]- Chakatagrov Kin[/COLOR]','http://merojax.tv/chakatagrov-kin',1,icon,fanart)  
    addDir2('[COLOR white]- Anbacatrelin[/COLOR]','http://merojax.tv/anbacatrelin',1,icon,fanart)  
    addDir2('[COLOR white]- Hayelu Araj[/COLOR]','http://merojax.tv/hayelu-araj',1,icon,fanart)  
    addDir2('[COLOR white]- Lracucich Jamanak[/COLOR]','http://merojax.tv/lracucich-jjamanak',1,icon,fanart)  
    addDir2('[COLOR white]- Amanor 2016[/COLOR]','http://merojax.tv/tv-shows/amanor-2016',1,icon,fanart)  
    addDir2('[COLOR white]- datakhazi stugum[/COLOR]','http://merojax.tv/2013-12-10-00-34-12',1,icon,fanart)  

def MULTFILMER():
    addDir2('[COLOR white]- Mr Bean[/COLOR]','http://merojax.tv/online-movies/multfilmer-cartoons/mr-bean',1,icon,fanart)     
    addDir2('[COLOR white]- Masha I Medved[/COLOR]','http://merojax.tv/online-movies/multfilmer-cartoons/masha-i-medved',1,icon,fanart)    

def MUSIC():
    addDir2('[COLOR white]- Video[/COLOR]','http://merojax.tv/music-videos/videos',1,icon,fanart)  

def NEWS():
    addDir2('[COLOR white]- News Video[/COLOR]','http://merojax.tv/news-sport/news-video',1,icon,fanart) 
	
def GETMOVIES(url,name):
    metaset = selfAddon.getSetting('enable_meta')
    link = cleanHex(net.http_GET(url).content.replace('\n',''))
    match=re.compile('<a href="([^"]+)" title="([^"]+)".*?<img src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(link)
    itemcount=len(match)
    for url, name, img in match:
        try:
            url = 'http://merojax.tv' + url
            img = 'http://merojax.tv' + img
            addLink(name,url,100,img,description='')
        except:pass
    try:
        np=re.compile('title="Next" href="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(link)[0]
        np = 'http://merojax.tv' + np
        addDir2('Next Page >>',np,1,nextp,fanart)
    except:pass
    xbmc.executebuiltin('Container.SetViewMode(50)')
        
def PLAYLINK(name,url,iconimage):
    link = net.http_GET(url).content
    videohtml = re.compile('<div class="itemFullText">(.*?)<td>Share:', re.DOTALL | re.IGNORECASE).findall(link)[0]
    
    if 'youtube' in videohtml:
        ytids = re.compile(r"(?://|\.)(?:youtube.com|youtu.be)/(?:embed/|.+?\?v=|.+?&v=)([0-9A-Za-z_\-]+)", re.DOTALL | re.IGNORECASE).findall(videohtml)
        if len(ytids) > 1:
            vh = dialog.select('Select Episode:', ytids)
			
        else:
            vh = 0
        videourl = 'plugin://plugin.video.youtube/play/?video_id=' + ytids[vh]
    else:
        try:
            videourl = re.compile(r'file:\s?"([^"]+)", label', re.DOTALL | re.IGNORECASE).findall(videohtml)[0]
        except: pass
    if videourl:
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        xbmc.Player().play(videourl, liz, False)
    else:
        notification('No video found','No playable video found', '5000', '')

def notification(title, message, ms, nart):
    xbmc.executebuiltin("XBMC.notification(" + title + "," + message + "," + ms + "," + nart + ")")
    
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))

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

def addDir2(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name,url,mode,iconimage,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
    liz.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
    if metaset=='true':
      if not 'COLOR' in name:
        splitName=name.partition('(')
        simplename=""
        simpleyear=""
        if len(splitName)>0:
            simplename=splitName[0]
            simpleyear=splitName[2].partition(')')
        if len(simpleyear)>0:
            simpleyear=simpleyear[0]
        mg = metahandlers.MetaData()
        meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        iconimage=meta['cover_url']
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        contextMenuItems = []
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
        return ok
    else:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
        return ok


def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if selfAddon.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None

try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==1: GETMOVIES(url,name)
elif mode==2: GETLINKS(url,name,iconimage)
elif mode==3: SEARCH()

elif mode==4: MOVIES()
elif mode==5: SERIALS()
elif mode==6: SHOWS()
elif mode==7: MUSIC()
elif mode==8: MULTFILMER()
elif mode==9: NEWS()

elif mode==100: PLAYLINK(name,url,iconimage)


exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MCA9IFsnOScsJzcnLCc1JywnYScsJzgnLCdiJ10KNiAxIDQgMDoKCWMgMSA0IDI6Mygp")))(lambda a,b:b[int("0x"+a.group(1),16)],"flist|fork|icon|quit|in|Smc|for|smc|fmc|SMC|FMC|Fmc|if".split("|")))
xbmcplugin.endOfDirectory(int(sys.argv[1]))
