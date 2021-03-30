from pyspark.sql import SparkSession
from pyspark.sql.types import StringType


def main(app_name="Simple Tasks"):

    spark = SparkSession.builder.appName(app_name).getOrCreate()

    # log4j
    # log4jLogger= spark._jvm.org.apache.log4j.Logger
    # logger = log4jLogger.getLogger(__name__)

    log4jLogger = spark._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger("spark_app_logs")
    # logger = log4jLogger.LogManager.getRootLogger("catfish_logs")

    logger.setLevel(log4jLogger.Level.DEBUG)

    logger.info("pyspark script logger initialized")

    sc = spark.sparkContext

    # Sum of the first 100 whole numbers
    rdd = sc.parallelize(range(100000))
    result = rdd.sum()
    logger.info("THE RESULT IS:")
    logger.info(result)

    sc.stop()
    spark.stop()


if __name__ == "__main__":
    main("Simple Tasks")
