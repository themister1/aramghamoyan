'''
    hdmovie_mvs_tvs.py
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment import common


class hdmoviefree(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "hdmoviefree"
    display_name = "HDMovieFree"

    base_url='https://www.hdmoviefree.org/'
    
    source_enabled_by_default = 'true'
    
    
    def GetFileHosts(self, url, list, lock, message_queue,ref):
        import re,json
        from entertainment.net import Net

        
        net = Net(cached=False)
        

        THE_URL='http://www.hdmoviefree.org/ajax/loadep/'+url
        

        data={'epid':url}
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.3','Referer':'http://www.hdmoviefree.org/'+ref,'Host':'hdmoviefree.org'}
       
        content = net.http_POST(THE_URL,data,headers=headers).content
      
        link=json.loads(content)

        DATA=link['link']
        try:
            for i in range(len(DATA['q'])):
                
                URL= DATA['l'][i]
                res= str(DATA['q'][i])+'P'

                self.AddFileHost(list, res, URL)
        except:
            DATA= DATA['embed']
            URL=re.compile('src="(.+?)"').findall(str(DATA))[0]
            self.AddFileHost(list, '720P', URL)            
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
        import re
        from entertainment.net import Net

        
        net = Net(cached=False)
        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)

        if len(episode)<2:
            episode = '0'+episode      

        search='http://www.hdmoviefree.org/search/%s.html' % name.replace(' ','-')

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.3','Referer':'http://hdmoviefree.org'}
     
        html = net.http_GET(search,headers=headers).content
       # #print html

        r ='class="play-center tooltip" href="(.+?)" title="(.+?) \|' 
        match=re.compile(r).findall(html)
      

        for URL ,TITLE in match:
            URL='http://www.hdmoviefree.org/'+URL
            ref=URL
            NAME = name.lower()
            if NAME in TITLE.lower():

                if year in TITLE:
 
                    id = URL.split('-')[-1].replace('.html','')

                    THE_URL ='http://www.hdmoviefree.org/ajax/loadsv/'+id
                    data={'id':id,'n':TITLE.replace('(','').replace('(','')}
                    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.3','Referer':URL,'Host':'hdmoviefree.org'}
     
                    content = net.http_POST(THE_URL,data,headers=headers).content
                  
                    match=re.compile('<a data-id="(.+?)" href="(.+?)">').findall(content)

                    for id, REF in match:
                        if type=='tv_episodes':
                            if 'season-' +season in REF:
                                if 'episode-' +episode in REF:
                                    self.GetFileHosts(id, list, lock, message_queue,REF)                                
                        else:        
                            self.GetFileHosts(id, list, lock, message_queue,REF)

                        

    #def Resolve(self, url):

        
       
            
        #return url

