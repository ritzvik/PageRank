hadoop fs -mkdir /node
hadoop fs -put C:\hadoop-2.8.0\pagerank\testdata1.txt /node
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\hadoop-2.8.0\pagerank\mapper1.py -mapper "python C:\hadoop-2.8.0\pagerank\mapper1.py 10" -file C:\hadoop-2.8.0\pagerank\reducer1.py -reducer "python C:\hadoop-2.8.0\pagerank\reducer1.py 10" -numReduceTasks 1 -input /node/* -output /node-output
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\hadoop-2.8.0\pagerank\mapper2.py -mapper "python C:\hadoop-2.8.0\pagerank\mapper2.py 10" -file C:\hadoop-2.8.0\pagerank\reducer2.py -reducer "python C:\hadoop-2.8.0\pagerank\reducer2.py 10" -input /node-output/* -output /node-matrix
python C:\hadoop-2.8.0\pagerank\vec_gen.py C:\hadoop-2.8.0\pagerank\10.txt 10

For ($i=0; $i -lt 10; $i++) {
    echo "
    
    ----$i----
    
    "
    hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\hadoop-2.8.0\pagerank\mapper3.py -mapper "python C:\hadoop-2.8.0\pagerank\mapper3.py C:\hadoop-2.8.0\pagerank\10.txt" -file C:\hadoop-2.8.0\pagerank\reducer3.py -reducer "python C:\hadoop-2.8.0\pagerank\reducer3.py 10" -numReduceTasks 1 -input /node-matrix/* -output /node-pagerank
    hadoop fs -get /node-pagerank/* C:\hadoop-2.8.0\pagerank\
    rm C:\hadoop-2.8.0\pagerank\10.txt
    mv C:\hadoop-2.8.0\pagerank\part* C:\hadoop-2.8.0\pagerank\10.txt
    rm C:\hadoop-2.8.0\pagerank\*CESS
    rm C:\hadoop-2.8.0\pagerank\part*
    hadoop fs -rm -r /node-pagerank
}
