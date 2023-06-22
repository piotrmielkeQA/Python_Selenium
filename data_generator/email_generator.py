from hashlib import new
from random import Random
from tokenize import String

import random
import string


class EmailGenerator():
    def random_email(self, char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num)) + "@gmail.com"

