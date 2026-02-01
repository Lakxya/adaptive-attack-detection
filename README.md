# adaptive-attack-detection
A biginner-friendly attack detection system that analyzes system logs and raises security alerts

# Adaptive Attack Detection System

A Python-based intrusion detection system (IDS) that analyzes SSH logs
to detect brute-force login attempts.

## Features
- SSH brute-force attack detection
- Regex-based robust log parsing
- Modular detector architecture
- Easy to extend with new attack detectors

## Project Structure
adaptive-attack-detection/
├── main.py
├── detectors/
│   └── bruteforce.py
├── data/
│   └── ssh.log
├── core/
├── parsers/
└── README.md

