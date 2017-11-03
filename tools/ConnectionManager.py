import requests, time
from stem.control import Controller
from stem import Signal


class ConnectionManager:

    def __init__(self):
        self.ip = '0.0.0.0'
        self.old_ip = '0.0.0.0'
        self._iter = 0
        self.new_identity()
        local_proxy = 'socks5://127.0.0.1:9050'
        proxies = {'http': local_proxy, 'https': local_proxy}

    def _my_ip(self):
        local_proxy = 'socks5://127.0.0.1:9050'
        proxies = {'http': local_proxy, 'https': local_proxy}
        current_ip = requests.get(url='http://icanhazip.com', proxies=proxies, verify=False)
        return current_ip.text.splitlines()[0]

    def new_identity(self):
        # increment iter until it reaches 10 or so to limit the change of IPs
        # self._iter += 1

        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            controller.close()
        self.ip = self._my_ip()
        print('IP changed from ' + self.old_ip + ' to ' + self.ip)
        self.old_ip = self.ip

        # if the change of IP is Due, than you reset iter to 0


# WORKING BLOCK


'''

http_proxy = {
        'http': local_proxy,
        'https': local_proxy
}



# Start with a 1 element as argument

# request the url and scrap it

# Returns a list of found links + fill in the data in the database





current_ip = requests.get(
        url='http://icanhazip.com',
        proxies=http_proxy,
        verify=False
)

ip = current_ip
print(current_ip.text)

time.sleep(5)

new_ip = current_ip

while ip == new_ip:
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        # controller.authenticate(password="houghton")
        controller.signal(Signal.NEWNYM)
        controller.close()
    time.sleep(5)

    new_ip = requests.get(
            url='http://icanhazip.com',
            proxies=http_proxy,
            verify=False
    )

print(new_ip.text)


'''




# To be ignored for now


"""
import socks, socket, requests
from stem import Signal
from stem.control import Controller

def set_new_ip():
        with Controller.from_port(port=9050) as Controller:
                controller.signal(Signal.NEWNYM)

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket

print (requests.get("http://icanhazip.com").text)

set_new_ip()

print(requests.get("http://icanhazip.com").text)
"""