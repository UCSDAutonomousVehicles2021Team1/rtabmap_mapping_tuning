# Base image
FROM ros:melodic-robot-bionic

USER root


# Update apt repo and pip2, and install python3, pip3
RUN apt-get update --fix-missing && \
    apt-get install -y python-pip \
                       python3-dev \
                       python3-pip \
                       git \
                       build-essential \
                       cmake \
                       vim \
                       wget
                       
# Upgrade pip
RUN pip3 install --upgrade pip

RUN \
   echo 'alias python="/usr/bin/python3"' >> /root/.bashrc && \
   echo 'alias pip="/usr/bin/pip3"' >> /root/.bashrc && \
   source /root/.bashrc

RUN pip3 install --no-cache-dir numpy \
                                scipy \
                                pandas \
                                pyyaml \
                                rospkg \
                                notebook \
                                matplotlib \
                                seaborn
# Cloning
RUN /bin/bash -c "cd /; wget https://raw.githubusercontent.com/ucsd-ets/datahub-base-notebook/master/scripts/run_jupyter.sh; chmod 755 run_jupyter.sh"
WORKDIR /tmp
RUN /bin/bash -c "git clone https://github.com/sisaha9/slamevaluations.git"
