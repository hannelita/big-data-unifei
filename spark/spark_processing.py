import sys
sys.path.insert(0,'E:\\Dropbox\\Doutorado\\big-data\\big-data-unifei\\data_import')

import excel_importer as excel
data = excel.import_file()
data.head()

filtered = excel.filter_data(data)

from pyspark.sql.functions import hour, mean
spark_temp = spark.createDataFrame(filtered)

spark_temp.createOrReplaceTempView("temp")
spark_temp.groupBy(hour("Data").alias("hour")).agg(mean("Power Production").alias("Power Production")).show()