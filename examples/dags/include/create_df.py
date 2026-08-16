from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("Create DataFrame") \
        .getOrCreate()

    df = spark.createDataFrame(
        [
            (1, "John Doe", 21),
            (2, "Jane Doe", 22),
            (3, "Joe Bloggs", 23),
        ],
        ["id", "name", "age"],
    )
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()
