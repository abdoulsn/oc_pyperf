# ! /usr/bin/env python3
# coding: utf-8
import os
def launch_analysis(data_file):
	directory = os.path.dirname(__file__)
	path_to_file = os.path.join(directory, "data_in", data_file )
	print('path_to_file')
	with open(path_to_file, 'r') as  file:
		preview = file.readline()
	print('Le preview de ce ficher csv: {}'.format(preview))
	
def main():
	launch_analysis('current_mps.csv')


if __name__ == "__main__":
    main()