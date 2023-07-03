import os
import socket
import requests
import colorama as c
import urllib.parse
import pandas as pd
from prettytable import PrettyTable
from requests_html import HTML
from requests_html import HTMLSession
from phonenumbers import geocoder, parse, carrier, timezone

c.init()
Banner = c.Fore.RED + """

   .----------------.  .----------------.  .----------------. 
  | .--------------. || .--------------. || .--------------. |
  | |      _       | || |    ______    | || |     __       | |
  | |     | |      | || |  .' ____ '.  | || |    /  |      | |
  | |  ___| |___   | || |  | (____) |  | || |    `| |      | |
  | | |___   ___|  | || |  '_.____. |  | || |     | |      | |
  | |     | |      | || |  | \____| |  | || |    _| |_     | |
  | |     |_|      | || |   \______,'  | || |   |_____|    | |
  | |              | || |              | || |              | |
  | '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------' 

""" + c.Style.RESET_ALL + c.Style.DIM +"""
                 * A Phone Number OSINT Tool *
""" + c.Style.RESET_ALL + c.Fore.GREEN +"""
                                                - Vai3hav.Sh
""" + c.Style.RESET_ALL 

def init_Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Banner)
init_Banner()

def Connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

if Connected():
    Target = input("Enter Phone Number with Contry Code: ")
    p = str(Target)

    # Parse & Print
    ParsedTarget = parse(Target, None)
    GeoTarget = geocoder.description_for_number(ParsedTarget, "en")
    carrierTarget = carrier.name_for_number(ParsedTarget, "en")
    timezoneTarget = str(timezone.time_zones_for_number(ParsedTarget))
    print(ParsedTarget)
    print("Origin: "+ GeoTarget)
    print("carrier: "+ carrierTarget)  
    print("TimeZone:"+ timezoneTarget+"\n\n")


    # Handy Methods

    def create_clickable_link(text, url):
        return f'\033]8;;{url}\033\\{text}\033]8;;\033\\'

    def get_source(url):
        try:
            session = HTMLSession()
            response = session.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(e)


    def parse_results(i):
        css_identifier_result = ".tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = ".yuRUbf a"
        css_identifier_text = ".VwiC3b"
        response = get_source("https://www.google.com/search?q=" + i)
        results = response.html.find(css_identifier_result)
        output = []
        for result in results:
            item = {
                'title': result.find(css_identifier_title, first=True).text,
                'link': result.find(css_identifier_link, first=True).attrs['href'],
                'text': result.find(css_identifier_text, first=True).text
            }
            output.append(item)
        #print(response)
        return output

    def listitup(res):
        x = PrettyTable()
        x.field_names = ["Title", "pre-text"]
        if res!=[]:
            print('\n')
            for q in res:    
                clickable_Title = create_clickable_link(q['title'], q['link'])
                x.add_row([clickable_Title, q['text'][:55]])
            return x
        else:
            return c.Fore.RED+'X'+c.Style.RESET_ALL
    # Scrappers

    def Social_Scrapper():
        sources=['facebook.com','linkedin.com','instagram.com','twitter.com']
        for source in sources:
            print(source, end=' ')
            print(listitup(parse_results('site:'+source+' intext:"'+p+'"')))

    def Nether_Scrapper():
        sources=['pastebin.com','github.com','whycall.me','locatefamily.com','spytox.com']
        for source in sources:
            print(source, end=' ')
            print(listitup(parse_results('site:'+source+' intext:"'+p+'"')))

    def Disposable_Scrapper():
        sources=[   'hs3x.com',
                    'receive-sms-now.com',
                    'smslisten.com',
                    'smsnumbersonline.com',
                    'freesmscode.com',
                    'catchsms.com',
                    'smstibo.com',
                    'smsreceiving.com',
                    'getfreesmsnumber.com',
                    'sellaite.com',
                    'receive-sms-online.info',
                    'receivesmsonline.com',
                    'receive-a-sms.com',
                    'sms-receive.net',
                    'receivefreesms.com',
                    'receive-sms.com',
                    'receivetxt.com',
                    'freephonenum.com',
                    'freesmsverification.com',
                    'receive-sms-online.com',
                    'smslive.co'
                ]
        for source in sources:
            disp=0
            if parse_results('site:'+source+' intext:"'+p+'"'):
                print(source, end=' ')
                print(listitup(parse_results('site:'+source+' intext:"'+p+'"')))
                disp=1
            else:                
                disp=0
        if disp==0:
            print('Not a Disposable number '+c.Fore.RED+'X'+c.Style.RESET_ALL)

    def Doc_Scrapper():
        print("Document Entry", end=' ')
        print(listitup(parse_results('(ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt | ext:xls) intext:"'+p+'"')))


    print(create_clickable_link('Truecaller','https://www.truecaller.com/search/in/'+p)+c.Fore.GREEN+' ✔'+c.Style.RESET_ALL)
    Social_Scrapper()
    Doc_Scrapper()
    Nether_Scrapper()
    Disposable_Scrapper()

else:
    print(c.Fore.RED +"NOT CONNECTED TO THE INTERNET, PLEASE CONNECT AND TRY AGAIN!"+ c.Style.RESET_ALL )
