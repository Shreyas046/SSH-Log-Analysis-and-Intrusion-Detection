# SSH Log Analysis and Intrusion Detection

## Overview

SSH Log Analysis and Intrusion Detection is a Python-based cybersecurity tool designed to automate the detection of suspicious SSH activities from Linux authentication logs.

The application analyzes authentication logs, identifies potential intrusion attempts, extracts attack indicators such as source IP addresses and timestamps, classifies attack types, and generates a structured CSV report for further investigation.

A graphical user interface built with Tkinter provides an easy and user-friendly method to perform log analysis.

---

## Features

- SSH Authentication Log Analysis
- Detection of Failed Login Attempts
- Invalid User Enumeration Detection
- Intrusion Classification
- IPv4 and IPv6 Address Extraction
- CSV Report Generation
- Graphical User Interface
- Simulated Scanning Workflow

---

## Technologies Used

- Python
- Linux
- Tkinter
- Pandas
- Regular Expressions (Regex)
- Logwatch

---

## Attack Patterns Detected

| Pattern | Detection |
|----------|-----------|
| Failed Password | Authentication Failure |
| Invalid User | User Enumeration |
| Connection Closed | Suspicious Activity |
| Accepted Password | Successful Login Monitoring |
| No SSH Identification | Scanner/Bot Detection |

---

## Project Workflow

1. User selects the folder containing the authentication log.
2. The application scans the log file.
3. Suspicious SSH activities are detected.
4. IP addresses and timestamps are extracted.
5. Attack types are classified.
6. A CSV report is generated.

---

## Screenshots

### Main Interface

Add screenshot here

### Scanning Process

Add screenshot here

### Report Generation

Add screenshot here

---

## Future Enhancements

- Real-Time Log Monitoring
- Email Alert Notifications
- GeoIP Lookup
- Automated Threat Scoring
- CVE Correlation using NIST NVD API
- SIEM Integration

---

## Author

Shreyas Madhukar

Cybersecurity Enthusiast | Linux Security | Threat Detection
