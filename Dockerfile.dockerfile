# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to be accessible on the host
EXPOSE 8501

# Run Streamlit app when the container starts
CMD ["streamlit", "run", "Streamlittest4.py"]



