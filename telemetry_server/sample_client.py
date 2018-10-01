import os
import sys
import concurrent.futures
import datetime

keys = sys.argv[1:]
AVERAGE_LINE_LENGTH = 100

def get_telemetry(key):
    with open(f"out/{key}.csv", 'rb') as fh:
        # 1024 is average line length
        fh.seek(-AVERAGE_LINE_LENGTH, os.SEEK_END)
        last = fh.readlines()[-1].decode().strip()
    return last

print("Current time:", datetime.datetime.now())
with concurrent.futures.ThreadPoolExecutor(max_workers=len(keys)) as executor:
     values = executor.map(get_telemetry, keys)

for k,v in zip(keys, values):
    print(k,v)
