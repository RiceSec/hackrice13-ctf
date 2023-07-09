FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat python python-pip
RUN pip install openai --break-system-packages

RUN useradd -m hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./duckspeak.py /home/hacker

RUN chmod 550 /home/hacker/duckspeak.py

CMD socat TCP-LISTEN:8000,reuseaddr,fork,max-children=5 EXEC:"stdbuf --output=0 /home/hacker/duckspeak.py"
