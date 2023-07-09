FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat nodejs

RUN useradd -m hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./flag.txt /home/hacker
COPY ./main.mjs /home/hacker

RUN chmod 440 /home/hacker/flag.txt
RUN chmod 550 /home/hacker/main.mjs

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"stdbuf --output=0 /home/hacker/main.mjs"
