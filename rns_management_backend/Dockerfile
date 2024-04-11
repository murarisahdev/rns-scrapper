# Use the official Python image as base
FROM python:3.10-alpine

WORKDIR /app

# Copy requirements.txt to container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /app/

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy the Django project files to the container
COPY . .

# Expose port 8000 for Django development server
EXPOSE 8000

# Run Django development server
ENTRYPOINT ["./entrypoint.sh"]
