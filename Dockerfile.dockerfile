FROM python:3.11-slim

WORKDIR /app

COPY Streamlittest4.py .
COPY requirements.txt .
COPY SQL-Database.png /app/SQL-Database.png
COPY turtles3.png /app/turtles3.png
COPY SQLCAT.png /app/SQLCAT.png
COPY BasicSQL.png /app/BasicSQL.png
COPY filtering.jpg /app/filtering.jpg
COPY sorting.jpg /app/sorting.jpg
COPY aggrgate.png /app/aggrgate.png
COPY SQL-JOINS-Example-0.png /app/SQL-JOINS-Example-0.png
COPY ZipperJoin.png /app/ZipperJoin.png
COPY subqueries.png /app/subqueries.png
COPY operations.jpg /app/operations.jpg
COPY modification.png /app/modification.png
COPY index.png /app/index.png
COPY transaction.png /app/transaction.png
COPY views.jpg /app/views.jpg
COPY trigger.png /app/trigger.png
COPY CTE.png /app/CTE.png
COPY windowfunctions.png /app/windowfunctions.png
COPY calendar.png /app/calendar.png
COPY logic.png /app/logic.png


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Streamlittest4.py"]

