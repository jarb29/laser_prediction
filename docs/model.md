# Project Overview

Welcome to our AWS Lambda-based machine learning project. This project leverages a suite of technologies and tools, including PyCaret for machine learning, Docker for containerization, and AWS Lambda for scalable, serverless computing.

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Project Structure](#project-structure)
4. [Setup and Deployment](#setup-and-deployment)
    - [Prerequisites](#prerequisites)
    - [Building the Docker Image](#building-the-docker-image)
    - [Deploying to AWS Lambda](#deploying-to-aws-lambda)
5. [Usage](#usage)
6. [Contributions](#contributions)
7. [License](#license)

## Introduction

The purpose of this project is to create a scalable and efficient machine learning service using AWS Lambda. The service predicts outcomes based on input data by leveraging a pre-trained machine learning model created with PyCaret. Docker is used to containerize the application, making it easier to deploy and manage.

## Technologies

The following technologies and tools are used in this project:

- **PyCaret**: A low-code machine learning library that automates the entire machine learning workflow.
- **Docker**: A platform for developing, shipping, and running applications inside containers.
- **AWS Lambda**: A serverless compute service that runs your code in response to events and automatically manages the underlying compute resources.
- **Amazon Elastic Container Registry (ECR)**: A fully-managed Docker container registry that makes it easy to store, share, and deploy container images.
- **AWS CLI**: A unified tool to manage AWS services from the command line.

## Project Structure
├── artifacts 
│ └── models 
│ └── laser_pycaret_pipeline.pkl 
├── app 
│ └── lambda.py 
├── .dockerignore 
├── Dockerfile 
├── requirements.txt 
└── README.md

- **artifacts/models/**: Directory containing the machine learning model.
- **app/lambda.py**: Main Python script for the AWS Lambda function.
- **Dockerfile**: Defines the Docker image for the Lambda function.
- **requirements.txt**: Lists the Python dependencies required by the project.
- **README.md**: This documentation file.

## Setup and Deployment

### Prerequisites

- Docker installed locally.
- An AWS account with permissions to create and manage AWS Lambda functions.
- AWS CLI configured with your AWS credentials.

### Building the Docker Image

To build the Docker image, run the following command in the root directory of the project:

```sh
docker build -t my-ml-service .
```

### Deploying to AWS Lambda

1. **Push Docker Image to Amazon ECR**:
    - Authenticate Docker to your Amazon ECR registry:
      ```sh
      aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<region>.amazonaws.com
      ```
    - Create an ECR repository:
      ```sh
      aws ecr create-repository --repository-name my-ml-service
      ```
    - Tag the Docker image:
      ```sh
      docker tag my-ml-service:latest <your-account-id>.dkr.ecr.<region>.amazonaws.com/my-ml-service:latest
      ```
    - Push the Docker image:
      ```sh
      docker push <your-account-id>.dkr.ecr.<region>.amazonaws.com/my-ml-service:latest
      ```

2. **Create the Lambda Function**:
    - Create the Lambda function using the container image:
      ```sh
      aws lambda create-function --function-name my-ml-service \
      --package-type Image \
      --code ImageUri=<your-account-id>.dkr.ecr.<region>.amazonaws.com/my-ml-service:latest \
      --role arn:aws:iam::<your-account-id>:role/<your-lambda-role>
      ```

## Usage

Once deployed, the AWS Lambda function can be invoked using the AWS Lambda Console, AWS CLI, or programmatically via an API Gateway. The function expects input data in JSON format, and will return a prediction based on the PyCaret model.

### Sample Input

```json
{
  "body": "{\"Longitude Corte (m)\": 123.456, \"Espesor\": 78.9}"
}
```

### Sample Output

```json
{
  "statusCode": 200,
  "body": "{\"prediction\": [1]}"
}
```

## Contributions

Contributions to the project are welcome! Please create a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.