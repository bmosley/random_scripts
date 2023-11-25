import subprocess
import os

profileOutput = os.popen("/usr/sbin/system_profiler SPHardwareDataType").read().strip()
if profileOutput:
    lines = profileOutput.split("\n")
    for line in lines:
        if "Hardware UUID" in line:

            # like 'Hardware UUID: 7086A05D-039D-5761-A106-72F86111995A'
            parts = line.split("Hardware UUID: ")
            if parts and len(parts) > 1:
                udid = parts[1].strip()

        # parse out 'hw model' (like "Model Identifier: MacBookPro13,2")
        if "Model Identifier:" in line:
            parts = line.split("Model Identifier: ")
            if parts and len(parts) > 1:
                hwModel = parts[1].strip()

print(hwModel)
print(udid + '\n')