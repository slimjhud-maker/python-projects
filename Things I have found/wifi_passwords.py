import subprocess

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8", errors="backslashreplace").split("\n")
profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

for profile in profiles:
    results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8", errors="backslashreplace").split("\n")
    passwords = [b.split(":")[1].strip() for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(profile, passwords[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(profile, "None"))

input("\n\nPress enter to continue...")