FROM node:8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --global  \
    resume-cli \
    jsonresume-theme-stackoverflow
RUN npm install js-yaml
COPY . /usr/src/app

CMD [ "node", "index.js" ]
