Python
# Configuration file for Automated Security Tool Tracker

# Import required libraries
import datetime
import os
import csv

# Configuration settings
TRACKER_NAME = "Automa Security Tracker"
VERSION = "1.0"

# List of security tools to track
TOOLS = [
    {"name": "Nmap", "path": "/usr/bin/nmap", "version": "7.92"},
    {"name": "Wireshark", "path": "/usr/bin/wireshark", "version": "3.4.5"},
    {"name": "John the Ripper", "path": "/usr/bin/john", "version": "1.9.0"},
]

# Log file settings
LOG_FILE = "automa_security_log.csv"
LOG_HEADERS = ["Tool Name", "Version", "Last Run", "Result"]

# Email notification settings
EMAIL_NOTIFY = True
EMAIL_RECIPIENTS = ["security_team@example.com"]
EMAIL_SERVER = "smtp.example.com"
EMAIL_USERNAME = "automa_security"
EMAIL_PASSWORD = "password123"

# Scheduled task settings
SCHEDULED_TASK = True
SCHEDULED_TIME = "00:00"  # daily at midnight