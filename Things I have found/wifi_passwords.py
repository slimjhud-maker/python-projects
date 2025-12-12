import subprocess
from unittest import result


data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8", errors="backslashreplace").split("\n")
profile = [i.split(":")[1][1:-1] for i in data if "All User Profiles" in i]

for i in profile:
    results = subprocess.check_output(["netsh", "wlan", "show", "profiles", i, "keyclear"]).decode("utf-8", errors="backslashreplace").spl
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<3}")