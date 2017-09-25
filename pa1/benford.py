# CS121: Benford's Law
#
# Spencer Ho

# Functions for evaluating data using Benford's Law.

import math
import os.path
import pylab as plt
import sys
import util


def extract_leading_digits(dollar_amount, num_digits):
    d = dollar_amount
    d = d[1:]
    d = float (d)
    e = math.trunc(10 ** (-math.floor(math.log10(d)) + num_digits - 1) * d)
    return e
    '''
    Given a dollar amount as a string and a number of digits, extract
    the specified number of leading digits

    Inputs:
        dollar_amount: string
        num_digits: the number of leading digits to extract from the
            amount.

    Returns:
        integer
    '''


    # Replace 0 with an appropriate return value
  



def get_leading_digits_range(num_digits):
    x = 10 ** (num_digits - 1)
    y = 10 ** num_digits
    return x, y
    '''
    Your function header comment here
    '''
    # YOUR CODE HERE
    # Replace (0, 0) with an appropriate return value
    


def compute_expected_benford_dist(num_digits):
    x = get_leading_digits_range(num_digits)
    x = list(range(x[0], x[1]))
    b = []   #expected benford distribution
    for i in x:
        b.append(math.log10(1 + 1 / i))
    return b


    '''
    YOUR FUNCTION HEADER COMMENT HERE
    '''

    # YOUR CODE HERE
    # Replace [] with an appropriate return value
  


def compute_benford_dist(dollar_amounts, num_digits):
    a = get_leading_digits_range(num_digits)
    b = [0] * (a[1] - a[0])   #creating an empty distribution list of length N
    for i in dollar_amounts:
        c = extract_leading_digits(i, num_digits)
        b[c - a[0]] = b[c - a[0]] + 1
    b[:] = [x / len(dollar_amounts) for x in b]
    return b    
    '''
    Your function header comment here
    Note that dollar_amounts is a list of strings
    '''
    # YOUR CODE HERE
    # Replace [] with an appropriate return value
  


def compute_benford_MAD(dollar_amounts, num_digits):
    x = compute_expected_benford_dist(num_digits)
    y = compute_benford_dist(dollar_amounts, num_digits)
    z = 0
    for i in range(len(x)):
        z = abs(x[i] - y[i]) + z   #z is the sum of the series x-y from i=1 to length of data set
    m = z / len(x)
    return m
    '''
    Your function header comment here
    Note that dollar_amounts is a list of strings
    '''

    # YOUR CODE HERE
    # Replace 0.0 with an appropriate return value





################ Do not change the code below this line ################

def plot_benford_dist(dollar_amounts, num_digits):
    '''
    Plot the actual and expected benford distributions

    Inputs:
        dollar_amounts: a non-empty list of positive dollar amounts as
            strings
        num_digits: number of leading digits
    '''
    # The assert statement below will cause the program to fail with the error:
    #    num_digits must be greater than zero...
    # if num_digits less than or equal to zero.   It will have no
    # effect, if num_digits is greater than zero.

    assert num_digits > 0, \
        "num_digits must be greater than zero {:d}".format(num_digits)

    n = len(dollar_amounts)

    # The assert statement below will fail with the error:
    #    "dollar_amounts must be a non-empty list"
    # if dollar_amounts is an empty list.
    assert n > 0, \
        "dollar_amounts must be a non-empty list"

    # compute range of leading digits
    (lb, ub) = get_leading_digits_range(num_digits)
    digits = range(lb,ub)

    # start a new figure
    f = plt.figure()

    # plot expected distribution
    expected = compute_expected_benford_dist(num_digits)
    plt.scatter(digits, expected, color="red", zorder=1)

    # plot actual distribution
    actual = compute_benford_dist(dollar_amounts, num_digits)
    plt.bar(digits, actual, align="center", color="blue", zorder=0)

    # set hash marks for x axis.
    plt.xticks(range(lb, ub, lb))

    # compute limits for the y axis
    max_val = max(max(expected), max(actual))
    y_ub = max_val * 1.1
    plt.ylim(0,y_ub)

    # add labels
    plt.title("Actual (blue) and expected (red) Benford distributions")
    if num_digits ==1: 
        plt.xlabel("Leading digit")
    else:
        plt.xlabel("Leading digits")
    plt.ylabel("Proportion")

    # show the plot
    plt.show()


def go():
    usage = "usage: python benford.py <input filename> <column number>  <num digits>"
    if len(sys.argv) != 4:
        print(usage)
    else:
        input_filename = sys.argv[1]
        if not os.path.isfile(input_filename):
            print(usage)
            print("error: file not found: {}".format(input_filename))
            return

        # convert column number argument to an integer
        try:
            col_num = int(sys.argv[2])
        except ValueError:
            s = "error: column number must be an integer: {}"
            print(usage)
            print(s.format(sys.argv[2]))
            return

        data = util.read_column_from_csv(input_filename, col_num, True)

        # convert number of digits argument to an integer
        try:
            num_digits = int(sys.argv[3])
        except ValueError:
            s = "error: number of digits must be an integer: {}".format(sys.argv[3])
            print(usage)
            print(s.format(sys.argv[3]))
            return

        plot_benford_dist(data, num_digits)

        # print only four digits after the decimal point
        print("MAD: {:.4}".format(compute_benford_MAD(data, num_digits)))

if __name__=="__main__":
    go()
