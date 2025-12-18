import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")


import sys


class ConsoleLogger:
    def __init__(self):
        self.log_levels = {
            "error": "\033[91m",  # Red
            "warn": "\033[93m",  # Yellow
            "success": "\033[92m",  # Green
            "info": "\033[94m",  # Blue
            "reset": "\033[0m",  # Reset to normal
        }

    def _log(self, level, title, message=None):
        color = self.log_levels.get(level, self.log_levels["info"])
        reset = self.log_levels["reset"]

        # Use a default message if none is provided
        message = message if message else "No message provided."

        print(f"{color}[{level.upper()}] {title}: {message}{reset}")

    def error(self, title, message=None):
        self._log("error", title, message)

    def warn(self, title, message=None):
        self._log("warn", title, message)

    def success(self, title, message=None):
        self._log("success", title, message)

    def info(self, title, message=None):
        self._log("info", title, message)
