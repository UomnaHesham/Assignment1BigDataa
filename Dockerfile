# Use the Ubuntu base image
FROM ubuntu:22.04

# Update The Package
RUN apt-get update -y 
RUN apt-get install -y

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Install Python python libraries
RUN pip3 install pandas 
RUN pip3 install numpy
RUN pip3 install seaborn
RUN pip3 install matplotlib
RUN pip3 install scikit-learn
RUN pip3 install scipy
# Create directory inside container
RUN mkdir -p /home/doc-bd-a1/

# Move dataset to container
COPY dataset.csv /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

COPY load.py dpre.py eda.py vis.py model.py /home/doc-bd-a1/

# Open bash shell upon container startup
CMD ["/bin/bash"]
