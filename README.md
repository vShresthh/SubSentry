# SubSentry

**SubSentry** is a modular and automated subdomain takeover detection tool. It performs subdomain enumeration, identifies vulnerable CNAME records, validates takeover possibilities, and generates detailed reports — making it a powerful addition to any pentester or bug bounty hunter's toolkit.

---

## Features

- Subdomain enumeration using `subfinder`.
- DNS CNAME resolution via `dnspython`.
- Fingerprint-based takeover validation (configurable via `services.json`).
- Automated report generation in **JSON** and **Markdown**.
- Logging with rotating log files.
- Built with modular Python design for extensibility.

---

## Installation

#### Step 1. Clone the Repository

```bash
git clone https://github.com/vShresthh/SubSentry.git
cd SubSentry
```
#### Step 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate (This will activate the virtual environment.)
```
#### Step 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```
#### Step 4. Install subfinder (Required)
SubSentry uses subfinder for subdomain enumeration.

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
Ensure that $GOPATH/bin is in your PATH.

#### Step 5. Install SubSentry as a Local Package (Optional)
If you want to install SubSentry as a local package using setup.py, run:

```bash
pip install .
```

---

## Usage
```bash
python3 sentry.py
```
Follow the interactive prompt to enter the domain name.

SubSentry will:
- Enumerate subdomains
- Resolve CNAMEs
- Validate for takeover possibilities
- Save results in `report.json` and `report.md`

---

## Output Files

| File            | Description                              |
|-----------------|------------------------------------------|
| subdomains.txt  | List of discovered subdomains            |
| report.json     | Validated results in structured format   |
| report.md       | Markdown summary of takeover status      |
| scanner.log     | Rotating log file for debugging          |

---

## Configuration
You can extend fingerprint detection by editing services.json:
```json
{
  "github.io": {
    "service": "GitHub Pages",
    "fingerprint": "There isn't a GitHub Pages site here."
  }
}
```

---

## Disclaimer
This tool is intended for **educational and authorized security testing purposes only**.  
Unauthorized use on third-party domains is strictly prohibited.

The creator assumes **no responsibility or liability** for any misuse. This includes, but is not limited to:

- Unlawful or illegal use of the tool  
- Legal or law infringement in any country, state, or region  
- Actions against human ethics, morals, or global cultures  
- Malicious acts causing harm to individuals, systems, or organizations using this tool

Use this tool **only with explicit permission** from the target owner.

---

## License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.
