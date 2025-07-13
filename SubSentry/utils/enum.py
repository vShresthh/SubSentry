import subprocess
import os
import logging

def run_enum(domain: str) -> list[str]:
    
    logging.info(f"[*] Enumerating subdomains for: {domain}")
    output_file = f"{domain}_subdomains.txt"

    try:
        subprocess.run(
            ["subfinder", "-d", domain, "-o", output_file],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError as e:
        logging.error(f"Subfinder failed: {e}")
        return []
    except FileNotFoundError:
        logging.error("Subfinder not found. Is it installed and in your PATH?")
        return []
    except Exception as e:
        logging.error(f"Unexpected error during subdomain enumeration: {e}")
        return []

    if not os.path.isfile(output_file) or os.path.getsize(output_file) == 0:
        logging.warning("Subfinder ran but found no subdomains.")
        return []

    try:
        with open(output_file) as f:
            subdomains = [line.strip() for line in f if line.strip()]
        logging.info(f"Found {len(subdomains)} subdomains.")
        return subdomains
    except Exception as e:
        logging.error(f"Failed to read subdomains from file: {e}")
        return []
