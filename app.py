# Avoiding Pyc Files
import sys
sys.dont_write_bytecode = True

# Importing Text Formatting Files
import argparse

# Importing Self-made Modules
from controller import control_socket as cs

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument("--DNSServer", type=str)
    parser.add_argument("Hostname", type=str)
    
    # Execute the parse_args() method
    args = parser.parse_args()
    DNSServer = args.DNSServer if args.DNSServer else "8.8.8.8"
    Hostname = args.Hostname
    
    cs.get_ip(Hostname,DNSServer)
