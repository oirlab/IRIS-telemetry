Telemetry Server
================

## Telemetry server prototype based on file streams

This implementation of the telemetry server creates in the `out/` folder one `.csv` file for each telemetry keyword and streams into that (unbuffered) a line for each sample with timestamp and a value of 0.

It is multithreaded, it opens a thread for each of the telemetry keys and writes simultaneously to all the files. The largest set if NFIRAOS with 85 keys.

### Usage

    cd telemetry_server
    python telemetry_server_prototype_files.py NFIRAOS

This runs for 10 seconds and creates output files in `out/`

Get values with the sample client:

    $ python sample_client.py WFS5FR WFS4GAIN WFS4GAIN
    Current time: 2018-10-01 12:25:47.985080
    WFS5FR 2018-10-01 12:25:47.916242,0
    WFS4GAIN 2018-10-01 12:25:47.914683,0
    WFS4GAIN 2018-10-01 12:25:47.914683,0

    $ python sample_client.py WFS5FR WFS4GAIN WFS4GAIN
    Current time: 2018-10-01 12:25:54.230562
    WFS5FR 2018-10-01 12:25:54.174597,0
    WFS4GAIN 2018-10-01 12:25:54.173689,0
    WFS4GAIN 2018-10-01 12:25:54.173689,0
