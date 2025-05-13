import json
import logging
from typing import List, Dict

def save_json_report(results: List[Dict], filename: str = "report.json") -> None:
    try:
        with open(filename, "w") as f:
            json.dump(results, f, indent=2)
        logging.info(f"JSON report saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to write JSON report: {e}")
        print(f"[!] Error saving JSON report: {e}")

def save_markdown_report(results: List[Dict], filename: str = "report.md") -> None:
    try:
        with open(filename, "w") as f:
            f.write("# Subdomain Takeover Report\n\n")
            if not results:
                f.write("_No vulnerable subdomains found._\n")
            else:
                for r in results:
                    f.write(f"- **{r['subdomain']}** (Service: {r['service']['service']}) - Status: {r['status']}\n")
        logging.info(f"Markdown report saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to write Markdown report: {e}")
        print(f"[!] Error saving Markdown report: {e}")

def generate_report(results: List[Dict]) -> None:
    print("[*] Generating reports...\n")
    save_json_report(results)
    save_markdown_report(results)
    print("[+] Reports saved to report.json and report.md")