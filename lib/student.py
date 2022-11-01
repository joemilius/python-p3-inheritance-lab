#!/usr/bin/env python

from lib.user import User

class Student(User):

    def __init__(self, first_name, last_name):
      # super.__init__(first_name, last_name)
      self.first_name = first_name
      self.last_name = last_name
      self.knowledge = []

    
    def learn(self, learning):
        self.knowledge.append(learning)
        pass
