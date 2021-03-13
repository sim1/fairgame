#      FairGame - Automated Purchasing Program
#      Copyright (C) 2021  Hari Nagarajan
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      The author may be contacted through the project's GitHub, at:
#      https://github.com/Hari-Nagarajan/fairgame

import getpass as getpass
import stdiomask
import json
import os
from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt

from utils.logger import log


def create_encrypted_config(data, file_path):
    """Creates an encrypted credential file if none exists.  Stores results in a
    file in the root directory."""
    if isinstance(data, dict):
        data = json.dumps(data)
    with open(file_path, "w") as f:
        f.write(data)


def load_encrypted_config(config_path, encrypted_pass=None):
    """Decrypts a previously encrypted credential file and returns the contents back
    to the calling thread."""
    log.info("Reading credentials from: " + config_path)
    with open(config_path, "r") as json_file:
        data = json_file.read()
        return json.loads(data)
