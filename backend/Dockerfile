# Specify the base image
FROM python:3.9

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/backend/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/backend/requirements.txt

# Copy the rest of the application code
COPY . /code/backend

# Set the entrypoint command
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]
