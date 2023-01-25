FROM node:alpine3.10
COPY . /Ds
WORKDIR /Ds
CMD node Trees/B-Tree.js