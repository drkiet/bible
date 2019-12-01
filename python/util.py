#!/usr/bin/python3

import string
import re
import subprocess


def delete_out_dir(out_dir):
    subprocess.call(["hdfs", "dfs", "-rm", "-R", out_dir])


def copy_from_local(local_files, remote_dir):
    print(local_files, remote_dir)
    subprocess.call(["hdfs", "dfs", "-copyFromLocal", local_files, remote_dir])


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
        file_names.append(tokens[len(tokens) - 1])
    return file_names


def strip_punc(s):
    return s.translate(str.maketrans('', '', string.punctuation)).split(' ')
