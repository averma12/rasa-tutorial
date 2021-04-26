FROM rasa/rasa-sdk:latest

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN apt-get update -qq && \
    apt-get install -y sudo && \
    apt-get install -y vim && \
    apt-get install -y python3-dev && \
    apt-get install -y gcc

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
