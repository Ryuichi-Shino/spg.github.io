from django.db import models

import sys
sys.dont_write_bytecode = True

class Score(models.Model):
    score = models.IntegerField(default=0)

    def increment(self):
        self.score += 1
        self.save()

    def reset(self):
        self.score = 0
        self.save()