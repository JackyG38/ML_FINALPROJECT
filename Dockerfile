# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files into the container
COPY requirements.txt ./

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . app1.py
COPY . app2.py


# Expose the port that Streamlit uses
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app1.py", "--server.port=8501", "--server.address=0.0.0.0"]
