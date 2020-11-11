#! /usr/bin/env python3
# coding: utf-8
import argparse


import analysis.csv as c_an
import analysis.xml as x_an
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type de fichier à analyser, csv ou xml?""")
    parser.add_argument("-d", "--datafile", help="""csv file of the data?""")
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    if args.extension == "csv":
        c_an.launch_analysis('current_mps.csv')
    elif args.extension == "xml":
        x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
    main()