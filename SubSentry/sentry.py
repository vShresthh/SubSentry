import logging
import re
from utils import enum, dns_checker, validator, reporter
import pyfiglet

# Setting up logging configuration
logging.basicConfig(
    filename='scanner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def print_banner():
    banner = pyfiglet.figlet_format("SubSentry", font="ansi_shadow")
    print("*" * 78)
    print(banner.strip())
    print("Subdomain Takeover Scanner + Validator".center(65))
    print("by @vshresthh".center(65))
    print("*" * 78)


def main():
    try:
        # Print banner without logging it
        print_banner()
        
        # Domain input
        domain = input("Enter the domain to scan: ").strip()
        if not domain:
            logging.warning("No domain entered. Exiting.")
            print("[!] No domain entered. Exiting.")
            return

        # Validate domain format
        if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
            logging.warning("Invalid domain format.")
            print("[!] Invalid domain format. Exiting.")
            return
        
        logging.info(f"Starting subdomain takeover scan for {domain}")
        print(f"[+] Starting subdomain takeover scan for {domain}\n")
        
        # Enumerating subdomains
        subdomains = enum.run_enum(domain)
        logging.info(f"Found {len(subdomains)} subdomains")
        print(f"[+] Found {len(subdomains)} subdomains.\n")
        
        # Checking CNAME records
        cname_targets = dns_checker.check_cnames(subdomains)
        logging.info(f"Found {len(cname_targets)} potential CNAME targets")
        print(f"[+] Found {len(cname_targets)} potential CNAME targets.\n")
        
        # Validating potential takeover targets
        results = validator.validate(cname_targets)
        
        # Generating report
        reporter.generate_report(results)
        
        logging.info("Scan completed successfully.")
        print("\n[✓] Scan completed. Check 'report.json' and 'report.md' for details.")

    except KeyboardInterrupt:
        logging.warning("Scan interrupted by user.")
        print("\n[!] Scan interrupted by user. Exiting.")

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        print(f"[!] Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
