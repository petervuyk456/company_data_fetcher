import logging
import sys


class Logger:
    def __init__(self):
        # Initiating the logger object
        self.logger = logging.getLogger(__name__)

        # Set the level of the logger. This is SUPER USEFUL since it enables you to decide what to save in the logs file.
        # Explanation regarding the logger levels can be found here - https://docs.python.org/3/howto/logging.html
        self.logger.setLevel(logging.DEBUG)

        # Create the logs.log file
        handler = logging.FileHandler('logs.log')

        # Format the logs structure so that every line would include the time, name, level name and log message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Adding the format handler
        self.logger.addHandler(handler)

        # And printing the logs to the console as well
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
