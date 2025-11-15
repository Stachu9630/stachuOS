import time
import inspect

boot_time = time.time()

stopwatches = {}

def log(message):
    elapsed = time.time() - boot_time
    # Get the module name of the caller
    caller_frame = inspect.stack()[1]
    module_name = inspect.getmodule(caller_frame[0]).__name__
    print(f"[{elapsed:06.3f}] [{module_name}] {message}")

log("logger module started")
log("""

Logger Module version 1.0.0
Built for StachuOS 4 / version 2

Documentation at Stachu9630.StachuOS.Github.io
""")


def log_time_start(name):
    stopwatches[name] = time.perf_counter()
    log(f"[TIMER] Started '{name}'")

def log_time_stop(name):
    if name not in stopwatches:
        log(f"[TIMER] Cannot stop '{name}' (not started)")
        return

    elapsed = time.perf_counter() - stopwatches[name]
    log(f"[TIMER] '{name}' finished in {elapsed:.5f} seconds")


    del stopwatches[name]

