# SIEM-Phishing-Domain-Monitor
New Domain Registration SIEM Ingestion and Dashboards for SumoLogic 

# Requirements
- Python 3.x
- Various Python Libraries to install using PIP

# Notes
- Retrieves latest domain registrations from https://whoisds.com
- Formats it for ingest and writes to log file for SumoLogic or similar SIEM solution to ingest
- SIEM does all the filtering, parsing, and other logic to determine if it looks like a phishing domain for your company.

# Configuration
Set "pwdir" to the directory to drop log files for SIEM Ingestion

# Execution
python3 /app/bin/tldMon/tldMon.py

# Crontab
0 2 * * * root python3 /app/bin/tldMon/tldMon.py >/dev/null 2>&1

# Dashboards
SumoLogic - change logic in query to work with your company's domains or key words.

