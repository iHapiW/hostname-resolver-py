from socket import gaierror
from struct import error

from model.stdio import error, success
from model import connection as c

#Connection Model Handler
def get_ip(hostname : str, dnsserver : str):
    try:
        connection = c.connection(dnsserver)
        packet = connection.make_packet(hostname.strip())
        result = connection.iopacket(packet)
        answer = connection.analyze_packet(packet,result)
        success("Host Found",f"""{{
    Type = {answer.type}
    Class = {answer.dns_class}
    TTL = {answer.ttl}
    Address = {answer.address}
}}
""")
    except gaierror:
        error("Invalid DNS")
    except error:
        error("Host Not Found")