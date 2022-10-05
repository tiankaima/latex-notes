import sys
import argparse
import os
import hashlib

parser = argparse.ArgumentParser(
    description='Make new folder for a given name (a 6-digit hash).')
parser.add_argument('--name', metavar='-n', type=str, help='name of the esssay')

args = parser.parse_args()

os.mkdir(os.path.join(os.getcwd(), hashlib.md5(args.name.encode()).hexdigest()[0:6]))
print(os.path.join(os.getcwd(), hashlib.md5(args.name.encode()).hexdigest()[0:6]),"created")