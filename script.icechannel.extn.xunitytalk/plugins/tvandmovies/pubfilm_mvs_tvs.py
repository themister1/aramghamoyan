'''
    Cartoon HD    
    Copyright (C) 2013 Mikey1234
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin



class pubfilm(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "PubFilm"
    display_name = "PubFilm"
    base_url = 'http://pubfilm.com/'
   
    source_enabled_by_default = 'true'

                
    
    def GetFileHosts(self, url, list, lock, message_queue,type,season,episode):

        import re
        from entertainment.net import Net
        net = Net(cached=False)
        
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
              'Referer': 'http://pubfilm.com'}


        content = net.http_GET(url,headers=headers).content

        headers={'Host': 'player.pubfilm.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': url,
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'en-US,en;q=0.8'}



        match=re.compile('href="http://player.pubfilm.com/(.+?)".+?value="(.+?)"',re.DOTALL).findall(content)
        
        for URL , EP in match:
            URL='http://player.pubfilm.com/'+URL
            EPISODE=EP.replace('EPISODE','').replace('episode','').replace('SERVER','').replace('server','').replace(':','').strip()
            



            if type == 'tv_episodes':
                EPISODE=int(EPISODE)
                if int(season)==EPISODE:
                    CONTENT = net.http_GET(URL,headers=headers).content
                    MATCHED=re.compile('file":"(.+?)".+?label":"(.+?)"').findall(CONTENT)
                  
                    for FINAL_URL , quality in MATCHED:
                        quality=quality.upper()   
                        if quality == '1080P':
                            quality ='1080P'
                        elif quality == '720P':
                            quality ='720P'                
                        elif quality == '480P':
                            quality ='HD'
                        else:
                            quality ='SD'

                        HOST= FINAL_URL.split('//')[1]
                        HOST= HOST.split('/')[0]
                        self.AddFileHost(list, quality, FINAL_URL,host=HOST.upper())
                    
            else:
                CONTENT = net.http_GET(URL,headers=headers).content

                MATCHED=re.compile('file":"(.+?)".+?label":"(.+?)"').findall(CONTENT)
              
                for FINAL_URL , quality in MATCHED:
                    quality=quality.upper()   
                    if quality == '1080P':
                        quality ='1080P'
                    elif quality == '720P':
                        quality ='720P'                
                    elif quality == '480P':
                        quality ='HD'
                    else:
                        quality ='SD'

                    HOST= FINAL_URL.split('//')[1]
                    HOST= HOST.split('/')[0]
                    self.AddFileHost(list, quality, FINAL_URL,host=HOST.upper())
        
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
      import re
      from entertainment.net import Net
      net = Net(cached=False)
      
      name=name.lower()

      headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
              'Referer': 'http://pubfilm.com'}


      new_url='http://pubfilm.com/?s=' +name.replace(' ','+')
      content = net.http_GET(new_url,headers=headers).content

      matched=re.compile('<h3 class="post-box-title"><a href="(.+?)" rel="bookmark">(.+?)</a>').findall(content)
      for URL, TITLE in matched:
              
          if type == 'tv_episodes':
            if name.lower() in TITLE.lower():
              if season in TITLE.lower():
                self.GetFileHosts(URL, list, lock, message_queue,type,season,episode)
        
          else:
            if name.lower() in TITLE.lower():
              if year in TITLE.lower():  
                self.GetFileHosts(URL, list, lock, message_queue,type,season,episode)
               
       

                

    def Resolve(self, url):                 
        url=url.replace('amp;','')
            
        if 'google' in url or 'blogspot' in url:
            if 'googleusercontent.com' in url or 'redirector' in url:
                import urllib
                page = urllib.urlopen(url)
                resolved=page.geturl()
                if 'requiressl=yes' in resolved:
                    resolved=resolved.replace('http://','https://')
                
            else:
                 if 'requiressl=yes' in url:
                     url=url.replace('http://','https://')
                 resolved=url
            

        else:
        
            from entertainment import istream
            resolved =istream.ResolveUrl(url)
        return resolved  









            
