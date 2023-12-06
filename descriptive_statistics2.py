#!/usr/bin/env python3

import sys
import math

#  In this program, I used '\' in print to avoid line-to-long
def main():
    """Business Logic"""

    #  Initialize an empty list named numbers to store values
    numbers = []

    #  path = sys.argv[1]
    #  Initialize the count to count the line in the file
    count = 0

    #  The initial number of valid number
    validnum = 0

    #  Set the upper and lower boundary for the data in the file
    max_range = -100000
    min_range = 100000

    #  Set a flag to indicate the column number in the file
    flag = ['0', '0', '0', '0', '0', '0']

    #  Open the file and go through the whole file
    with open(sys.argv[1], 'r') as out:

        #  go through the whole file
        for line in out:
            count = count + 1
            # Set the column to parse as sys.argv[2]
            column_to_parse = int(sys.argv[2])
            try:
                flag[column_to_parse]

            #  When the index out of bound
            except IndexError:

                #  Print this when column_to_parse >= 6

                print(f"\nExiting: There is no valid 'list index' in column", \
                      column_to_parse, f"in line 1 in file:", sys.argv[1])

                #  Exit the system after warning
                sys.exit(1)

            #  Set another 'try except' to deal with the ValueError
            try:

                if line.split("\t")[column_to_parse] != 'NaN':

                    #  Add the other numeric data into the numbers list
                    numbers.append(float(line.split("\t")[column_to_parse]))
                    validnum = validnum + 1

                    #  Use the upper and lower bound to find out the max&min value in this column
                    max_range = max(numbers[validnum - 1], max_range)
                    min_range = min(numbers[validnum - 1], min_range)

            #  Still need to consider about other non NaN data, such as string in the column
            except ValueError:

                #  Skipping strings

                print(f"\n Skipping line number", count, ':', \
                      f"could not convert string to float:", \
                      '\'' + (line.split("\t")[column_to_parse]) + '\'')


    #  Here is the calculation part for the stats
    #  First check whether there are values in the numbers list
    if len(numbers) > 0:

        #  Calculate the average value
        avg = sum(numbers) / len(numbers)

        #  Initiallize the variance and std value to calculate it
        var = std = 0
        if len(numbers) > 1:

            #  Go through all the items in the numbers list
            for i in numbers:
                var = (i - avg) ** 2 + var
            #  Calculate it
            var = var / (len(numbers) - 1)

            # Get the Std Dev after we have the variance
            std = math.sqrt(var)

        #  To get the median we need to order the list first
        numbers.sort()

        #  When we have even numbers in the list
        if len(numbers) % 2 == 0:
            median = (numbers[int((len(numbers) - 1) / 2)] + numbers[int(len(numbers) / 2)]) / 2

        #  When odd numbers in the list
        else:
            median = numbers[int((len(numbers) - 1) / 2)]


    #  Outputs in this part
    #  Confirm whether there is first item in the list
    try:
        #  Check if the first item exist
        if numbers[0] != []:

            #  Print all the statistics:

            print(f"\n", f'    Column:', column_to_parse)
            print(f"\n")

            tlist = ['Count', 'Average', 'ValidNum', \
                     'Maximum', 'Minimum', 'Variance', 'Std Dev', 'Median']

            #  Print out all the results from the list

            print(f'        {tlist[0]:<10} = {count:10.3f}')
            print(f'        {tlist[2]:<10} = {validnum:10.3f}')
            print(f'        {tlist[1]:<10} = {avg:10.3f}')
            print(f'        {tlist[3]:<10} = {max_range:10.3f}')
            print(f'        {tlist[4]:<10} = {min_range:10.3f}')
            print(f'        {tlist[5]:<10} = {var:10.3f}')
            print(f'        {tlist[6]:<10} = {std:10.3f}')
            print(f'        {tlist[7]:<10} = {median:10.3f}')

    except IndexError:

        #  If there is no valid number

        print(f"\nError: There were no valid number(s) in column", \
              column_to_parse, f"in file:", sys.argv[1])


if __name__ == "__main__":
    main()


