import subprocess
import time

print("Cafes.lol")
time.sleep(3)

command = 'curl parrot.live'

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
