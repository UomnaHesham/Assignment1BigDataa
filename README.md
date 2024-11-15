
Docker project :

This project involves building and running a Docker container for data
preprocessing. The Docker container contains Python scripts and
libraries used to load, preprocess, and clean a dataset.

Docker Hub : https://hub.docker.com/r/yomnahesham/bd-a1-image

Git Hub : https://github.com/UomnaHesham/Assignment1BigDataa

Commands Overview :

1- Build the Docker Image

'''docker build -t bd-a1-image .'''

Builds a Docker image named bd-a1-image using the Dockerfile in the
current directory. This image contains all dependencies for running
Python scripts.

2- Run the Docker Container

'''docker run -it --name bd-a1-container bd-a1-image'''

Creates and runs a Docker container from the bd-a1-image image. The -it
flag allows interactive terminal access inside the container.

3- Run Data Preprocessing Script

'''python3 load.py dataset.csv'''

Executes the load.py Python script inside the container, processing the
input file dataset.csv. The script performs data cleaning,
transformation, and reduction on the dataset.

4- Pipeline Execution

The pipeline inside the Docker container performs the following
operations:

. Data Loading and Cleaning: - The dataset (dataset.csv) is loaded and
cleaned. - The script outputs a cleaned dataset (res_dpre.csv).

. Feature Transformation: - Feature (like FamilySize) is transformed as
required for model training.

. Data Reduction and Discretization: - The dataset is reduced (e.g.,
dimensions or columns) and discretized for further use.

. Figures and Reports: - Visualization file (vis.png) is generated. -
Logs of the process are saved in text files (e.g., eda-in-1.txt,
eda-in-2.txt).

These steps create the outputs that are important for the project's next
steps, including visual analysis and dataset preparation.

5- Data Transfer

To transfer the generated files from the container to local machine .
*Run the final.sh Script*:\
The final.sh script will copy the files from the Docker container to
your host machine.

bash bash final.sh

6- Push Docker Image to Docker Hub : - Push the Docker Image to Docker
Hub.

     docker tag bd-a1-image username/bd-a1-image
     docker push username/bd-a1-image
     ```

7- Push All Files to GitHub Repo : - Push all your files to a GitHub
repo.
