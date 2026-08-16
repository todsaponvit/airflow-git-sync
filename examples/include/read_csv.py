from pyspark.sql import SparkSession
from pyspark import SparkFiles

spark=SparkSession.builder.getOrCreate()
# Read Plain CSV from websites
# 1. Define the website URL
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# 2. Download the file via SparkContext
spark.sparkContext.addFile(url)

# 3. Fetch the local path where Spark cached it
# Note: Use the exact filename from the end of your URL string
file_name = "iris.csv" 
file_path = "file://" + SparkFiles.get(file_name)

# 4. Load the file as a standard DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)
df.show()

spark.stop()
