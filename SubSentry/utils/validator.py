import logging

def validate(targets, exploit_keywords=None):
    """
    Validates subdomain takeover possibilities by analyzing CNAME records.
    Targets should have 'subdomain', 'cname', and 'service' info.
    The status is marked as 'Exploitable', 'Needs Review', or other custom statuses based on conditions.
    
    :param targets: List of targets containing subdomain, cname, and service details.
    :param exploit_keywords: List of keywords that indicate exploitable subdomains (default is None).
    :return: List of validated targets with added status field.
    """
    
    # Set default keywords for exploitable subdomains if none are provided
    if exploit_keywords is None:
        exploit_keywords = ["cdn", "dev", "staging"]
    
    logging.info("[*] Validating subdomain takeover possibilities...")

    validated = []

    for target in targets:
        try:
            # Extract target details
            subdomain = target['subdomain']
            cname = target['cname']
            service = target['service']
            service_name = service['name']
            service_fingerprint = service.get('fingerprint', None)

            # Log the validation process for each target
            logging.info(f"Validating {subdomain} with CNAME {cname} for service {service_name}")

            # Check for missing CNAME record (important for validation)
            if not cname:
                status = "No CNAME"
                logging.warning(f"{subdomain} has no CNAME record.")
            
            # Logic to determine if the subdomain is exploitable based on the CNAME and service
            elif any(keyword in subdomain for keyword in exploit_keywords):
                status = "Exploitable"
                logging.info(f"{subdomain} is exploitable based on subdomain pattern.")
            
            # If service is AWS, GitHub, or others, we can add service-specific checks here
            elif service_name in ["GitHub", "AWS", "GitLab"]:
                status = "Needs Review"  # This can be extended for more service-specific checks.
                logging.info(f"{subdomain} marked for review due to service {service_name}.")
            else:
                status = "Needs Review"
                logging.info(f"{subdomain} needs review based on current logic.")

            # Append the validated target with status
            validated.append({
                **target,
                "status": status
            })
        
        except KeyError as e:
            # Log missing key error in target data
            logging.error(f"Missing key {e} in target {target}. Skipping.")
            continue
        except Exception as e:
            # Handle unexpected errors gracefully
            logging.error(f"Unexpected error occurred while validating {target}: {e}")
            continue

    return validated
