# Task 2 - Phishing Email Analyzer

## Objective
Analyze a phishing email sample and identify all phishing
characteristics using Python and online tools.

## Tools Used
- Python 3 (custom analyzer script)
- MXToolbox (email header analysis)
- VirusTotal (URL reputation check)

## What is Phishing?
Phishing is a cyber attack where criminals send fake emails
pretending to be trusted companies like PayPal, Google or
Amazon to steal your passwords and personal information.

## How to Run
1. Download or clone this repository
2. Open CMD and navigate to the folder
3. Run the script:
   python analyze.py
4. Choose input method:
   - Option 1: Paste email content directly
   - Option 2: Load from a .txt file

## Phishing Indicators Found in Sample Email

| Indicator | Details |
|-----------|---------|
| Fake sender | paypa1-support.com instead of paypal.com |
| Urgent language | "URGENT", "24 HOURS", "SUSPENDED" |
| Suspicious URL | http://paypal-secure-verify.xyz |
| Sensitive info requested | CVV, SSN, Credit Card number |
| Spelling errors | "securty", "permenantly" |
| Sent at odd time | 3:22 AM |
| Private IP in header | 192.168.45.231 (forged header) |
| Only 1 email hop | Bypassed verification servers |

## Phishing Score: 95/100
## Verdict: HIGH RISK - Very likely PHISHING!

## Files in This Repo

| File | Description |
|------|-------------|
| analyze.py | Python phishing analyzer (user input) |
| phishing_sample.txt | Sample phishing email used |
| phishing_report.txt | Auto generated analysis report |
| screenshot_mxtoolbox.png | MXToolbox header analysis result |
| README.md | Project documentation |

## Key Concepts Learned
- What phishing is and how attackers use it
- How to identify email spoofing
- How to read and analyze email headers
- How social engineering works in phishing
- How to verify suspicious URLs safely

## Header Analysis Summary (MXToolbox)
- Sending domain confirmed fake: mail.paypa1-support.com
- Originating IP is private/local: 192.168.45.231
- Only 1 hop found (legitimate emails have multiple)
- Missing "By" and "With" fields confirms forged header
- Received delay of 0 seconds is impossible for real email
