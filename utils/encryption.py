import json
import os
from base64 import b64encode, b64decode

from utils.logger import log

def create_encrypted_config(data, file_path):
    """Creates an encrypted credential file if none exists.  Stores results in a
    file in the root directory."""
    if isinstance(data, dict):
        data = json.dumps(data)
    with open(file_path, "w") as f:
        f.write(data)
        log.info("Credentials safely stored.")



def load_encrypted_config(config_path, encrypted_pass=None):
    """Decrypts a previously encrypted credential file and returns the contents back
    to the calling thread."""
    log.info("Reading credentials from: " + config_path)
    with open(config_path, "r") as json_file:
        data = json_file.read()
        return json.loads(data)
