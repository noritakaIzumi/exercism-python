FROM gitpod/workspace-python-3.9

USER gitpod

# Upgrade pip self
RUN pip install --upgrade pip

# Install pip packages
COPY requirements.txt .
RUN pip install -r requirements.txt
