# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


class JwtVerifyUseCase:

    def __init__(self, ok, bad_request, jwt_verify):
        self.ok = ok
        self.bad_request = bad_request
        self.jwt_verify = jwt_verify

    def execute(self, token):
        '''Main method for this usecase.'''

        if not token:
            return self.bad_request('Token not found.')

        if not (isValidToken := self.jwt_verify.verify(token)):
            return self.bad_request('Token invalid.')

        return self.ok({'isValidToken': isValidToken})

