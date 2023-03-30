# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Internal modules.
from utils.http import ok, bad_request
from domain.usecases.jwt_verify_usecase import JwtVerifyUseCase
from infra.providers.jwt.jwt_verify_provider import JwtVerifyProvider

class JwtVerifyFactory:

    @staticmethod
    def build():
        '''Return builded use case.'''

        args = {}

        args['ok'] = ok
        args['bad_request'] = bad_request
        args['jwt_verify'] = JwtVerifyProvider()

        return JwtVerifyUseCase(**args)

