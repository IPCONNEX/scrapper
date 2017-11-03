#! /usr/bin/python3.6

__author__ = 'RicardoMoya'

import time
import urllib
import urllib.request
import urllib.error
from stem import Signal
from stem.control import Controller


class ConnectionManager:
    def __init__(self):
        self.new_ip = "0.0.0.0"
        self.old_ip = "0.0.0.0"
        self.new_identity()

    @classmethod
    def _get_connection(self):
        """
        TOR new connection
        """
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            # controller.authenticate(password="houghton")
            controller.signal(Signal.NEWNYM)
            controller.close()

    @classmethod
    def _set_url_proxy(self):
        """
        Request to URL through local proxy
        """
        proxy_support = urllib.request.ProxyHandler({"socks5": "127.0.0.1:9050"})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    @classmethod
    def req(self, url):
        """
        TOR communication through local proxy
        :param url: web page to parser
        :return: request
        """

        try:
            self._set_url_proxy()
            req = urllib.request.Request(url, None, {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) "
                              "AppleWebKit/535.11 (KHTML, like Gecko) "
                              "Ubuntu/10.10 Chromium/17.0.963.65 "
                              "Chrome/17.0.963.65 Safari/535.11"})
            req = urllib.request.urlopen(req)
            return req
        except urllib.error.HTTPError as e:
            return e.read()

    def new_identity(self):
        """
        new connection with new IP
        """
        # First Connection
        if self.new_ip == "0.0.0.0":
            self._get_connection()
            self.new_ip = self.req("http://icanhazip.com/").read().decode('utf-8')
        else:
            self.old_ip = self.new_ip
            self._get_connection()
            self.new_ip = self.req("http://icanhazip.com/").read().decode('utf-8')

        seg = 0

        # If we get the same ip, we'll wait 5 seconds to request a new IP
        while self.old_ip == self.new_ip:
            time.sleep(5)
            seg += 5
            print ("Waiting to obtain new IP: %s Seconds" % seg)
            self.new_ip = self.req("http://icanhazip.com/").read().decode('utf-8')

        print ("New connection with IP: %s" % self.new_ip)