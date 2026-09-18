FROM node:20-alpine

ARG UID=1000
ARG GID=1000

RUN apk add --no-cache shadow \
 && npm install -g jupyter-book@2

RUN deluser node 2>/dev/null || true \
 && delgroup node 2>/dev/null || true \
 && (groupadd -g ${GID} book 2>/dev/null || groupadd book) \
 && useradd -u ${UID} -g book -m -s /bin/sh book

WORKDIR /book

ENV HOST=0.0.0.0

EXPOSE 3000

USER book

CMD ["jupyter-book", "start", "--port", "3000", "--keep-host"]
