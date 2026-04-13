# Use official Python image
FROM python3.10

# Set working directory
WORKDIR app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Run the app using gunicorn (Cloud Run requirement)
CMD exec gunicorn --bind :$PORT sample_api:app
