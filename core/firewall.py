import subprocess
import json
import time
import os

BAN_FILE = "banned_ips.json"
BAN_DURATION = 86400  # 24 hours


def load_banned_ips():
    if not os.path.exists(BAN_FILE):
        return {}
    with open(BAN_FILE, "r") as f:
        return json.load(f)


def save_banned_ips(data):
    with open(BAN_FILE, "w") as f:
        json.dump(data, f)


def ban_ip(ip):
    print(f"[+] Banning IP: {ip}")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

    banned = load_banned_ips()
    banned[ip] = int(time.time())
    save_banned_ips(banned)


def unban_ip(ip):
    print(f"[+] Unbanning IP: {ip}")
    subprocess.run(["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])

    banned = load_banned_ips()
    if ip in banned:
        del banned[ip]
        save_banned_ips(banned)


def check_unban():
    banned = load_banned_ips()
    current_time = int(time.time())

    for ip, ban_time in list(banned.items()):
        if current_time - ban_time > BAN_DURATION:
            unban_ip(ip)