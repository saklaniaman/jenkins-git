FROM centos:7

RUN mkdir my-model
ENV MODEL_DIR=/MLOps/my-model

COPY diabetes.csv ./diabetes.csv
COPY FinalDraftMLProject.py ./FinalDraftMLProject.py