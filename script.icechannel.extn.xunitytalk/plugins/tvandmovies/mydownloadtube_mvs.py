from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin
from entertainment import common
import xbmcaddon


class putlockeris(MovieSource):
    implements = [MovieSource]
    
    name = "MyDownloadTube"
    display_name = "MyDownloadTube"
    source_enabled_by_default = 'true'
    
    def GetFileHosts(self, url, list, lock, message_queue):
        import re

        from entertainment.net import Net
        net = Net(cached=False)

        
        ADDON=xbmcaddon.Addon(id='script.module.urlresolver') 
        movielink = net.http_GET(url).content.encode('ascii', 'ignore')
        
            
        links=re.compile('<a class="download_item".+?href="(.+?)".+?\'Downloads-Server\', \'(.+?)\'(.+?)</a>',re.DOTALL).findall(movielink)        
        for url ,host, fuckup in links:
            
            if 'Bit -' in host:
                host=host.split('Bit -')[1].upper().strip()
            if '(factory)' in host:
                host='FILEFACTORY'
                
            if '1080' in fuckup:
                res='1080P'
            elif '720' in fuckup:
                res='720P'
            elif '4k' in fuckup.lower():
                res='4K'
            elif '3d' in fuckup.lower():
                res='3D'
            else:
                res='HD'
                
            if not 'promo' in host.lower():
                if not 'multi' in host.lower():
                    if ADDON.getSetting('RealDebridResolver_token')=='':
                        if 'UPTOBOX' in host:
                            self.AddFileHost(list, res, url,host=host)
                    else:        
                        self.AddFileHost(list, res, url,host=host)



    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        import json
        from entertainment.net import Net
        net = Net(cached=False)
        name = self.CleanTextForSearch(name)

        search_url = 'http://www.mydownloadtube.com/search/search_val?language=English%20-%20UK&term=' + name.replace(' ','+')
        
        content = net.http_GET(search_url).content
        link=json.loads(content)

        for field in link:
            URL = field['url']
            title=field['value'].encode("utf-8")
            if '/movies/' in URL:
                if name.lower() in title.lower():
                    if year in title:
                        self.GetFileHosts(URL, list, lock, message_queue)

                
    def crack(self,code):
            #Function written by D4Vinci
            zeros = ''
            ones = ''
            for n,letter in enumerate(code):
                    if n%2 == 0:
                            zeros += code[n]
                    else:
                            ones =code[n] + ones
            key = zeros + ones
            key = base64.b64decode(key.encode("utf-8"))
            return key[2:]
        

    def Resolve(self,url):
        
        import requests
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
        from entertainment import istream
            
        if 'bit.ly' in url:
                r = requests.get(url,headers=headers,allow_redirects=False)
                url = r.headers['location'] 
        if 'adf.ly' in url:
                adfly_data = requests.get(url).content
                ysmm = adfly_data.split("ysmm = \'")[1].split("\';")[0]
                url = crack(ysmm)
                
        
        return istream.ResolveUrl(url)
