import dns.resolver
import json
import logging
import time

# Load known vulnerable services from services.json
with open("services.json", encoding="utf-8") as f:
    services = json.load(f)

# Configure logging
logging.basicConfig(
    filename='scanner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Customizable DNS Resolver
def get_dns_resolver(timeout=5, nameservers=None):
    """
    Creates a DNS resolver with custom timeout and nameservers.
    Default timeout is 5 seconds.
    """
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = timeout  # Set lifetime of query (time before it times out)
    
    # If nameservers are provided, use them; otherwise, use system default
    if nameservers:
        resolver.nameservers = nameservers
    
    return resolver

def check_cnames(subdomains, resolver=None):
    
    logging.info("[*] Checking DNS CNAME records...")
    targets = []
    
    # Use custom resolver if provided, else use default
    resolver = resolver or get_dns_resolver()

    for sub in subdomains:
        try:
            # Attempt to resolve CNAME records for the subdomain
            answers = resolver.resolve(sub, 'CNAME')
            for rdata in answers:
                cname = str(rdata.target).rstrip('.')
                
                # Check if the CNAME target matches any known vulnerable service
                for key in services:
                    if key in cname:
                        target_info = {
                            "subdomain": sub,
                            "cname": cname,
                            "service": services[key],
                            "status": "Potential Takeover"
                        }
                        targets.append(target_info)
                        logging.info(f"Found potential takeover target: {sub} -> {cname} (Service: {services[key]})")
        
        except dns.resolver.NoAnswer:
            logging.warning(f"No CNAME record found for {sub}.")
        except dns.resolver.NXDOMAIN:
            logging.warning(f"Domain {sub} does not exist.")
        except dns.resolver.Timeout:
            logging.error(f"Timeout while resolving {sub}.")
        except Exception as e:
            logging.error(f"Error resolving CNAME for {sub}: {e}")
    
    # Return the list of targets found
    logging.info(f"Found {len(targets)} potential CNAME takeover targets.")
    return targets

def test_custom_dns_resolution(subdomains):
    """
    Test custom DNS resolution (optional) for a set of subdomains.
    """
    custom_nameservers = ['8.8.8.8', '8.8.4.4']  # Google's DNS servers as example
    resolver = get_dns_resolver(nameservers=custom_nameservers)

    results = check_cnames(subdomains, resolver=resolver)
    return results
