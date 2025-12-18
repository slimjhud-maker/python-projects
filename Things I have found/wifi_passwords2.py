import subprocess

profiles_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8", errors="backslashreplace").split("\n")
profiles = [line.split(":")[1].strip() for line in profiles_data if "All User Profile" in line]

for profile in profiles:
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8", errors="backslashreplace").split("\n")
        password = [line.split(":")[1].strip() for line in results if "Key Content" in line]
        print(f"{profile:<30} | {password[0] if password else 'None'}")
    except subprocess.CalledProcessError:
        print(f"{profile:<30} | Error retrieving")