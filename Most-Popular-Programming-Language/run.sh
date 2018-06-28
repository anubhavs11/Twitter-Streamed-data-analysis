hadoop jar hadoop-streaming-3.1.0.jar -mapper mapper.py -reducer reducer.py -input twitter.txt -output output
# twitter.txt is actually a json file i.e. Output of TwitterStreaming API
# mapper.py mapper program
# reducer.py reducer program
# output is directory that will be created automatically when job is executed
