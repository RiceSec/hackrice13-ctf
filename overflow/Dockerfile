FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat

RUN useradd -m hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./flag.txt /home/hacker
COPY ./lecture.txt /home/hacker
COPY ./overflow /home/hacker

RUN chmod 440 /home/hacker/flag.txt /home/hacker/lecture.txt
RUN chmod 550 /home/hacker/overflow

CMD socat TCP-LISTEN:8000,reuseaddr,fork,crnl EXEC:"stdbuf --output=0 /home/hacker/overflow"
