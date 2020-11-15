# Base image
FROM osrf/ros:melodic-desktop-full

USER root


# Update apt repo and pip2, and install python3, pip3
RUN apt-get update --fix-missing && \
    apt-get install -y python-pip \
                       python3-dev \
                       python3-pip

# Install apt dependencies, add your apt dependencies to this list
RUN apt-get install -y git \
                       build-essential \
                       cmake \
                       vim \
                       ros-melodic-genpy \
                       ros-melodic-rtabmap \
                       ros-melodic-rtabmap-ros \

# Upgrade pip
RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir numpy==1.16.0 \
                                scipy==1.2.0 \
                                pyyaml \
                                rospkg

RUN /bin/bash -c "git clone https://github.com/sisaha9/slamevaluations.git; source /opt/ros/melodic/setup.bash"
