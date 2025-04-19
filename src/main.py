import argparse
import requests
import threading
import time

parser = argparse.ArgumentParser(
    description="SubHawk - A subdomain and website reconassiance tool for pentesters and bug bounty hunters.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-d", "--domain", help="Domain name usage: --domain example.com")
parser.add_argument("-w", "--wordlist", help="Path to the wordlist file usage: --worldlist /path/to/wordlist.txt")
parser.add_argument("-t", "--threads", help="Number of threads to use default is 5 usage: --default 5", default=5, type=int)
parser.add_argument("--user-agent", help="User agent to use for requests default is Mozilla/5.0 usage: --user-agent Mozilla/5.0", default="Mozilla/5.0")
parser.add_argument("-o", "--output", help="Output file to save results usage: --output /path/to/output.txt")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("--timeout", help="Timeout for requests is optional but could be useful avoiding request limiting usage: --timeout 5", type=int)
args = parser.parse_args()


def main():
    if args.domain is None:
        print("Domain name is required. Use --help for more information.")
        return
    
    if args.domain is not None:
        validate = requests.get(f"http://{args.domain}")
        validate2 = requests.get(f"https://{args.domain}")
        if validate.status_code == 200 or validate2.status_code == 200:
            pass
        else:
            print(f"Domain {args.domain} is not a valid domain.")
            return
        
    if args.wordlist is not None:
        try:
            with open(args.wordlist, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    word = line.strip()
                    if args.verbose:
                        print(f"Trying {word}...")
                        print(f"http(s)://{word}.{args.domain}")
                    else:
                        print(f"Trying {word}...")
        except FileNotFoundError:
            print(f"Wordlist file {args.wordlist} not found.")
            return
    if args.wordlist is None:
        print("Wordlist is required. Use --help for more information.")
        return


main()