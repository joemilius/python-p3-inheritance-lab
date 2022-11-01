#!/usr/bin/env python

from lib.user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        # super.__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = ["Science", "Social Studies", "Math", "Reading", "Writing", "P.E.", "Art", "Music"]

    def teach(self):
        return self.knowledge[random.randrange(len(self.knowledge))]
        pass