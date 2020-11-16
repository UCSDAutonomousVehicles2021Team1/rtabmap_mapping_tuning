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
                       ros-melodic-genpy \
                       ros-melodic-rtabmap \
                       ros-melodic-rtabmap-ros \
                       ros-melodic-gazebo-* \
                       ros-melodic-rviz
# Upgrade pip
RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir numpy==1.16.0 \
                                scipy==1.2.0 \
                                pyyaml \
                                rospkg \
                                notebook

# Cloning
RUN /bin/bash -c "git clone https://github.com/sisaha9/slamevaluations.git; source /opt/ros/melodic/setup.bash"
