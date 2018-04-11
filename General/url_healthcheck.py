import requests
import socket

def url_healthcheck():
    list_of_names = input('Enter path to file containing list of domain names: ')
    namefile = open(list_of_names,"r")
    print('\nChecking list of domain names, only errors will be shown below')
    print('----------')
    for name in namefile:
        try:
            requests.get('https://' + name.strip(), timeout=12)
        except requests.exceptions.Timeout:
            print(name + ' timed out')
            print('----------')
        except requests.exceptions.RequestException:
            try:
                socket.gethostbyname(name.strip())
            except socket.error:
                try:
                    socket.gethostbyname('www.' + name.strip())
                    print(name + ' no CNAME for www')
                    print('----------')
                except socket.error:
                    print(name  + ' has no www record')
                    print('----------')
    namefile.close()
    print('\nCheck complete \n')

url_healthcheck()
