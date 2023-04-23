FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY flask_app/* ./

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port that the application will run on
EXPOSE 8080

# Run the command to start the WSGI server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]