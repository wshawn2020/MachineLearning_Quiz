# Author: Shawn Wang
# Date: 9-22-2021
# Email: wshawn2020@gmail.com
# Github: https://github.com/wshawn2020

from solution import *

if __name__ == '__main__':
    # configuration file of source data
    filePath = 'test_v2.psv'

    # create object and initialization of solution
    solution = Solution(filePath)

    # load source data
    solution.load_data()

    # set flag of Tuesdays
    solution.weekday_search('Tuesday')

    # calculate f1 for Tuesdays
    f1 = solution.calc_f1()

    # print out final f1 value
    print('The f1 for Tuesdays is ', f1, '.')








