FROM ubuntu:latest
LABEL authors="lucianistrati"

ENTRYPOINT ["top", "-b"]