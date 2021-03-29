FROM arezamoosavi/spark-k8s:spark-3.1.1-java11-python3.7

# Adding file to Container
COPY ./example/jars $SPARK_HOME/jars
COPY example/simple_spark.py /opt/work-dir