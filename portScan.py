#!/bin/python

import optparse
import socket
from socket import *


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('arch.nerth.net\r\n')
        results = connSkt.recv(100)
        print('\n[+]\t{}/tcp open\n').format(tgtPort)
        print('\n[+]\t' + str(results))
        connSkt.close()
    except:
        print('\n[-]\t{}/tcp closed\n').format(tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('\n[-]\tCannot resolve {}: Unknown host\n').format(tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+]\tScan Results for ' + tgtName[0])
    except:
        print('\n[+]\tScan Results for ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('\nScanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser('usage %prog -H '+\
                                   '<target host> -p <target port>')
    parser.add_option('-H',dest='tgtHost', type='string',\
                      help='specify target host')
    parser.add_option('-p',dest='tgtPort', type='string',\
                      help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__=='__main__':
    main()