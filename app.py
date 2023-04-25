import os

# Disable Wi-Fi
os.system("networksetup -setairportpower en0 off")

# Wait for an hour
time.sleep(3600)

# Enable Wi-Fi
os.system("networksetup -setairportpower en0 on")
