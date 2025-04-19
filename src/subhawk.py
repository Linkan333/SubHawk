import argparse
import requests
import threading
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style

init()  # Initialize colorama

parser = argparse.ArgumentParser(
    description="SubHawk - A subdomain and website reconassiance tool for pentesters and bug bounty hunters.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-d", "--domain", help="Domain name usage: --domain example.com")
parser.add_argument("-w", "--wordlist", help="Path to the wordlist file usage: --worldlist /path/to/wordlist.txt")
parser.add_argument("-t", "--threads", help="Number of threads to use default is 5 and max is 100 usage: --default 5", default=5, type=int)
parser.add_argument("--user-agent", help="User agent to use for requests default is Mozilla/5.0 usage: --user-agent Mozilla/5.0", default="Mozilla/5.0")
parser.add_argument("-o", "--output", help="Output file to save results usage: --output /path/to/output.txt")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("--timeout", help="Timeout for requests is optional but could be useful avoiding request limiting usage: --timeout 5", type=int)
args = parser.parse_args()

banner = f"""{Fore.CYAN}
 ____        _     _   _                _    
/ ___| _   _| |__ | | | | __ ___      _| | __
\___ \| | | | '_ \| |_| |/ _` \ \ /\ / / |/ /
 ___) | |_| | |_) |  _  | (_| |\ V  V /|   < 
|____/ \__,_|_.__/|_| |_|\__,_| \_/\_/ |_|\_\
{Fore.YELLOW}
       -- Subdomain Discovery Tool --
          Created by Linkan333 🦅
{Fore.RED}
=========================================={Style.RESET_ALL}
"""

print(banner)

def subdomain_enum(subdomain, domain, timeout, verbose, output_file):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            result = f"Found: {url} (Status: {response.status_code})"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
    except requests.RequestException:
        if verbose:
            print(f"Failed: {url}")
        pass

def main():
    if args.domain is None:
        print("Domain name is required. Use --help for more information.")
        return
    if args.wordlist is None:
        print("Wordlist is required. Use --help for more information.")
        return
    
    timeout = args.timeout or 5
    num_threads = min(args.threads, 100)
    
    try:
        with open(args.wordlist, 'r') as f:
            subdomains = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Could not find wordlist file: {args.wordlist}")
        return
    
    
    print(f"Starting scan with {num_threads} threads...")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(
                subdomain_enum,
                subdomain,
                args.domain,
                timeout,
                args.verbose,
                args.output
            )
            for subdomain in subdomains
        ]
        
        for future in futures:
            future.result()
            
    print("Scan completed.")
    if args.output:
        print(f"Results saved to {args.output}")
        
        
if __name__ == "__main__":
    main()