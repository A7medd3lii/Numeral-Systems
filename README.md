# Number_Converter Web-app

## Overview

The Number Converter Web Application is a simple and effective tool designed to convert decimal numbers into binary and hexadecimal formats. Built using Python and Flask, this application features a user-friendly interface and a professional design for an excellent user experience.

## Features

- Convert decimal numbers to binary and hexadecimal formats.
- Input validation to ensure correct data entry.
- Responsive and visually appealing design.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Deployment**: Flask development server, Docker

## Getting Started

### Prerequisites

- Python 3.9 or later
- pip (Python package installer)
- Docker (optional, for containerization)

### Installation

- Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the dependencies:

```bash
 pip install -r requirements.txt
```

### Running the Application

To run the application locally, execute:

```bash
python main.py
```

### Running Tests

To run the unit tests, execute:

```bash
python unittest test_main.py
```

### Dockerizing the Application

To build the Docker image, run:

```bash
docker build -t systems-number .
```

To run the Docker container, execute:

```bash
docker run -p 5000:5000 systems-number
```

### push docker image to docker hub

- step 1: login to docker hub

```bash
docker login
```

- step 2: build the docker image

```bash
docker build -t a7medd3lii/number-systems:v1.0 .

```

- step 3: push the docker image

```bash
docker push a7medd3lii/number-systems:v1.0
```

### Run ansible playbook

```bash
ansible-playbook -i hosts.ini main.yml
```

### Initialize terraform

```bash
terraform init
```

### Aplly terraform

```bash
terraform apply
```
