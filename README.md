# APEP - Subdomain Enumerator 🐍

A fast, multi-threaded subdomain enumeration tool written in Python.
Designed for penetration testers and security researchers to discover
valid subdomains of a target domain during reconnaissance.

## ⚠️ Disclaimer
This tool is intended for authorized penetration testing and educational
purposes only. Always obtain written permission before testing any domain
you do not own. Unauthorized use is illegal and unethical.

## Features
- Multi-threaded scanning for fast enumeration
- Saves discovered subdomains to an output file
- Clean ASCII banner
- Simple command-line interface

## Requirements
- Python 3.x
- dnspython

## Installation
git clone https://github.com/C0rmat/APEP-Subdomain-Enumerator
cd APEP-Subdomain-Enumerator
pip install dnspython

## Usage
python3 scanner.py --domain example.com --wordlist wordlist.txt

## Arguments
--domain     Target domain (e.g. example.com)
--wordlist   Path to your wordlist file
--threads    Number of threads (default: 10)
--output     Output file for results (default: results.txt)

## Example
python3 scanner.py --domain google.com --wordlist subdomains.txt --threads 20

## Wordlists
Recommended wordlists can be found in the SecLists repository:
https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS

## Author
C0rmat
