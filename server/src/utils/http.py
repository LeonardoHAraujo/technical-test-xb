# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


def ok(data):
    '''Make return http ok.'''

    rep = {}

    rep['status'] = 200
    rep['body'] = data

    return rep, rep['status']


def bad_request(error):
    '''Make return http bad request.'''

    rep = {}

    rep['status'] = 400
    rep['error'] = error

    return rep, rep['status']
