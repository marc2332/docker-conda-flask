# Use anaconda image
FROM continuumio/anaconda3

# Create a the project folder
WORKDIR /app

# Copy all the project into `app`
COPY . /app

# Create a conda environment
RUN conda create -n docker

# Install dependencies listed in requirements.txt with conda-forge as channel, 
# inside the environment  previously
RUN conda install --yes --file requirements.txt --channel conda-forge -n docker

# Run flash in all 0.0.0.0 so Docker can actually forward the port
CMD ["flask", "run", "--host", "0.0.0.0"]