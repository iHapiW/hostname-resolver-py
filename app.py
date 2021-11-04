# Importing Self-made Modules
from controller import control_socket as cs

# Importing argparse
import argparse

# Avoiding Pyc Files
import sys
sys.dont_write_bytecode = True


def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    
    # Add the arguments
    parser.add_argument("--dns-server", type=str)
    parser.add_argument("hostname", type=str)
    
    # Execute the parse_args() method
    args = parser.parse_args()
    
    dns_server = args.dns_server if args.dns_server else "8.8.8.8"
    hostname = args.hostname
    
    cs.get_ip(hostname, dns_server)


if __name__ == "__main__":
    main()
