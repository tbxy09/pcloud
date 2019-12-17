import logging
import os

LOG_FORMAT = "%(name)s.%(module)s.%(funcName)s: %(message)s"

def enable_logging():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# if os.environ.get("INVOKE_INFO"):
    # enable_logging()
enable_logging()

# Add top level logger functions to global namespace. Meh.
tasklog = logging.getLogger("taskfile")
apilog = logging.getLogger("APIfile")

for x in ("debug","info"):
    globals()['task'+x] = getattr(tasklog, x)
    globals()['api'+x] = getattr(apilog, x)
