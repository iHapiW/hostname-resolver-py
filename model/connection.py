import socket

from struct import pack, unpack
from collections import namedtuple

# Connection Handler
class Connection:

    # Initializing Connection Between DNS Server
    def __init__(self,dnsserver):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.connect((dnsserver,53))

    # Making DNS Query Packet
    def make_packet(self,hostname):

        # Setting Transaction ID : 3838 (self-made), Flags: 0100 (Standard Query) , Question Count (1) , Answer & Authoriy & Additional RRs (0)
        part1 = pack(">HHHHHH",0x3838,0x100,0x01,0x00,0x00,0x00)
        
        # Constructing Qname in DNS Query
        # format : example. \x06google\x03com\x00
        # bytes before every label includes byte counts of the label
        
        part2 = b""
        for label in hostname.split('.'):
            part2 += len(label).to_bytes(1,'little')
            part2 += bytes(label,"utf8")
        else: part2 += b"\x00"
        
        # Setting Type A, Class IN
        part3 = pack(">HH",0x01,0x01)
        
        # Returning Final Packet
        return part1+part2+part3
            
    def iopacket(self,packet):
        self.connection.send(packet)
        return self.connection.recv(1024)
    
    def analyze_packet(self,sent_packet,recieved_packet):
        # DNS Packet Structure : IP Packet + UDP + DNS Query + DNS Answer
        # DNS Answer = Whole Packet - (IP Packet + UDP + DNS Query) :
        dns_answer = recieved_packet[len(sent_packet):]
        
        # Unpacking DNS Answer to this format : (Qname, Type, Class, Data Length, Address Octet1, Address Octet2, Address Octet3, Address Octet4)
        record = unpack(">HhhIhBBBB",dns_answer)
        ip = (".".join(str(i) for i in record[-4:]),)
        record = record[:-4] + ip
        
        # Reconstruct DNS Answer Tuple to : (QName, Type, Class, Data length, Address)
        answer = namedtuple("Answer","qname type dns_class ttl data_length address")

        # Assign it to a Named Tuple and Return to Controller
        return answer._make(record)