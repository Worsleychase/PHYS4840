#!/usr/bin/python
#####################################
#
# Solutions Lab 1 Exercise 2
# Author: M Joyce
#
#####################################
import numpy as np

def takeInput():
    return float(input('enter the amount of money you have for cookies: '))

def cookieCount(cookie_price, max_money):
    return np.floor(max_money / cookie_price)

def changeCalc(cookie_price, max_money):
    return round((max_money % cookie_price),2)

def lab1_ex2():
    max_money = takeInput()
    # Price list:
    # Sugar – $2.65
    # Chocolate – $3.20
    # Snickerdoodle – $3.45
    # S’mores – $3.70
    sugar_price = 2.65
    choc_price = 3.20
    snick_price = 3.45
    smore_price = 3.70

    n_sugar = cookieCount(sugar_price, max_money)
    n_choc = cookieCount(choc_price, max_money)
    n_snick = cookieCount(snick_price, max_money)
    n_smore  = cookieCount(smore_price, max_money)

    change_sugar = changeCalc(sugar_price, max_money)
    change_choc =  changeCalc(choc_price, max_money)
    change_snick =  changeCalc(snick_price, max_money)
    change_smore =  changeCalc(smore_price, max_money)

    print('you can have', n_sugar, ' sugar cookies with $',change_sugar, ' in change remaining')
    print('you can have', n_choc, ' chocolate cookies with $',change_choc, ' in change remaining')
    print('you can have', n_snick, ' snickerdoodles with $',change_snick, ' in change remaining')
    print('you can have', n_smore, " s'mores cookies with $",change_smore, ' in change remaining')
    ###########################################
    #
    # the array casting below is the core weakness of this solution!
    # If the cookie_type and spare_change arrays are not
    # ordered in precisely this way, argmin() from one vector
    # will not correctly index the other vector
    #
    ###########################################
    cookie_type = np.array(['sugar', 'chocolate', 'snickerdoodle', "s'mores"])
    spare_change = np.array([change_sugar, change_choc, change_snick, change_smore])
    print('minimum spare change: ', spare_change.min())
    print('index of the minimum value in the array: ', spare_change.argmin() )
    which_cookie = cookie_type[spare_change.argmin()]
    print('The single type of cookie that minimizes change is: ', which_cookie)