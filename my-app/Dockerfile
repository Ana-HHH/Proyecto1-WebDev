FROM node:19.0.1-alpine as build

WORKDIR /app/

COPY . .
# RUN  ls /app
RUN npm install
RUN npm run build
RUN echo "hello world!"
# CMD ["npm", "run", "build"]
FROM nginx:1.17.1-alpine
COPY --from=build /app/dist/my-app /usr/share/nginx/html
COPY /server/nginx.config /etc/nginx/conf.d/default.conf
EXPOSE 80

