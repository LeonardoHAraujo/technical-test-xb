# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
from abc import ABC, abstractmethod

class GetUserByEmailRepository(ABC):

    @abstractmethod
    def find_by_email(self, email):
        '''Find user by email.'''

        raise Exception('Method not implemented')
