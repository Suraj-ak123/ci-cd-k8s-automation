# Use the official Ubuntu 20.04 as a base image
FROM ubuntu:24.04

# Install required packages
RUN apt update && apt install -y fortune-mod cowsay netcat-openbsd

ENV PATH="/usr/games:${PATH}"

# Copy the script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Set the default command to run the script
CMD ["/usr/local/bin/wisecow.sh"]
