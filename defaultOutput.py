import subprocess
import time

output = "alsa_output.pci-0000_00_1f.3.analog-stereo"

for i in range(20):
    try:
        p = subprocess.check_output(["pactl", "set-default-sink", output])
        break
    except Exception:
        pass

    time.sleep(1)
