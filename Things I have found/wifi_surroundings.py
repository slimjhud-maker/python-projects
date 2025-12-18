import subprocess

networks = subprocess.check_output(["netsh", "wlan", "show", "network"]).decode("utf-8", errors="backslashreplace").split("\n")

for line in networks:
    if "SSID" in line:
        print(line.strip())