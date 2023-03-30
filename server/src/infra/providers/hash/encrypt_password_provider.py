# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
import hashlib

# Internal modules.
from domain.providers.hash.encrypt_password_provider import (
    EncryptPasswordProvider
)

class EncryptPassProvider(EncryptPasswordProvider):

    def encrypt(self, password):
        '''Encrypt password provider.'''

        return hashlib.sha256(password.strip().encode()).hexdigest()

