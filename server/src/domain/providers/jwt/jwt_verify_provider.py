# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
from abc import ABC, abstractmethod

class JwtVerifyProvider(ABC):

    @abstractmethod
    def verify(self, token):
        '''Verify jwt provider.'''

        raise Exception('Method not implemented')


