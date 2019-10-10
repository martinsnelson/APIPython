# FROM nginx
FROM nginx:1.12.2

# remove o arquivo nginx.conf padrao
RUN rm /etc/nginx/conf.d/default.conf

# substitui com o meu nginx.conf
COPY nginx.conf /etc/nginx/conf.d/