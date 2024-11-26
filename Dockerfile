# Use the Amazon Linux 2 as the base image for Lambda
FROM public.ecr.aws/lambda/python:3.9

# Set environment variables correctly
ENV LAMBDA_TASK_ROOT=/var/task

# Update yum and install necessary system dependencies
RUN yum update -y && \
    yum install -y \
    gcc \
    gcc-c++ \
    python3-devel \
    make \
    cmake \
    openssl-devel \
    libffi-devel \
    tar \
    zip \
    unzip \
    lapack-devel \
    blas-devel \
    which && \
    yum clean all

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install numpy first to resolve potential issues
RUN pip install numpy==1.23.3

# Copy the requirements file into the container
COPY requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt

# Install Python dependencies
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt -t ${LAMBDA_TASK_ROOT}/

# Copy the model into the container
COPY models/laser_pycaret_pipeline.pkl ${LAMBDA_TASK_ROOT}/model/ilaser_pycaret_pipeline.pkl

# Copy the application script into the container
COPY app/lambda.py ${LAMBDA_TASK_ROOT}/lambda_function.py

# Set the CMD to your handler
CMD ["lambda_function.lambda_handler"]