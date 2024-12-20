# -*- coding: utf-8 -*-
"""reto174179

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O3WOsxkJkC9PE7H63g2FSoJhtYa_cKwp
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.master("local[*]").getOrCreate()

from google.colab import drive
drive.mount('/content/drive')

df = spark.read.csv('/content/drive/My Drive/pokemon.csv', header=True)

def ejercicio(df):

    df = spark.read.csv('/content/drive/My Drive/pokemon.csv', header=True, inferSchema=True)

    df_filtered = df.filter(~col("Name").startswith("Mega")).filter(col("Legendary") == False)

    df_with_double_speed = df_filtered.withColumn("Double_Speed", col("Speed") * 2)

    df_speed_filtered = df_with_double_speed.filter(col("Double_Speed") > 100)

    df_grouped = df_speed_filtered.groupBy("Generation").count()

    df_sorted = df_grouped.orderBy("Generation")

    df_final = df_sorted.withColumnRenamed("count", "Conteo").withColumn("Conteo", col("Conteo").cast("string"))

    pandas_df = df_final.toPandas()

    return pandas_df

ejercicio(df)

