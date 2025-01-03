# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and your app into the container
COPY requirements.txt .
COPY Streamlittest4.py .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit uses (default: 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "Streamlittest4.py", "--server.port=8501", "--server.enableCORS=false"]
