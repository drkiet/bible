#!/usr/bin/python3

from pyspark import SparkContext, SparkConf
import util
import collections
import sys
import os
import shutil

"""
For a given input directory that has file with an extension of .txt
create the same file with an extention of .idx store in the output directory
"""

class IndexMaker():
    def __init__(self):
        self.conf = SparkConf().setAppName('Index Maker App')
        self.sc = SparkContext(conf=self.conf)

    def word_count(self, file_name):
        self.index_by_word = {}
        self.text = self.sc.textFile(file_name)
        self.counts = self.text \
            .flatMap(lambda line: util.strip_punc(line)) \
            .map(lambda word: (word.lower(), 1)) \
            .reduceByKey(lambda a, b: a + b)

    def make_index(self):
        for items in self.counts.collect():
            if items[0].strip() != '':
                self.index_by_word[items[0]] = []
        line_no = 1
        for line in self.text.collect():
            line = util.strip_punc(line)
            for word in line:
                if word.strip() != '':
                    self.index_by_word[word.lower()].append(line_no)
            line_no += 1

    def write_index(self, local_file_name):
        if os.path.exists(local_file_name):
            os.remove(local_file_name)
        local_file = open(local_file_name, 'w')
        self.index_by_word = collections.OrderedDict(sorted(self.index_by_word.items()))
        for word in self.index_by_word:
            local_file.write(word + ' ' + str(self.index_by_word[word]) + '\n')

    @staticmethod
    def prepare_dirs(argv):
        in_dir = argv[0]
        out_dir = argv[1]
        local_dir = '/tmp/idx/'
        if os.path.exists(local_dir):
            shutil.rmtree(local_dir)
        os.mkdir(local_dir)
        util.delete_out_dir(out_dir)
        in_file_names = util.get_file_names(in_dir)
        out_file_names = []
        for file_name in in_file_names:
            out_file_names.append(file_name.replace('.txt', '.idx'))
        return in_dir, out_dir, in_file_names, out_file_names, local_dir

    @staticmethod
    def prepare_file_names(in_dir, local_dir, in_file_name, out_file_name):
        in_file_name = in_dir + '/' + in_file_name
        local_file_name = local_dir + out_file_name
        print(' in:', in_file_name)
        print('out:', local_file_name)
        return in_file_name, local_file_name

    @staticmethod
    def main(argv):
        in_dir, out_dir, in_file_names, out_file_names, local_dir = IndexMaker.prepare_dirs(argv)
        im = IndexMaker()
        for i in range(0, len(in_file_names)):
            in_file_name, local_file_name = IndexMaker.prepare_file_names(in_dir, local_dir, in_file_names[i], out_file_names[i])
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