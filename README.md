
# AutoPylet

Your end 2 end Python Software Engineer, Data Scientist , Automation Engineer , DevOps Engineer etc.

## Prerequisites

- Python>=3.10.x
- `virtualenv`
- `git-lfs`
- `make`

## Setup

### Create Virtual Environment

To create a virtual environment, run:

```sh
make getenv
```

### Install Dependencies

To install the required dependencies listed in `requirements.txt`, run:

```sh
make install
```

## Package Management

### Add a Package

To add a new package and update `requirements.txt`, run:

```sh
make add pkg=<package-name>
```

Replace `<package-name>` with the actual name of the package you want to add.

## Running the Application

To run the application, use:

```sh
make run prompt="<your-prompt>"
```

Replace `<your-prompt>` with the actual prompt you want to pass to `pylet.py`.

## Model Management

### Download Pre-trained Model

To download the pre-trained model from Hugging Face, run:

```sh
make getmodel
```

## Code Quality

### Linting

To lint the Python files using `pylint`, run:

```sh
make lint
```

### Formatting

To format the Python files using `black`, run:

```sh
make format
```
