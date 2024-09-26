FROM geerlingguy/docker-ubuntu2204-ansible:latest

WORKDIR /betterdiscordpy
ENV PATH /snap/bin:$PATH

RUN apt update && apt install wget snapd squashfuse fuse flatpak -y

RUN flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
RUN flatpak install com.discordapp.Discord -y

RUN wget "https://discord.com/api/download?platform=linux&format=deb" -O discord.deb
RUN apt install ./discord.deb -y
RUN rm ./discord.deb

COPY . .
ADD docker/snap /usr/local/bin/snap

RUN systemctl enable snapd
STOPSIGNAL SIGRTMIN+3

ENTRYPOINT ["/lib/systemd/systemd"]