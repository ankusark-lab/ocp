FROM registry.access.redhat.com/ubi8/python-39:latest

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# OpenShift uses port 8080 for non-root apps
EXPOSE 3333

CMD ["python", "app.py"]
