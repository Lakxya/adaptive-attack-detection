import re

FAILED_REGEX = re.compile(
    r"Failed password.*from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
)

def detect_bruteforce(log_file_path, threshold=3):
    failed_attempts = {}

    with open(log_file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            line = line.strip()
            match = FAILED_REGEX.search(line)

            if match:
                ip = match.group(1)

                if ip not in failed_attempts:
                    failed_attempts[ip] = 1
                else:
                    failed_attempts[ip] += 1

    alerts = []
    for ip, count in failed_attempts.items():
        if count >= threshold:
            alerts.append((ip, count))

    return failed_attempts, alerts
