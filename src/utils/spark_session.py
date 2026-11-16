import os
from pyspark.sql import SparkSession

def get_spark_session(app_name: str = "EnergySCADALakehouse") -> SparkSession:
    builder = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.driver.memory", "4g") \
        .config("spark.sql.shuffle.partitions", "8") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")
         
    return builder.getOrCreate()