# Data Extraction & Secure Validation Assignment
**Assignment:** ALU Regex Data Extraction  
**Author:** Cedric Hirwa  

# Project Overview
This project is a Python-based sanitization engine designed to process raw, messy text data from external APIs. It utilizes Regular Expressions (Regex) to extract structured information while implementing defensive programming techniques to ensure data security and privacy.

# Features & Data Types
The tool identifies and extracts the following data types:
* **Email Addresses:** Detects standard and international formats (e.g., `.co.uk`).
* **URLs:** Specifically targets `http` and `https` protocols to ensure link validity.
* **Credit Card Numbers:** Identifies 16-digit sequences separated by spaces or dashes.
* **Currency:** Extracts USD amounts, handling commas for thousands and decimal points.

---

# Security Awareness & Implementation
In compliance with security best practices for Junior Developers, this tool implements:

1. XSS Neutralization
The engine performs a **pre-processing pass** to identify HTML and `<script>` tags. These are neutralized (replaced with `[SECURITY_STRIPPED]`) before data extraction to prevent Cross-Site Scripting (XSS) vulnerabilities if the data were rendered in a UI.

2. Sensitive Data Redaction
To follow privacy regulations (like GDPR or PCI-DSS), Credit Card numbers are **masked** immediately upon extraction. Only the last four digits are preserved in the output (e.g., `****-****-****-4432`), preventing accidental exposure in logs.

 3. Protocol Enforcement
The URL regex is designed to require a protocol prefix, ignoring "naked" domains that could be spoofed or lead to untrusted resources.

---

# How to Use

# Prerequisites
* Python 3.x installed.

# Execution
1. Ensure `sample_input.txt` is in the same directory as the script.
2. Run the program: python3 main.py
