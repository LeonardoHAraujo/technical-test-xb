# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
import jwt

# Internal modules.
from domain.providers.jwt.jwt_verify_provider import JwtVerifyProvider

class JwtVerifyProvider(JwtVerifyProvider):

    def verify(self, token):
        '''Verify jwt provider.'''

        try:
            jwt.decode(token, 'secret', algorithms=['HS256'])

            return True

        except jwt.ExpiredSignatureError:
            return False
