# https://hub.docker.com/r/rancher/k3s/tags
# https://github.com/k3s-io/k3s/blob/master/package/Dockerfile
FROM rancher/k3s:v1.26.2-k3s1

RUN (apk add --no-cache bash curl python3 sudo || (apt-get update && apt-get install -y bash curl python3 sudo)) || true

COPY server.sh /server.sh
RUN chmod +x /server.sh

ENTRYPOINT []
CMD [ "/server.sh" ]
