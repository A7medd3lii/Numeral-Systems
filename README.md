# Number_Converter Wep-app

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

1. Clone the repository:
 Install the dependencies:

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
python test_main.py
```

### Dockerizing the Application

To build the Docker image, run:

```bash
docker build -t number-converter-app .
```

To run the Docker container, execute:

```bash
docker run -p 8080:8080 number-converter-app
```
