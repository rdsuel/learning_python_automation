# Call another python script using subprocess
import subprocess

for i in range(0, 5):
    subprocess.check_call(['python3', '2_example.py'])
