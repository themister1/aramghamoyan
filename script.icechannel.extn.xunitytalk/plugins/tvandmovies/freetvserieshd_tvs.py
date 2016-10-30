'''
    Istream
    Oneclickwatch
    Copyright (C) 2013 Coolwave

    version 0.1

'''


from entertainment.plugnplay import Plugin
from entertainment import common

from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.xgoogle.search import GoogleSearch


class freetvserieshd(TVShowSource):
    implements = [TVShowSource]
	
    #unique name of the source
    name = "seriestv"
    source_enabled_by_default = 'true'
    #display name of the source
    display_name = "SERIESTV"
    
    #base url of the source website
    base_url = 'http://mobserep.com/'
    
    def GetFileHosts(self, url, list, lock, message_queue):
        import re

        from entertainment.net import Net
        net = Net(cached=False)

  

        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

        content = net.http_GET(url,headers=headers).content
        content = content.split('td-post-featured-video')[1]
        URL=re.compile(' src="(.+?)"',re.DOTALL).findall(content)[0].replace('https://','http://')

        host=URL.split('//')[1]
        host=host.split('/')[0]
     
        headers={'Referer':url,'Host':host,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
      
        content = net.http_GET(URL,headers=headers).content
   
        match=re.compile('"file":"(.+?)".+?"label":"(.+?)"',re.DOTALL).findall(content)
        for url , res in match:            
               
                res =res.upper().replace('hd','').replace('HD','')
                if not 'p' in res.lower():
                    res=res+'P'                
                if '480' in res:
                    res='HD'

 
                            
                self.AddFileHost(list, res, url)




    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):

        import urllib2
        import re
        from entertainment.net import Net

        from entertainment import bing
        net = Net(cached=False)
        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)


        search_term ='%s Season %s Episode %s' %(name,season,episode)

      
        
        new_url ='http://mobserep.com/?s='+search_term.replace(' ','+')

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                 'Referer': 'http://mobserep.com/'}
       

        html = net.http_GET(new_url,headers=headers).content

        html = html.split('item-details')

        for p in html:
            movie_url=re.compile('href="(.+?)"').findall(p)[0]
            TITLE=re.compile('title="(.+?)"').findall(p)[0]
 
            if search_term.lower() in TITLE.lower():
   

                
                self.GetFileHosts(movie_url, list, lock, message_queue)
                   

    def Resolve(self, url):

        UA='|Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8&Upgrade-Insecure-Requests=1&User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        
        
      
        if 'redirector.googlevideo' in url:
            import urllib
            url=urllib.urlopen(url).geturl()

            
        return url#+UA
