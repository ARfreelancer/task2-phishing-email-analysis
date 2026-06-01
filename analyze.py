# -----------------------------------------------
#  PHISHING EMAIL ANALYZER - USER INPUT VERSION
#  Cyber Security Internship - Task 2
# -----------------------------------------------

import datetime

# ---- PHISHING INDICATORS -----------------------

SUSPICIOUS_KEYWORDS = [
    "urgent", "suspended", "verify immediately",
    "account will be deleted", "click here",
    "confirm your identity", "unusual activity",
    "within 24 hours", "permanently closed",
    "frozen", "validate your account",
    "act now", "immediate action", "warning",
    "limited time", "expire", "blocked"
]

SUSPICIOUS_DOMAINS = [
    ".xyz", ".tk", ".ml", ".ga", ".cf",
    "paypa1", "g00gle", "amaz0n", "micros0ft",
    "-secure", "-verify", "-alert", "-support",
    "-login", "-update", "-confirm"
]

SENSITIVE_REQUESTS = [
    "credit card", "cvv", "social security",
    "ssn", "password", "pin", "date of birth",
    "bank account", "routing number",
    "card number", "expiry", "mother maiden"
]

COMMON_TYPOS = {
    "permenantly": "permanently",
    "securty":     "security",
    "califronia":  "california",
    "recieve":     "receive",
    "occured":     "occurred",
    "seperate":    "separate",
    "account":     "account",
    "verfiy":      "verify",
    "immediatly":  "immediately",
    "suspened":    "suspended"
}

# ---- FUNCTIONS ---------------------------------

def print_banner():
    print()
    print("=" * 60)
    print("      PHISHING EMAIL ANALYZER")
    print("      Cyber Security Internship - Task 2")
    print("      " + str(datetime.datetime.now()))
    print("=" * 60)

def get_user_input():
    print()
    print("HOW DO YOU WANT TO INPUT THE EMAIL?")
    print("-" * 40)
    print("  1 → Type/Paste email content directly")
    print("  2 → Load from a .txt file")
    print("-" * 40)
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        print()
        print("Paste your email content below.")
        print("When done, type 'DONE' on a new line and press Enter:")
        print("-" * 40)
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "DONE":
                break
            lines.append(line)
        email_text = "\n".join(lines)
        print("-" * 40)
        print("[OK] Email content received!")
        return email_text.lower()

    elif choice == "2":
        print()
        filename = input("Enter the full file path (e.g. C:\\CyberTask2\\phishing_sample.txt): ").strip()
        try:
            with open(filename, "r", encoding="utf-8") as f:
                email_text = f.read()
            print("[OK] File loaded successfully!")
            return email_text.lower()
        except FileNotFoundError:
            print("[ERROR] File not found! Please check the path.")
            exit()
    else:
        print("[ERROR] Invalid choice! Please run again and enter 1 or 2.")
        exit()

def check_keywords(email_text):
    print()
    print("[1] CHECKING URGENT/THREATENING LANGUAGE...")
    print("-" * 40)
    found = []
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in email_text:
            print("    FOUND: '" + keyword + "'")
            found.append(keyword)
    if not found:
        print("    No suspicious keywords found")
    return found

def check_domains(email_text):
    print()
    print("[2] CHECKING SUSPICIOUS DOMAINS/URLS...")
    print("-" * 40)
    found = []
    for domain in SUSPICIOUS_DOMAINS:
        if domain in email_text:
            print("    FOUND suspicious pattern: '" + domain + "'")
            found.append(domain)
    if not found:
        print("    No suspicious domains found")
    return found

def check_sensitive(email_text):
    print()
    print("[3] CHECKING IF SENSITIVE INFO IS REQUESTED...")
    print("-" * 40)
    found = []
    for item in SENSITIVE_REQUESTS:
        if item in email_text:
            print("    DANGER: Asking for '" + item + "'")
            found.append(item)
    if not found:
        print("    No sensitive info requests found")
    return found

def check_spelling(email_text):
    print()
    print("[4] CHECKING COMMON SPELLING ERRORS...")
    print("-" * 40)
    found = []
    for wrong, correct in COMMON_TYPOS.items():
        if wrong in email_text:
            print("    TYPO FOUND: '" + wrong +
                  "' should be '" + correct + "'")
            found.append(wrong)
    if not found:
        print("    No spelling errors detected")
    return found

def check_sender(email_text):
    print()
    print("[5] CHECKING SENDER EMAIL ADDRESS...")
    print("-" * 40)
    suspicious = []
    patterns = [
        "paypa1", "g00gle", "amaz0n",
        "-support.com", "-secure.com",
        "-alert.com", "-verify.com",
        "-login.com", "-update.com"
    ]
    for p in patterns:
        if p in email_text:
            print("    SUSPICIOUS sender pattern: '" + p + "'")
            suspicious.append(p)
    if not suspicious:
        print("    Sender looks okay")
    return suspicious

def calculate_score(keywords, domains, sensitive, spelling, sender):
    score = 0
    score += len(keywords) * 10
    score += len(domains)  * 15
    score += len(sensitive)* 20
    score += len(spelling) * 10
    score += len(sender)   * 15
    return min(score, 100)

def get_verdict(score):
    if score >= 70:
        return "HIGH RISK - Very likely PHISHING!"
    elif score >= 40:
        return "MEDIUM RISK - Suspicious email!"
    else:
        return "LOW RISK - Appears relatively safe"

def save_report(score, verdict, keywords,
                domains, sensitive, spelling, sender):
    filename = "phishing_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("PHISHING EMAIL ANALYSIS REPORT\n")
        f.write("Date   : " + str(datetime.datetime.now()) + "\n")
        f.write("=" * 60 + "\n\n")

        f.write("PHISHING SCORE : " + str(score) + "/100\n")
        f.write("VERDICT        : " + verdict + "\n\n")

        f.write("-" * 60 + "\n")
        f.write("INDICATORS FOUND:\n\n")

        f.write("1. Urgent/Threatening Keywords (" +
                str(len(keywords)) + " found):\n")
        for k in keywords:
            f.write("   - " + k + "\n")

        f.write("\n2. Suspicious Domains/URLs (" +
                str(len(domains)) + " found):\n")
        for d in domains:
            f.write("   - " + d + "\n")

        f.write("\n3. Sensitive Info Requested (" +
                str(len(sensitive)) + " found):\n")
        for s in sensitive:
            f.write("   - " + s + "\n")

        f.write("\n4. Spelling Errors (" +
                str(len(spelling)) + " found):\n")
        for sp in spelling:
            f.write("   - " + sp + "\n")

        f.write("\n5. Suspicious Sender Patterns (" +
                str(len(sender)) + " found):\n")
        for se in sender:
            f.write("   - " + se + "\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("RECOMMENDATIONS:\n")
        f.write("1. Do NOT click any links in this email\n")
        f.write("2. Do NOT provide any personal information\n")
        f.write("3. Report email as phishing/spam\n")
        f.write("4. Delete the email immediately\n")
        f.write("5. Inform your IT/security team\n")
        f.write("=" * 60 + "\n")

    print()
    print("[OK] Report saved to: " + filename)

# ---- MAIN --------------------------------------

if __name__ == "__main__":
    print_banner()

    # Get email from user
    email_text = get_user_input()

    # Run all checks
    keywords  = check_keywords(email_text)
    domains   = check_domains(email_text)
    sensitive = check_sensitive(email_text)
    spelling  = check_spelling(email_text)
    sender    = check_sender(email_text)

    # Calculate score and verdict
    score   = calculate_score(keywords, domains,
                               sensitive, spelling, sender)
    verdict = get_verdict(score)

    # Print final result
    print()
    print("=" * 60)
    print("  PHISHING SCORE : " + str(score) + "/100")
    print("  VERDICT        : " + verdict)
    print("=" * 60)

    # Save report
    save_report(score, verdict, keywords,
                domains, sensitive, spelling, sender)

    print()
    input("Press Enter to exit...")
