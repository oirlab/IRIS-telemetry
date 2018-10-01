import sys
import pyhocon
import datetime
from time import sleep
import concurrent.futures


def stream_telemetry(tel):
    with open(f"out/{tel['name']}.csv", "wb", buffering=0) as f:
        sleep_time = 1 / tel["requiredRate"]
        for i in range(10 * tel["requiredRate"]):
            f.write((str(datetime.datetime.now()) + ",0\n").encode("utf-8"))
            sleep(sleep_time)


CONFIG_PATH = "../IRIS-Model-Files/drs/drs-assembly/subscribe-model.conf"

conf = pyhocon.ConfigFactory.parse_file(CONFIG_PATH)
telemetry = conf["subscribe"]["telemetry"]

available_subsystems = set()
for t in telemetry:
    available_subsystems.add(t["subsystem"])

if len(sys.argv) < 2:
    print("Specify the requested subsystem")
    print("Using configuration file", CONFIG_PATH)
    print("Available subsystems", available_subsystems)
    sys.exit(1)

subsystem = sys.argv[1]
assert (
    subsystem in available_subsystems
), f"Wrong subsystem specified, available subsystems are {available_subsystems}"

subsystem_telemetry = [t for t in telemetry if t["subsystem"] == subsystem]
num_telemetry_keys = len(subsystem_telemetry)

print(f"Generating telemetry for {num_telemetry_keys} keys")

with concurrent.futures.ThreadPoolExecutor(max_workers=num_telemetry_keys) as executor:
    executor.map(stream_telemetry, subsystem_telemetry)
