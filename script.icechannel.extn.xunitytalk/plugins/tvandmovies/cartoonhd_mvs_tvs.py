'''
    Cartoon HD    
    Copyright (C) 2013 Mikey1234
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment import common
import os

class cartoonhd(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "Cartoon HD"
    display_name = "Cartoon HD"
    base_url = 'http://cartoonhd.website/'
   
    source_enabled_by_default = 'true'

    cookie_file = os.path.join(common.cookies_path, 'cartoonhd.cookie')            
    
    def GetFileHosts(self, url, list, lock, message_queue,type,domain,cookie,year):

        import re,time,base64
        from entertainment.net import Net
        net = Net(cached=False)
     


        YEARWAY=url.replace('bollox-','')
        url=url.replace('%s-'%year,'')
        host=domain.split('//')[1]        

        headers={'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.8',
                'Cache-Control':'no-cache',
                'Connection':'keep-alive',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':host,
                'Origin':domain,
                'Pragma':'no-cache',
                'Referer':domain,
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}
        
        #cookie=net.get_cookies()
        #print cookie
        #print '###########################################'
        #print url
        net.save_cookies(self.cookie_file)
        #COOKIE=re.compile('__utmx="(.+?)"').findall(open(self.cookie_file).read())[0]
        #print COOKIE
        net.set_cookies(self.cookie_file)                         
     
   
        content = net.http_GET(domain+url,headers=headers).content
        if '%TITLE% (%YEAR%)' in content:
            
            content = net.http_GET(domain+YEARWAY,headers=headers).content    
        TIME = time.time()- 3600
  
        TIME= str(TIME).split('.')[0]
  
        TIME= base64.b64encode(TIME,'strict')
 
        TIME=TIME.replace('==','%3D%3D')
        
        token=re.compile("var tok.+?'(.+?)'").findall(content)[0]        
        match=re.compile('elid.+?"(.+?)"').findall(content)
        id = match[0]
        #COOKIE='flixy=%s; %s=%s' % (token,id,TIME)

        headers={'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.8',
                'Cache-Control':'no-cache',
                'Connection':'keep-alive',
                'Content-Length':'94',
                #'Cookie':COOKIE,
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':host,
                'Origin':domain,
                'Pragma':'no-cache',
                'Referer':url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}
                #'Authorization': 'Bearer '+COOKIE.replace('%3D','=')


        if type == 'tv_episodes':
            get='getEpisodeEmb'
        else:
            get='getMovieEmb'

        new_search=domain+'/ajax/nembeds.php'

        data={'action':get,'idEl':id,'token':token,'elid':TIME}
   
        import requests
        content = requests.post(new_search, data=data, headers=headers).content
        #print content

    

        quality ='HD'

            
        r = 'iframe src="(.+?)"' #% option
        #print r
        FINAL  = re.compile(r,re.IGNORECASE).findall(content.replace('\\',''))
        for FINAL_URL in FINAL:
            self.AddFileHost(list, quality, FINAL_URL.split('"')[0])
    
        
        
                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):                 
  
      domain,cookie = self.GetDomain()
      name=name.lower()
      
      if type == 'tv_episodes':
        name=name.lower()
        item_url = '/watch-%s-%s-online-stream-full-episodes/season/%s/episode/%s' %(name.replace(' ','-'),year,season,episode)
        self.GetFileHosts(item_url, list, lock, message_queue,type,domain,cookie,year)
      else:
        if not year:
            year='bollox'
        item_url = '/%s-%s-online-free-putlocker-live' % (name.replace(' ','-'),year)    
        #print item_url
        self.GetFileHosts(item_url, list, lock, message_queue,type,domain,cookie,year)
           
       


    def GrabMailRu(self,url,list):
        #print url
        
        from entertainment.net import Net
        net = Net(cached=False)

        
        import json,re
        items = []

        data = net.http_GET(url).content
        cookie = net.get_cookies()
        for x in cookie:

             for y in cookie[x]:

                  for z in cookie[x][y]:
                       
                       l= (cookie[x][y][z])
                       
        r = '"key":"(.+?)","url":"(.+?)"'
   
        match = re.compile(r,re.DOTALL).findall(data)
        for quality,stream in match:
            test = str(l)
            test = test.replace('<Cookie ','')
            test = test.replace(' for .my.mail.ru/>','')
            url=stream +'|Cookie='+test
            Q=quality.upper()
            if Q == '1080P':
                Q ='1080P'
            elif Q == '720P':
                Q ='720P'                
            elif Q == '480P':
                Q ='HD'
            else:
                Q ='SD'                
            self.AddFileHost(list, Q, url,host='MAIL.RU') 


    def GetDomain(self):                 
        
        from entertainment.net import Net
        net = Net(cached=False)

        try:
            headers={'Accept':'application/json, text/javascript, */*; q=0.01',
                    'Accept-Encoding':'gzip, deflate',
                    'Accept-Language':'en-US,en;q=0.8',
                    'Cache-Control':'no-cache',
                    'Connection':'keep-alive',
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host':'cartoonhd.website',
                    'Origin':'http://cartoonhd.website',
                    'Pragma':'no-cache',
                    'Referer':'http://cartoonhd.website',
                    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
                    'X-Requested-With':'XMLHttpRequest'}

            cookie = net.http_GET('http://cartoonhd.website/',headers=headers).content
            domain='http://cartoonhd.website'
        except:
            try:              
                headers={'Accept':'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'en-US,en;q=0.8',
                        'Cache-Control':'no-cache',
                        'Connection':'keep-alive',
                        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                        'Host':'cartoonhd.tv',
                        'Origin':'http://cartoonhd.tv',
                        'Pragma':'no-cache',
                        'Referer':'http://cartoonhd.tv',
                        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
                        'X-Requested-With':'XMLHttpRequest'}

                cookie = net.http_GET('http://cartoonhd.tv/',headers=headers).content
                domain='http://cartoonhd.tv'
            except:
                headers={'Accept':'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'en-US,en;q=0.8',
                        'Cache-Control':'no-cache',
                        'Connection':'keep-alive',
                        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                        'Host':'www.cartoonhd.mobi',
                        'Origin':'http://www.cartoonhd.mobi',
                        'Pragma':'no-cache',
                        'Referer':'http://www.cartoonhd.mobi',
                        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
                        'X-Requested-With':'XMLHttpRequest'}

                cookie = net.http_GET('http://www.cartoonhd.mobi/',headers=headers).content
                domain='http://www.cartoonhd.mobi'                    
        return domain , cookie                    

                

    def Resolve(self, url):                 

            
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









            
