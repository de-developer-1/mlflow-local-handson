FROM jupyter/pyspark-notebook

USER root
RUN pip install mlflow xgboost delta-spark
USER $NB_UID
