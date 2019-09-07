FROM python:3.6-stretch
RUN pip3 install flask flask-cors
COPY src ./issocsopen
WORKDIR ./issocsopen
EXPOSE 5000
CMD ["python3", "run.py"]