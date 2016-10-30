'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment import common
import os



class onetwothree(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "123Movies"
    display_name = "123Movies"
    base_url = 'http://123movies.ru/'

    UA ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    
    profile_path = common.profile_path
    cookie_file = os.path.join(profile_path, 'cookies', '123movies.cookies')
    
    source_enabled_by_default = 'true'
    

    def random_generator(self,size=16):
            import random,string
            chars=string.ascii_lowercase + string.digits
            return ''.join(random.choice(chars) for x in range(size))

    def uncensored(self,a,b):
        import base64
        n = -1
        fuckme=[]
        #justshow=[]
        while True:
            
            if n == len(a)-1:
                break
            n +=1
           
            
            d = int(''.join(str(ord(c)) for c in a[n]))
          
            e=int(''.join(str(ord(c)) for c in b[n]))
            #justshow.append(d+e)
            fuckme.append(chr(d+e))
        #print justshow 
        return base64.b64encode(''.join(fuckme))

    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year,query):

        key = '87wwxtp3dqii'
        key2 = '7bcq9826avrbi6m49vd7shxkn985mhod'
        key3 = '7bcq9826avrbi6m4'

        REF=url

        from entertainment.net import Net
        from entertainment import cloudflare
        import re,json,hashlib,urllib
        net = Net(cached=False)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':'http://123movies.ru'}
        #print url
        try:
            LINK = net.http_GET(url,headers=headers).content
            net.save_cookies(self.cookie_file)
            #print '##########################'
            #print 'NET'             
        except:LINK = cloudflare.solve(url,self.cookie_file,self.UA,'8')
        
        try:movie_id = re.compile('name="movie_id" value="(.+?)"').findall(LINK)[0]
        except:movie_id = re.compile('id: "(.+?)"').findall(LINK)[0]
        #token = re.compile('player-token="(.+?)"').findall(LINK)[0]
        coookie_1 = hashlib.md5(movie_id+key).hexdigest()

        net.set_cookies(self.cookie_file)
        LOAD =net.http_GET('http://123movies.ru/ajax/v2_get_episodes/%s'%(movie_id),headers=headers).content
        LOAD=LOAD.replace('Episode 0','Episode ')
        link=LOAD.split('<div id="server-')
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':'http://123movies.ru'}
      
        for p in link:

            #try:
                
                res ='720P'
               
                    

                if type == 'tv_episodes':
                        
                        HTML=p.split('<a title="')
                        
                        for d in HTML:
                            try:
                           
                                if ' '+episode+':' in d.lower():
                                    
                                    #token = re.compile('hash="(.+?)"').findall(d)[0]
                                    SERVER=d.split('loadEpisode(')[1]
                                    server=SERVER.split(',')[0]
                                    episodeid=re.compile(',(.+?)\)').findall(SERVER)[0]
                                    key_gen = self.random_generator()
                                    COOKIE =  hashlib.md5(episodeid + key).hexdigest() + '=%s' %key_gen
                                    a= episodeid + key2
                                    b= key_gen
                                    i=b[-1]
                                    h=b[:-1]
                                    b=i+h+i+h+i+h
                                    token = urllib.quote(self.uncensored(a, b))
                                    if int(server) > 11:
                                        
                                        URL='http://123movies.ru/ajax/load_embed/%s' % (episodeid)
                                        if server=='99':
                                            HOST='CDN'
                                        if server=='14':
                                            HOST='OPENLOAD.CO'
                                        if server=='13':
                                            HOST='VIDEOMEGA.TV'
                                        if server=='12':
                                            HOST='VIDEOWOOD.TV'

                                        change=True    
                                    else:
                                        URL='http://123movies.ru/ajax/v2_get_sources/%s?hash=%s' % (episodeid,token)
                                        change=False

                                    HEADERS={'Accept-Encoding':'gzip, deflate, sdch','x-requested-with':'XMLHttpRequest','Cookie':COOKIE,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':REF}
               
                                    net.set_cookies(self.cookie_file)
                                    HTML1=net.http_GET(URL,headers=HEADERS).content
                                
                                    
                                    
                                    try:

                                        if change:
                                            HTML2 = json.loads(HTML1)
                                            FINAL_URL = HTML2['embed_url']
                                            if '720p' in FINAL_URL.lower():
                                                res='720P'
                                            if '1080p' in FINAL_URL.lower():
                                                res='1080P'
                                            else:
                                                res='720P'                                                

                                                self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())

                                        if not change:       
                                            HTML2 = json.loads(HTML1)
                                            DATA=HTML2['playlist'][0]['sources']
                                            for field in DATA:
                                                FINAL_URL= field['file']
                                                res= field['label']#.upper()
                                            
                                            #if 'google' in FINAL_URL or 'blogspot' in FINAL_URL or '123movies.ru' in FINAL_URL:                             
                                                if not '.srt' in FINAL_URL:
                                                    res=res.replace('p','').replace('P','').replace('CAM','360')
                                                    if not res.isdigit():
                                                        res='720'
                                                    #print res
                                                    #res=int(res)
                                                    #print res
                                                    if res =='360':
                                                        res='SD'
                                                    if res =='480':
                                                        res='DVD'
                                                    if res =='720':
                                                        res='720P'
                                                    if res =='1080':
                                                        res='1080P'
                                                      

                                                    HOST=FINAL_URL.split('//')[1]
                                                    HOST=HOST.split('/')[0]  
                                                    

                                                    

                                                    self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())                            
                                    except:pass
                            except:pass                                    
                else:
                        HTML=p.split('<a title="')
                        
                        for d in HTML:
                            try:                                
                                YEAR=re.compile('Release:</strong>(.+?)<').findall(LINK)[0].strip()
                                THETITLE=re.compile('"og:title" content="(.+?)"').findall(LINK)[0].strip()
                                SERVER=d.split('loadEpisode(')[1]
                                server=SERVER.split(',')[0]
                                episodeid=re.compile(',(.+?)\)').findall(SERVER)[0]
                                key_gen = self.random_generator()
                                COOKIE =  hashlib.md5(episodeid + key).hexdigest() + '=%s' %key_gen
                                a= episodeid + key2
                                b= key_gen
                                i=b[-1]
                                h=b[:-1]
                                b=i+h+i+h+i+h
                                token = urllib.quote(self.uncensored(a, b))
                                if int(server) > 11:
                                    
                                    URL='http://123movies.ru/ajax/load_embed/%s' % (episodeid)
                                    if server=='99':
                                        HOST='CDN'
                                    if server=='14':
                                        HOST='OPENLOAD.CO'
                                    if server=='13':
                                        HOST='VIDEOMEGA.TV'
                                    if server=='12':
                                        HOST='VIDEOWOOD.TV'

                                    change=True    
                                else:
                                    URL='http://123movies.ru/ajax/v2_get_sources/%s?hash=%s' % (episodeid,token)
                                    change=False

                                HEADERS={'Accept-Encoding':'gzip, deflate, sdch','x-requested-with':'XMLHttpRequest','Cookie':COOKIE,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':REF}
               
                                if not year:
                                    if query.lower() in THETITLE.lower():
                                        PASS=True
                                else:        
                                    if year == YEAR:
                                        PASS=True
                                if PASS==True:
                                    net.set_cookies(self.cookie_file)
                                    HTML=net.http_GET(URL,headers=HEADERS).content
                                    try:  

                                        if change:
                                            HTML1 = json.loads(HTML)
                                            FINAL_URL = HTML1['embed_url']

                                            if '720p' in FINAL_URL.lower():
                                                res='720P'
                                            if '1080p' in FINAL_URL.lower():
                                                res='1080P'
                                            else:
                                                res='720P'                                                

                                                self.AddFileHost(list, res, FINAL_URL,host=HOST.upper())

                                        if not change:       
                                                HTML2 = json.loads(HTML)
                                                DATA=HTML2['playlist'][0]['sources']
                                                for field in DATA:
                                                    FINAL_URL= field['file']
                                                    res= field['label']#.upper()
                                                
                                                #if 'google' in FINAL_URL or 'blogspot' in FINAL_URL or '123movies.ru' in FINAL_URL:                             
                                                    if not '.srt' in FINAL_URL:
                                                        res=res.replace('p','').replace('P','').replace('CAM','360')
                                                        if not res.isdigit():
                                                            res='720'
                                                        #print res
                                                        #res=int(res)
                                                        #print res
                                                        if res =='360':
                                                            res='SD'
                                                        if res =='480':
                                                            res='DVD'
                                                        if res =='720':
                                                            res='720P'
                                                        if res =='1080':
                                                            res='1080P'
                                                          

                                                        HOST=FINAL_URL.split('//')[1]
                                                        HOST=HOST.split('/')[0]  
                                                        

                                                        

                                                        self.AddFileHost(list, res, FINAL_URL,host=HOST.upper()) 
                                    except:pass
                            except:pass



            
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net

        import re

        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        query = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':'http://123movies.ru'}
                
        url='http://123movies.ru/movie/search/' + str(query).replace(' ','+')
        #print url
        try:
           net.set_cookies(self.cookie_file)
           LINK=net.http_GET(url,headers=headers).content
           net.save_cookies(self.cookie_file)
           print 'CLOUDFLARE BYPASSED'
        except:
           from entertainment import cloudflare
           LINK = cloudflare.solve(url,self.cookie_file,self.UA,'8')
                              
        LINK = LINK.split('"ml-item">')
        for p in LINK:
            try:
               movie_url=re.compile('a href="(.+?)"',re.DOTALL).findall(p)[0]
               name=re.compile('title="(.+?)"',re.DOTALL).findall(p)[0]
               iconimage=re.compile('img data-original="(.+?)"',re.DOTALL).findall(p)[0]           

               movie_url=movie_url+'watching.html'
               if type == 'tv_episodes':
                   if query.lower() in name.lower():                
                       if 'Season '+season in name:
                           self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year,query)
                        
               else:
                   if query.lower() in name.lower():
                       self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year,query)

            except:pass

                    
            
    def Resolve(self, url):
       url=url.replace('amp;','')
       if 'streaming.fshare' in url or 'redirector.googlevideo' in url or 'googleusercontent' in url:
          import urllib2 
          headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Referer': 'http://123movies.ru'}
          req = urllib2.Request(url, headers=headers) 
          url = urllib2.urlopen( req )  .geturl()    
          return url
       else:  
            from entertainment import istream
            return istream.ResolveUrl(url)
            
                
                
