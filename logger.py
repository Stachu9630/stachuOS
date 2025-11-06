import time
import inspect

boot_time = time.time()

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

Documentation at Stachu9630.github.io
""")