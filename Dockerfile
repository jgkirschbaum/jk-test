FROM alpine:3

RUN apk --update --no-cache add bash~="3" && rm -rf /var/cache/apk/*

ENV USER jktest
ENV UID 1001
ENV GROUP jktest
ENV GID 1001
ENV HOME /home/$USER

RUN addgroup -g $GID -S $GROUP && adduser -u $UID -S $USER -G $GROUP -U $GROUP -s /bin/bash

COPY src/* $HOME/bin/
RUN chown -R $USER:$GROUP $HOME && chmod 555 $HOME/bin/*

# Run as non-root
USER $UID:$GID
WORKDIR $HOME

CMD ["sleep", "infinity"]