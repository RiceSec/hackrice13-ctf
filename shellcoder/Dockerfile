FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat python

RUN useradd -m hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./flag.txt /home/hacker
COPY ./shellcoder /home/hacker

RUN chmod 440 /home/hacker/flag.txt
RUN chmod 550 /home/hacker/shellcoder

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"stdbuf --output=0 /home/hacker/shellcoder"
