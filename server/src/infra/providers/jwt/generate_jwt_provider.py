# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
import jwt
import calendar
import datetime

# Internal modules.
from domain.providers.jwt.generate_jwt_provider import GenerateJwtProvider

class GenJwtProvider(GenerateJwtProvider):

    def generate(self, user_id):
        '''Generate jwt provider.'''

        future = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        unix_future = calendar.timegm(future.timetuple())

        token = jwt.encode(
            {
                'sub': user_id,
                'exp': unix_future
            },
            'secret',
            algorithm='HS256'
        )

        return token

