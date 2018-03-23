# Snakes Cafe

**Author**: Tyler Fishbone and Shannon Tully
**Version**: 0.4.0

## Overview
This is an order form interface for a restaurant. Upon start up the user is shown a welcome message, instructions to exit the application, and a menu of items. The user is then prompted to enter in text saying what they would like to order. After each order they get a repsonse saying what they've added to their cart and how many of those they currently have.

This application addresses the need for a simple and easy to understand ordering interface.

## Getting Started
1. Download and instal Python 3.6 if you do not already have it installed.
2. Fork or clone the repo to your machine.
3. Navigate inside the repo
4. If you'd like to use your own menu, put a valid csv file into directory. see snakes_cafe.py for format
5. Execute `python3 -m vent ENV` in the terminal
6. Execute `python3 script.py`
7. Order as much as you can eat!

## Architecture
This application is written in Python, specifically 3.6. No eternal libraries or APIs are currently used in it.

## Change Log
* 2018-03-22 - 1930 - user can enter their own csv file path for customized menu
* 2018-03-22 - 1830 - tests added
* 2018-03-22 - 1730 - multiple quantities now can be ordered at once
* 2018-03-22 - 1600 - all major functions tested, stock property added
* 2018-03-21 - 1800 - entering menu or any of the categories prints that over, more tests added
* 2018-03-21 - 1500 - user can now enter order to see reciept when they enter order
* 2018-03-20 - 1730 - second and third test function completed and passed
* 2018-03-20 - 1500 - first test function completed
* 2018-03-20 - 1400 - reformatted file for more modularity
* 2018-03-19 - 1800 - user input order is reflected in dictionary of menu items ordered. handles inputted items not on menu
* 2018-03-19 - 1645 - menu now stored in app as dict. quits cleanly.
* 2018-03-19 - 1730 - app prints menu to screen when runa dn accepts user input.
* 2018-03-19 - 1700 - initial scaffold complete.

