FROM python:3.7-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

RUN pip install \
    dagster \
    dagster-postgres \
    dagster-docker

# Add repository code

WORKDIR /opt/dagster/app

COPY . /opt/dagster/app

RUN pip install --upgrade pip

RUN pip install -e ".[dev]"

# Run dagster gRPC server on port 5000

EXPOSE 5000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "5000", "-f", "repo.py"]