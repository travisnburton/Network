##!/usr/bin/python3.6.3

import socket
# Create dictionary 
mydict = {}
inputpath = input('Provide path to input file (list of fqdn): ')
namefile = open(inputpath,"r")

for name in namefile:
    print('Checking ' + name)
    ip = socket.gethostbyname(name.strip())
    mydict.update({name.replace('.flexnet.net', '').strip().upper(): ip})
    #print(name + ip)

namefile.close()

for x , y in mydict.items():
    print('create ltm pool ' + x + '-WWW_POOL members add { ' + x + '-WWW:443 { address ' + y + ' }}')

for x in mydict:
    print('modify ltm data-group internal WEB_DG_BRIDGE records add {' + str.lower(x) + '.flexnet.net {data ' + x + '-WWW_POOL}}')


