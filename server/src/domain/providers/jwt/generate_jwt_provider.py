# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
from abc import ABC, abstractmethod

class GenerateJwtProvider(ABC):

    @abstractmethod
    def generate(self, user_id):
        '''Generate jwt provider.'''

        raise Exception('Method not implemented')


