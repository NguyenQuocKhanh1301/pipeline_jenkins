FROM jenkins/inbound-agent:latest
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv docker.io
USER jenkins
