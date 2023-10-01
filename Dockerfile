# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 for the Flask web application
EXPOSE 5000

# Set the environment variables for Flask and HF_TOKEN
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV HF_TOKEN="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"

# Run the command to start the Flask web application
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD [ "python3", "src/app.py" ]