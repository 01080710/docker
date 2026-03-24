from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = (
    SparkSession.builder
    .appName("ExampleSparkJob")
    .getOrCreate()
)

# Read data
df = spark.read.option("header", "true").csv("/opt/spark-data/input.csv")

# Simple transformation
result = (
    df
    .groupBy("category")
    .agg(_sum(col("amount").cast("double")).alias("total_amount"))
)

# Write output
result.write.mode("overwrite").parquet("/opt/spark-data/output")

spark.stop()
