FROM node:20-alpine

RUN npm install -g jupyter-book@2

WORKDIR /book

ENV HOST=0.0.0.0

EXPOSE 3000

CMD ["jupyter-book", "start", "--port", "3000", "--keep-host"]
