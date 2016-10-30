'''
    movieshd
    Copyright (C) 2014 Coolwave
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay import Plugin
from entertainment import common
import os

do_no_cache_keywords_list = ['Sorry for this interruption but we have detected an elevated amount of request from your IP']

class movieshd(MovieSource):
    implements = [MovieSource]
    
    name = "MoviesHD"
    display_name = "MoviesHD"
    cookie_file = os.path.join(common.cookies_path, 'MoviesHD')
    source_enabled_by_default = 'true'
    
    def GetFileHosts(self, url, list, lock, message_queue):
        import re
        from entertainment.net import Net
        net = Net(cached=False)
   
        content = net.http_GET(url).content

        SITES= ['<b>Google</b>','<b>Openload</b>']

        for site in SITES:
            link=content.split(str(site))
            for p in link:

                url = re.compile(' src="(.+?)"').findall(p)[0]

                HOST=url.split('//')[1]
                HOST=HOST.split('/')[0]              
                res='720P'
                if not 'cloudflare' in url:
                    self.AddFileHost(list, res, url,host=HOST.upper())
                    
        content=content.split('<table id="source_table"')[1]                
        LINK=content.split('<td><img src="')

        for p in link:
            url=re.compile('<a href="(.+?)"').findall(p)[0]
            HOST=re.compile('target=".+?">(.+?)<').findall(p)[0]
            res =re.compile('<td>(.+?)</td>').findall(p)[0]
            if not 'RATING' in res.upper():
                self.AddFileHost(list, res.upper(), url,host=HOST.upper())
            
            
               
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):
        import re
        from entertainment.net import Net
        
        net = Net(cached=False)


        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)

        content = net.http_GET('http://movieshd.tv/?s=%s'%name.replace(' ','+')).content

        link=content.split('class="entry-title">')

        for p in link:
            url=re.compile('<a href="(.+?)"').findall(p)[0]
            _name=re.compile('title="(.+?)">').findall(p)[0]           
            if name.lower() in _name.lower():
                if year in _name.lower():
                    #print 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
                    self.GetFileHosts(url, list, lock, message_queue)
                

                    
    
    def Resolve(self, url):
        url=url.replace('#038;','')
        if 'redirector.googlevideo' in url:
            if 'requiressl=yes' in url:
                url=url.replace('http://','https://')
            import urllib
            resolved=urllib.urlopen(url).geturl()
        
            

        else:
        
            from entertainment import istream
            resolved =istream.ResolveUrl(url)
        return resolved  
