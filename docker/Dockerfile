# Blue/green demo image for the ECS CodeDeploy scenario.
# Built twice with a different COLOR build-arg to produce the :blue and :green tags.
FROM nginx:alpine

ARG COLOR=BLUE
RUN printf 'VERSION=%s\n' "$COLOR" > /usr/share/nginx/html/index.html

EXPOSE 80
