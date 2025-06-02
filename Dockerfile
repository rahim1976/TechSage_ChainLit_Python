# Use a Python 3.7 base image which is compatible with TensorFlow 1.15.5
FROM python:3.7-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install your Python dependencies
# --no-cache-dir saves space
# --upgrade pip ensures you have a recent pip to handle installations
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that Chainlit will run on. Render provides $PORT, which we'll use in the command.
# Chainlit defaults to 8000, so we'll expose that.
EXPOSE 8000

# This is the command that Render will execute to start your application.
# It uses the $PORT environment variable that Render injects.
CMD ["chainlit", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]