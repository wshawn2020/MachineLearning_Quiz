# Author: Shawn Wang
# Date: 9-22-2021
# Email: wshawn2020@gmail.com
# Github: https://github.com/wshawn2020

import numpy as np
import csv
import datetime

dayStrToInt = {
    "Monday"    : 0,
    "Tuesday"   : 1,
    "Wednesday" : 2,
    "Thursday"  : 3,
    "Friday"    : 4,
    "Saturday"  : 5,
    "Sunday"    : 6
}

class Solution:
    def __init__(self, filePath):
        self.filePath = filePath
        self.date = []
        self.yTure = []
        self.yHat = []

    def load_data(self):
        with open(self.filePath) as file_path:
            csv_reader = csv.reader(file_path, delimiter='|')
            next(csv_reader, None)  # skip the question line
            next(csv_reader, None)  # skip the header line

            for row in csv_reader:
                self.date.append(row[0])
                self.yTure.append(row[1])
                self.yHat.append(row[2])

    def weekday_search(self, wkdayInpt):
        wkdaySearch = dayStrToInt[wkdayInpt]
        self.isDateRight = np.full((len(self.date)), False)

        for i in range(len(self.date)):
            year = int(self.date[i][:4])
            month = int(self.date[i][5:7])
            day = int(self.date[i][-2:])

            dateToCheck = datetime.date(year, month, day)
            wkday = dateToCheck.weekday()

            if wkdaySearch == wkday:
                self.isDateRight[i] = True

    def calc_f1(self):
        dateFilter = self.isDateRight
        yTrue = np.array([int(i) for i in self.yTure])[dateFilter == True]
        yHat = np.array([int(i) for i in self.yHat])[dateFilter == True]
        epsilon = 1e-7

        tp = np.sum(yHat * yTrue, axis=0)
        fp = np.sum(yHat * (1 - yTrue), axis=0)
        fn = np.sum((1 - yHat) * yTrue, axis=0)

        pres = tp / (tp + fp + epsilon)
        recall = tp / (tp + fn + epsilon)

        f1 = 2 * pres * recall / (pres + recall + epsilon)
        f1 = np.where(np.isnan(f1), np.zeros_like(f1), f1)
        return np.mean(f1)