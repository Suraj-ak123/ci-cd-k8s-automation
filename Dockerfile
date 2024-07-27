FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    netcat

COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

CMD ["/usr/local/bin/wisecow.sh"]
