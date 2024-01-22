# Use an official Python runtime as a parent image
FROM chltpdus48/github-actions-session

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run migrations and then start the server
# First, define the entrypoint script
ENTRYPOINT ["sh", "-c"]

# Then, define the command to execute
CMD ["python manage.py migrate --settings=config.settings.prod && python manage.py runserver 0.0.0.0:8000"]

