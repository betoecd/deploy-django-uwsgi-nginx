FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./localhost.crt /etc/nginx/certs/localhost.crt
COPY ./localhost.key /etc/nginx/certs/localhost.key

USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static
RUN chown -R nginx:nginx /etc/nginx/certs/

USER nginx
