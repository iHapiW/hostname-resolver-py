# Avoiding Pyc Files
import sys
sys.dont_write_bytecode = True

# Importing Text Formatting Files
import argparse

# Importing Self-made Modules
from controller import control_socket as cs

if __name__ == "__main__":
    
    # Parser Definition
    parser = argparse.ArgumentParser(
        prog='resolve',
        usage='%(prog)s [-d DNS-SERVER] hostname',
        description='Resolve Hostname & Get IP',
        allow_abbrev=False
    )

    # Arguments Definition
    parser.add_argument(
        "Hostname",
        help="Website Hostname",
        type=str,
        action="store"
    )
    
    parser.add_argument(
        "-d",
        "--dns",
        type=str,
        help="Insert DNS to look for IP",
        action="store",
        default="8.8.8.8",
        metavar="DNS IP"
    )

    # Parsing Arguments
    args = parser.parse_args()

    # Letting Controller , Control App :)
    DNSServer = args.dns
    Hostname = args.Hostname
    
    cs.get_ip(Hostname,DNSServer)
