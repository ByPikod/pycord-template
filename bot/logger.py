from typing import TextIO
import datetime
import os


class PiLogger:

    def __init__(self, stdout: TextIO):
        self.stdout: TextIO = stdout
        self.flush = stdout.flush

        if os.path.exists("logs") is False:
            os.makedirs("logs")

        dt_string = datetime.datetime.now().strftime("log-%d.%m.%Y-%H:%M:%S")
        dt_string = dt_string.replace(":", "-")
        filename = "logs/" + dt_string + ".log"

        self.out_file = open(filename, "w+")

    def write(self, text) -> None:

        if text == "\n":
            self.stdout.write(text)
            self.out_file.write(text)
            return

        datestr = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        text = f"[{datestr}] {text}"

        self.stdout.write(text)
        self.out_file.write(text)

    def __enter__(self):
        return self


def install_logger(oldLogger) -> None:
    import sys
    sys.stdout = PiLogger(oldLogger)
