# Python_MapReduce_Lab2_DVGC15

This work is bases on lab specification: Laboration #2. 

the mapper.py and reducer.py is based on paper: MapReduce - Simplified Data Processing on Large Clusters.pdf


If you want to test this project:
- Download and install the hadoop and hadoop streaming framework.
- When this is installed run the following hadoop commands.

- create the folder in and put your files into them.

hadoop fs -rmr /out
hadoop fs -mkdir /in

haddop fs -copyFromLocal file1.txt file2.txt /in

- To run the hadoop framework:

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-streaming-2.8.1.jar -input /in -output /out -mapper mapper.py -reducer reducer.py -file <folderpath>/MapReduce_invertedIndex_Python/mapper.py -file <folderpath>/MapReduce_invertedIndex_Python/reducer.py

- To see your results:
hadoop fs -cat /out/part-00000

if you dont want to run with the hadoop framework use the inverted_index.sh script and same output will be made.
