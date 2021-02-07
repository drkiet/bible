#!/bin/bash
hdfs dfs -mkdir -p /user/thebible

hdfs dfs -copyFromLocal ./dr /user/thebible
hdfs dfs -copyFromLocal ./lv /user/thebible
hdfs dfs -copyFromLocal ./nab /user/thebible
hdfs dfs -copyFromLocal ./rsv /user/thebible

hdfs dfs -copyFromLocal ./ccc /user/thebible
hdfs dfs -copyFromLocal ./metadata /user/thebible

hdfs dfs -copyFromLocal ./dr.csv /user/thebible
hdfs dfs -copyFromLocal ./lv.csv /user/thebible
hdfs dfs -copyFromLocal ./nab.csv /user/thebible
hdfs dfs -copyFromLocal ./rsv.csv /user/thebible

hdfs dfs -copyFromLocal ./dr.json /user/thebible
hdfs dfs -copyFromLocal ./lv.json /user/thebible
hdfs dfs -copyFromLocal ./nab.json /user/thebible
hdfs dfs -copyFromLocal ./rsv.json /user/thebible
