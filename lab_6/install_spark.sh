#!/bin/sh

echo "\n>>>> Updating apt. This will take a while..."
apt update

echo "\n>>>> Installing Spark requirements (e.g., Java)..."
apt install -y curl
apt install -y openjdk-8-jdk  # because oracle jdk requires an account now >.<

echo "\n>>>> Checking Java install..."
java -version

echo "\n>>>> Downloading and installing Spark. This will take a while..."
dist=spark-2.4.4-bin-hadoop2.7
curl -O http://apache.cs.utah.edu/spark/spark-2.4.4/${dist}.tgz  # huge: 250MB!
tar zxvf ${dist}.tgz
mv ${dist}/ /opt/spark
touch ~/.bashrc
echo "" >> ~/.bashrc
echo "# SPARK env variables:" >> ~/.bashrc
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PYSPARK_DRIVER_PYTHON=ipython3" >> ~/.bashrc
echo "export PYSPARK_PYTHON=python3" >> ~/.bashrc
# Single quotes below are intentional:
echo 'export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH' >> ~/.bashrc
# Annoying py4j dependency (from /opt/spark/bin/pyspark):
echo 'export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/jre/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc
# Annoying hard-coded python check in /opt/spark/bin/pyspark. A quick-fix symlink:
ln -s /usr/bin/python3 /usr/bin/python

# exec bash to correctly source our ~/.bashrc.
exec bash
