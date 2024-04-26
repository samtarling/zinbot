"""Runs 'zinbot."""
__author__ = "Tamzin Hadasa Kelly"
__copyright__ = "Copyright 2021, Tamzin Hadasa Kelly"
__license__ = "The MIT License"
__email__ = "coding@tamz.in"
__version__ = "1.4.2"

import time

import pagetriage.newpages
import logging_


def run() -> None:
    """Run the bot's tasks that are currently approved / in trial."""
    logging_.log_local_misc(f"[{logging_.gettimestamp()}] Checking queue", "debug.txt")
    pagetriage.newpages.checkqueue()  # trial


if __name__ == "__main__":
    print(f"RUNNING (version {__version__})")
    logging_.log_local_misc(f"[{logging_.gettimestamp()}] Bot start", "debug.txt")

    while True:
        run()
        print("Run done. Sleeping.")
        time.sleep(1800)
