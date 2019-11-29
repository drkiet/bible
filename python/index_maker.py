#!/usr/bin/python3
import tokenize

from pyspark import SparkContext, SparkConf
import string
import sys
import re
import subprocess


def delete_out_dir(out_dir):
    subprocess.call(["hdfs", "dfs", "-rm", "-R", out_dir])

def get_file_names(in_dir):
    buf = ''
    file_names = []
    with subprocess.Popen(["hdfs", "dfs", "-ls", in_dir], stdout=subprocess.PIPE) as proc:
        buf += re.sub('\t', '', str(proc.stdout.read()))
    for line in buf.split('\\n'):
        tokens = []
        for token in line.split(' '):
            if token.strip() != '':
                tokens.append(token)
        if len(tokens) < 8:
            continue
        tokens = tokens[7].split('/')
        file_names.append(tokens[len(tokens)-1])
    return file_names

"""
For a given input directory that has file with an extension of .txt
create the same file with an extention of .idx store in the output directory
"""

class IndexMaker():
    def __init__(self):
        self.conf = SparkConf().setAppName('Index Maker App')
        self.sc = SparkContext(conf=self.conf)

    @staticmethod
    def main(argv):
        in_dir = argv[0]
        out_dir = argv[1]
        delete_out_dir(out_dir)
        file_names = get_file_names(in_dir)
        for file_name in file_names:
            print(file_name)
        print(len(file_names), 'files')

if __name__ == '__main__':
    IndexMaker.main(sys.argv[1:])