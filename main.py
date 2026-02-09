import yaml
from detectors.bruteforce import detect_bruteforce

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

LOG_FILE = config["log_file"]
THRESHOLD = config["bruteforce_threshold"]

failed_attempts, alerts = detect_bruteforce(LOG_FILE, THRESHOLD)

print("Failed attempts per IP:")
print(failed_attempts)

print("\nSECURITY ALERTS:")
for ip, count in alerts:
    print(f"🚨 Brute-force suspected from IP {ip} ({count} failed attempts)")
