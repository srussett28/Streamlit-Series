# Use an official Python slim image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy application files into the container
COPY Streamlittest4.py .
COPY sandbox.db .  

# Copy images
COPY SQL-Database.png .
COPY turtles3.png .
COPY SQLCAT.png .
COPY BasicSQL.png .
COPY filtering.jpg .
COPY sorting.jpg .
COPY aggrgate.png .
COPY SQL-JOINS-Example-0.png .
COPY ZipperJoin.png .
COPY subqueries.png .
COPY operations.jpg .
COPY modification.png .
COPY index.png .
COPY transaction.png .
COPY views.jpg .
COPY trigger.png .
COPY CTE.png .
COPY windowfunctions.png .
COPY calendar.png .
COPY logic.png .

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "Streamlittest4.py", "--server.port=8501", "--server.address=0.0.0.0"]



