# SubSentry

**SubSentry** is a modular and automated subdomain takeover detection tool. It performs subdomain enumeration, identifies vulnerable CNAME records, validates takeover possibilities, and generates detailed reports — making it a powerful addition to any pentester or bug bounty hunter's toolkit.

---

## Features

- Subdomain enumeration using `subfinder`
- DNS CNAME resolution via `dnspython`
- Fingerprint-based takeover validation (configurable via `services.json`)
- Automated report generation in **JSON** and **Markdown**
- Logging with rotating log files
- Built with modular Python design for extensibility

---

## Installation

### Step 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SubSentry.git
cd SubSentry
```
### Step 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate (This will activate the virtual environment.)
```
### Step 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```
### Step 4. Install subfinder (Required)
SubSentry uses subfinder for subdomain enumeration.

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
Ensure that $GOPATH/bin is in your PATH.

### Step 5. Install SubSentry as a Local Package (Optional)
If you want to install SubSentry as a local package using setup.py, run:

```bash
pip install .
```
You can now run it from anywhere in your virtual environment with:
```bash
python3 sentry.py
```
