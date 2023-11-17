import pandas as pd
from django.db import models

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def cardValues():
        df = pd.read_csv("./frontend/questions.csv")
        return [df["QNo"].tolist(), df["Qs"].tolist(), df["A1"].tolist(), df["A2"].tolist(), df["A3"].tolist()]