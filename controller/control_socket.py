import socket
import struct

from model.stdio import error, success, warning
from model import connection as c

#Connection Model Handler
def get_ip(hostname : str, dnsserver : str):
    try:
        connection = c.connection(dnsserver)
        packet = connection.make_packet(hostname.strip())
        result = connection.iopacket(packet)
        answer = connection.analyze_packet(packet,result)
        success(f"""{{
    ---DNS Answer Recieved----
    Type = {answer.type}
    Class = {answer.dns_class}
    TTL = {answer.ttl}
    Address = {answer.address}
}}""")
    except socket.gaierror:
        error("Cannot Access DNS Server!")
    except struct.error:
        warning("Invalid Host")