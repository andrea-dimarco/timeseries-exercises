FROM ubuntu:22.04
ENV TZ=Europe/Rome \
    DEBIAN_FRONTEND=noninteractive


# Ubuntu setup
RUN apt update -y && \
    apt install -y curl && \
    apt install -y ca-certificates curl gnupg && \
    apt install wget -y



# Install CONDA
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh -O /home/miniconda.sh && \
     /bin/bash /home/miniconda.sh -b -p /opt/conda
ENV PATH=/opt/conda/bin:$PATH
RUN conda init bash


# Install libraries
RUN conda install conda-forge::pyoptsparse -y
WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
