FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]