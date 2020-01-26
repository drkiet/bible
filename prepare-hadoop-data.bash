#!/bin/bash
hdfs dfs -mkdir -p /user/thebible
hdfs dfs -mkdir /tmp

hdfs dfs -copyFromLocal ./ccc /user/thebible
hdfs dfs -copyFromLocal ./dr /user/thebible
hdfs dfs -copyFromLocal ./lv /user/thebible
hdfs dfs -copyFromLocal ./metadata /user/thebible
hdfs dfs -copyFromLocal ./nab /user/thebible
hdfs dfs -copyFromLocal ./rsv /user/thebible
