FROM alpine:3

RUN apk --update --no-cache add bash~="5" python3~="3" && rm -rf /var/cache/apk/*

ENV USER jktest
ENV UID 1001
ENV GROUP jktest
ENV GID 1001
ENV HOME /home/$USER

RUN addgroup -g $GID -S $GROUP && adduser -u $UID -S -G $GROUP -h $HOME -s /bin/bash $USER 

COPY src/* $HOME/bin/
RUN chown -R $USER:$GROUP $HOME && chmod 555 $HOME/bin/*

# Run as non-root
USER $UID:$GID
WORKDIR $HOME

CMD ["sleep", "infinity"]
