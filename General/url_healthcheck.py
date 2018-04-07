#!/usr/bin/python
import requests
import socket

def url_healthcheck():
    list_of_names = input('Enter path to file containing list of domain names: ')
    namefile = open(list_of_names,"r")
    print('\nChecking list of domain names, only errors will be shown below')
    print('----------')
    for name in namefile:
        try:
            r = requests.get('https://' + name.strip(), timeout=7)
        except requests.exceptions.Timeout:
            print(name + ' timed out')
            print('----------')
        except requests.exceptions.RequestException:
            try:
                ip = socket.gethostbyname(name.strip())
            except socket.error:
                try:
                    ip = socket.gethostbyname('www.' + name.strip())
                    print(name + ' no CNAME for www')
                    print('----------')
                except socket.error:
                    print(name  + ' has no www record')
                    print('----------')
    namefile.close()
    print('Check complete \n')

url_healthcheck()
