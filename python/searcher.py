#!/usr/bin/python3

from pyspark import SparkContext, SparkConf
import util
import collections
import sys
import os
import shutil

"""
word-> filename1, filename2, ...
"""

class Searcher:
    def __init__(self):
        self.file_names_by_word = {}
        pass

    @staticmethod
    def prepare_dirs(argv):
        in_dir = argv[0]
        idx_dir = argv[1]
        in_file_names = util.get_file_names(in_dir)
        idx_file_names = util.get_file_names(idx_dir)
        return in_dir, idx_dir, in_file_names, idx_file_names

    @staticmethod
    def prepare_file_names(in_dir, local_dir, in_file_name, idx_file_name):
        in_file_name = in_dir + '/' + in_file_name
        local_file_name = local_dir + out_file_name
        print(' in:', in_file_name)
        print('out:', local_file_name)
        return in_file_name, local_file_name

    @staticmethod
    def main(argv):
        in_dir, idx_dir, in_file_names, idx_file_names = Searcher.prepare_dirs(argv)
        for i in range(0, len(idx_file_names)):
            im.word_count(in_file_name)
            im.make_index()
            im.write_index(local_file_name)

        print('\n\n')
        print('   in_dir:', in_dir)
        print('  out_dir:', out_dir)
        print('local_dir:', local_dir)

        util.copy_from_local(local_dir, out_dir)


if __name__ == '__main__':
    IndexMaker.main(sys.argv[1:])