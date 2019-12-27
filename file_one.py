import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Enter your username here")             #specifies which command line argument our programme is willing to accept
    args = parser.parse_args()                  # returns data from the options specified above
    print(args.username)

my_main()

if __name__ == "__main__"



#
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number")
# args = parser.parse_args()
# print(args.square**2)