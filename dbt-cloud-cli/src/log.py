import logging
import json


class Log:
    def __init__(self, msg):
        self.msg = msg
        logging.basicConfig(
            format="%(asctime)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S", level="INFO"
        )
        logging.info("\t%s", self.msg)

    def json(msg):
        print(json.dumps(msg, indent=4, sort_keys=True))
