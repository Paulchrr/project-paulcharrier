import time
import dns.resolver
import requests
import json
import os
from emailfinder.extractor import *
import subprocess
from bs4 import BeautifulSoup


# ------------------------------------------------------------------ #
#Clé API (https://securitytrails.com)
securitytrails_API = "8GyuK9VwK6arR1SkVhBDlALrCWS9lKPo"

# ------------------------------------------------------------------ #
#Fonction qui demande à l'utilisateur le nom de domaine cible
def choose_domain():
    global domain_target
    domain_target = input("Indiquer le nom de domaine cible ? : ")

# ------------------------------------------------------------------ #
#Création du fichier contenant les résultats
def create_result():
    global newpath
    newpath = "result"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    def split_domain(nom_domaine):
        return nom_domaine.split('.')[0]

    global result_name, RESULT_FILE
    result_name = split_domain(domain_target)
    #global RESULT_FILE
    RESULT_FILE = os.path.join(newpath, result_name + '.txt')
    with open(RESULT_FILE, 'w') as f:
        f.write("")

#Affichage en print du fichier contenant les résultats
def print_result_file():
    with open(RESULT_FILE, 'r') as f:
        data = f.read()
        print(data)
# ------------------------------------------------------------------ #
#Fonction qui va chercher des mails à partir du nom de domaine donné par l'utilisateur
def search_mail():
    try : 
        result_google = get_emails_from_google(domain_target)
        result_bing = get_emails_from_bing(domain_target)
        result_baidu = get_emails_from_baidu(domain_target)
        with open(RESULT_FILE, 'a') as f:
            f.write(''+'\n')
            f.write("Les mails identifiés" + '\n' )
            f.write("-"*30 + '\n')
            print("\n Les mails identifiés" )
            print("-"*30 )
            print('\n')
            for i in result_google:
                print(i)
                f.write(i+'\n')
            for i in result_bing:
                print(i)
                f.write(i+'\n')
            for i in result_baidu:
                print(i)
                f.write(i+'\n')
    except:
        print("Le module search_mail() n'a pas fonctionné")
        pass

# ------------------------------------------------------------------ #
#Fonction qui sera utilisé pour executer des commandes en subprocess
def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    #output va être le résultat de notre commande
    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        #print(output)
        return output
    else:
        print('La commande à échoué')
        pass

# ------------------------------------------------------------------ #
#Fonction qui ajoute automatiquement le https.
    #Cette fonction est nécessaire car certaines fonctions utiliserons l'https.
def add_https(url):
    if not url.startswith("https://"):
        url = "https://" + url
    return url

# ------------------------------------------------------------------ #
#Fonction qui va nous afficher les dernières CVE 
    #L'api utilisé est https://cve.circl.lu/api/last/
    
def get_latest_cve(num_cve):
    url = f"https://cve.circl.lu/api/last/{num_cve}"
    response = requests.get(url)
    if response.status_code == 200:
        cves = response.json()
        #boucle qui va afficher les cve une par une. L'idée ici a été de travaillé un print en deux colonnes pour la lisibilité
        for i in range(0, len(cves), 2):
            cve1 = cves[i]
            cve2 = cves[i+1] if i+1 < len(cves) else None
            cve1_print = f"ID : {cve1['id']} Date :  {cve1['Published']}"
            cve2_print = f"ID : {cve2['id']} Date :  {cve2['Published']}" if cve2 else ""
            print("{:<50}{}{}".format(cve1_print, "  |  " if cve2 else "", cve2_print))
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
# ------------------------------------------------------------------ #

#Fonction qui check si un site est sur wordpress
def is_wordpress():
    output = execute(command="is_wordpress "+ domain_target)
    from random import randint
    import requests,json,re,time
    from bs4 import BeautifulSoup
    from colorama import Fore,init
    init()

    #Fonction qui va scanner un site wordpress
    def scan_wordpress():

        with open(RESULT_FILE,'a') as f:
            f.write("\n //Scanner WordPress \n")
            

            user_agent_list = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1","Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3","Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058","Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36","Roku4640X/DVP-7.70 (297.70E04154A)","Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)","AppleTV6,2/11.1","AppleTV5,3/9.1.1","Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US","Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586","Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)","Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2","Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU","Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)","Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)","Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+","Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"]
            RANDOM_USER_AGENT = user_agent_list[randint(0,52)]
            
            def user_finder(new_u) :

                new_url2 = new_u+'/wp-json/wp/v2/users'
                
                headers = {"user-agent":RANDOM_USER_AGENT}
                
                r2 = requests.get(new_url2,headers=headers)
                
                if r2.status_code == 200 :
                    print('\n[+] Enumerating usernames : \n')
                    time.sleep(1.3)
                    data = json.loads(r2.text)
                    for info in data :
                        f.write('\n[*] Username Found : {}'.format(info['slug']))
                        print(' [*] Username Found : {}'.format(info['slug']))
                        time.sleep(0.2)
                else :
                        print('\n[-] Usernames Not Found ')
            
            #fonction qui va trouver le panel d'admin du wordpress
            def adminpanel_finder(org_url) :
                
                urlA = org_url+'/wp-login.php?action=lostpassword&error=invalidkey'
                uagent = {"user-agent":RANDOM_USER_AGENT}
                
                r3 = requests.get(urlA,headers=uagent)

                if r3.status_code == 200 :
                    r3data = r3.text
                    pagesoup = BeautifulSoup(r3data,'html.parser')
                    ptag = pagesoup.findAll("p",{"id":"nav"})
                    
                    if len(ptag) > 0 :
                            for ptags in ptag :
                                for atags in ptags.find_all('a') :
                                    if 'Log in' in atags :
                                        admin_url = atags['href']
                                        print('\n[+] Admin panel found - ',admin_url)
                                        f.write('\n[+] Admin panel found - ',admin_url + '\n')

                                    else :
                                        f.write('\n[-] Admin panel not found')
                                        print('\n[-] Admin panel not found ')      
                    else :
                        print('\n[-] Admin panel not found ')
                        f.write('\n[-] Admin panel not found \n')
                        
                else :
                    print('\n[-] Admin panel not found ')
                    f.write('\n[-] Admin panel not found \n ')

            #print( '\nWebsite Url (with https://) : ', end="")
            url = add_https(domain_target)
            org_url = url
            roboturl = url+'/robots.txt'
            feedurl = url+'/feed'
            url = url+'/wp-json'

            headers = {"user-agent":RANDOM_USER_AGENT}
            f.write('\n')
            try:
                testreq = requests.get(org_url,headers=headers)
            except Exception as e:
                print('\nWebsite status : Error !')
                f.write('\nWebsite status : Error ! \n')
            else :
                print('\nWebsite status : Up')
                f.write("Website status : Up \n")
                f.write('\n')

                r = requests.get(url,headers=headers)
                rcode = r.status_code

                if rcode == 200 :

                    robotres = requests.get(roboturl,headers=headers)

                    if 'wp-admin' in robotres.text :
                        print('\n[+] WordPress Detection : ','Yes')
                        f.write("[+] WordPress Detection : Yes  \n")

                        feedres = requests.get(feedurl,headers=headers)
                        contents = feedres.text
                        soup = BeautifulSoup(contents,'xml')
                        wpversion = soup.find_all('generator')
                        if len(wpversion) > 0 :
                            wpversion = re.sub('<[^<]+>', "", str(wpversion[0])).replace('https://wordpress.org/?v=','')
                            print('\n[+] WordPress version : ',wpversion)
                            f.write("[+] WordPress version : " +wpversion)
                        else:
                            rnew = requests.get(org_url,headers=headers)
                            if rnew.status_code == 200 :
                                newsoup = BeautifulSoup(rnew.text,'html.parser')
                                generatorTAGS = newsoup.find_all('meta',{"name":"generator"})
                                for metatags in generatorTAGS :     
                                    if "WordPress" in str(metatags) :
                                        altwpversion = metatags['content']
                                        altwpversion = str(altwpversion).replace('WordPress','')
                                        print('\n[+] WordPress version : ',altwpversion)
                                        f.write("\n[+] WordPress version : " +wpversion)
                            else :
                                print('[-] WordPress version : Not Found !')
                                f.write('\n[-] WordPress version : Not Found ! ')
                        time.sleep(0.8)

                        data = json.loads(r.text)
                        siteName = data['name']
                        siteDesc = data['description']

                        plugins = data['namespaces']

                        print('\n[+] Webite name        :',siteName)
                        f.write('\n[+] Webite name        : '+siteName)
                        time.sleep(0.8)
                        f.write('\n')
                        print('\n[+] Webite description :',siteDesc)
                        f.write("\n[+] Webite description : "+ siteDesc)
                        time.sleep(0.8)
                        print('\n[+] Enumerating Plugins :',end=' ')
                        f.write('\n[+] Enumerating Plugins :')
                        plugins=list(set(plugins))
                        print('\n')
                        f.write('\n')
                        for i in plugins :
                            elem = (i[:i.find('/')])
                            print(' [*] ',elem) 
                            f.write('\n [*] '+ elem)
                            #f.write(elem)
                            time.sleep(0.2)
                        f.write('\n')
                        time.sleep(1)
                        adminpanel_finder(org_url)
                        time.sleep(1)
                        user_finder(org_url)

                    else :
                        print('\n[-] WordPress Detection : No')
                        f.write('\n[-] WordPress Detection : No')
                else :
                    print('\n[-] WordPress Detection : No')
                    f.write('\n[-] WordPress Detection : No')


    with open(RESULT_FILE,'a') as f:
        f.write(''+'\n')
        f.write("//Le site est-il un WordPress ?")
        print("Le site est-il un WordPress ?")
        f.write(''+'\n')
        if "None" in output:
            f.write("A priori le site n'est pas un wordpress" +'\n')
            print("A priori le site n'est pas un wordpress")
            pass
        else:
            print(output)
            f.write(output)
            print("Le site est un wordpress, voulez-vous éxecuter le scanner wordpress ? ")
            print("1: Oui")
            print("2: Non"+'\n')
            choix_scan = input("Indiquer 1 ou 2 : ")
            if choix_scan == "1":
                try: 
                    scan_wordpress()
                except:
                    print("Le scan n'a pas pu démarrer")

            elif choix_scan == "2":
                pass

            else:
                print("choix invalide")


# ------------------------------------------------------------------ #
 #Utilisation de DuckDuckGO pour les "google dorks". Voici le wiki : https://help.duckduckgo.com/duckduckgo-help-pages/results/syntax/
    # Doc utilisés : 
        #  https://www.makeuseof.com/duckduckgo-get-faster-results-search-operators/
        #  https://brettterpstra.com/2019/03/07/the-ultimate-guide-to-duckduckgo/
        
def dorks(domaine):
    #Le but de la fonction est d'aller chercher des fichiers pdf ou xls qui sont hébergé par le domaine ciblé
    def search_dorks(domaine, filetype):
        query = f'site:{domaine} filetype:{filetype}'
        url = f'https://duckduckgo.com/html?q={query}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', {'class': 'result__url'}, href=True)
        with open(RESULT_FILE, 'a') as f:
            f.write('\nFichier(s) '+ filetype + ' trouvé(s) \n')
            f.write("-"*30 + '\n')
            print('\nFichier(s) '+ filetype + ' trouvé(s)')
            print("-"*30 )
            for result in results:
                f.write(result['href'] + '\n')
                print(result['href'])

    try :
        search_dorks(domaine,"pdf")
        search_dorks(domaine,"xls")

    except:
        print("pas de documents trouvé")

    return 'Les résultats de la recherche ont été enregistrés dans le fichier resultat.txt'

# ------------------------------------------------------------------

#La fonction à pour but de réaliser un who is à partir du domaine indiqué.
#Nous utilisons l'API http://ipwhois.app/json
def auto_whois():
    import dns.resolver
    time.sleep(1)
    result = dns.resolver.resolve(domain_target)

    with open(RESULT_FILE,'a') as f:
        f.write("Résolution du nom" + '\n' )
        f.write("-"*30 + '\n')
        f.write(''+'\n')
        for ipval in result:
            inputIP = ipval.to_text()
            a = domain_target + " <==> " + inputIP
            f.write(a + '\n')

    def isIP(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    while True:
        if inputIP.count(".") == 3 and all(isIP(i) for i in inputIP.split(".")):
            response = requests.get("http://ipwhois.app/json/" + inputIP)
                # https://ipwhois.io/documentation

            if response.status_code == 200:
                ipwhois = json.loads(response.text)
                request_status = str(ipwhois["success"])
                str1 = request_status.strip()

                def result_whois():
                    ip = "IP:  " + ipwhois["ip"] + '\n'
                    type = "Type:  " + ipwhois["type"] + '\n'
                    country = "Country:  " + ipwhois["country"] + '\n'
                    country_code = "Country Code:  " + ipwhois["country_code"] + '\n'
                    region = "Region:  " + ipwhois["region"] + '\n'
                    city = "City:  " + ipwhois["city"] + '\n'
                    asn = "ASN:  " + ipwhois["asn"] + '\n'
                    organization = "Organization:  " + ipwhois["org"] + '\n'
                    isp = "ISP:  " + ipwhois["isp"] + '\n'
                    with open(RESULT_FILE,"a") as f :
                        f.write('\n')
                        f.write("Whois pour " + inputIP + "\n ")
                        f.write("-"*30 + '\n')
                        f.write(ip)
                        f.write(type)
                        f.write(country)
                        f.write(country_code)
                        f.write(region)
                        f.write(city)
                        f.write(asn)
                        f.write(organization)
                        f.write(isp)
                        print(ipwhois["success"])
                    with open(RESULT_FILE,"r") as f:
                        data = f.read()
                        print(data)

                if str1 == "True":
                    result_whois()
                else:
                    print(ipwhois["success"])
            else:
                print(response.raise_for_status)
            break
        else:
            print("\nError: Invalid IP Address.\n")
            continue
# ------------------------------------------------------------------ #

#La fonction à pour but de trouver les sous domaines à partir du domaine cible
#Nous utilons ici l'API securityTrails.com
def get_sub_domains(domain_target,RESULT_FILE):
    try :
        url_subdomain = "https://api.securitytrails.com/v1/domain/"+domain_target+"/subdomains"
        #print(url)
        querystring = {"children_only":"true"}
        headers = {
        'accept': "application/json",
        'apikey': securitytrails_API}
        response = requests.request("GET", url_subdomain, headers=headers, params=querystring)
        result_json=json.loads(response.text)
        sub_domains=[i+'.'+domain_target for i in result_json['subdomains']]
        
        #Nous allons ici écrire les résultats dans notre RESULT_FILE
        with open(RESULT_FILE,'a') as f:
            print("Les sous domaines")
            print(("-"*30 + '\n'))
            f.write(''+'\n')
            f.write("Les sous domaines" + '\n' )
            f.write("-"*30 + '\n')
            f.write(''+'\n')
            for i in sub_domains:
                print(i)
                f.write(i+'\n')
            return sub_domains
    except:
        print("Un problème avec le module des sous domaines, peux-être que la clé API a atteint son maximum de requêtes, dans ce cas veuillez actualiser la clé API securitytrails_API")
        pass
        
# ------------------------------------------------------------------ #

#Fonction qui va réaliser un NMAP avec les arguments -sV
def auto_nmap():
    options = ["Oui", "Non"]
    print("")
    print("Voulez-vous scanner la target (NMAP) ? :")
    for i, option in enumerate(options):
        print(f"{i + 1}: {option}")
    print("")
    response_reconnaissance = input("Veuillez entrer le numéro de l'option que vous souhaitez sélectionner: ")
    response_reconnaissance = int(response_reconnaissance) - 1

    selected_option = options[response_reconnaissance]
    global RESULT_NMAP
    RESULT_NMAP = os.path.join(newpath, result_name + '_nmap.txt')
    
    if selected_option == "Oui":
        print("")
        print("Démarrage de NMAP sur la target")
        print("")
        
        
        f = open(RESULT_NMAP, 'a')
        process = subprocess.Popen(('nmap', "-sV",domain_target ), stdout=f)

        while process.poll() is None:
            print("En cours")
            time.sleep(8)
            continue
        f.close()
        
        with open(RESULT_NMAP, 'r') as x:
            print_result = x.read()
            print(print_result)
    else:
        pass
# ------------------------------------------------------------------ #
#Fonction AUTO qui va appeler les autres fonctions utilisés par ce module
def auto():
    os.system('clear')
    print("""\

 █████╗ ██╗   ██╗████████╗ ██████╗  
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗ 
███████║██║   ██║   ██║   ██║   ██║ 
██╔══██║██║   ██║   ██║   ██║   ██║ 
██║  ██║╚██████╔╝   ██║   ╚██████╔╝ 
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  
                                    
███╗   ███╗ ██████╗ ██████╗ ███████╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝
██╔████╔██║██║   ██║██║  ██║█████╗  
██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                                    

        """)
    choose_domain()
    create_result()
    auto_whois()
    is_wordpress()
    auto_nmap()
    print("Tous les résultats sont stockés dans : " +'\n')
    print(RESULT_FILE)
    print(RESULT_NMAP)
    
# ------------------------------------------------------------------ #
#Fonction OSINT qui va appeler les autres fonctions utilisés par ce module
def osint():
    choose_domain()
    create_result()
    auto_whois()
    get_sub_domains(domain_target,RESULT_FILE)
    search_mail()
    dorks(domain_target)
    is_wordpress()
    print("\n Tous les résultats sont stockés dans : " +'\n')
    print(RESULT_FILE)
