
layout: post
title: Docker cheat sheet
date: 2017-02-07 09:11
categories:
- A note
tags:
- Docker
author: Jason
---
<p><strong><em>Docker cheet sheet</em></strong></p>

# Containers
 * `docker create` creates a container but does not start it.
 * `docker rename` allows the container to be renamed.
 * `docker run` **creates and starts a container in one operation.**
 * `docker rm` **deletes a container.**
 * `docker update` updates a container's resource limits.
 * `docker start` starts a container so it is running.
 * `docker stop` stops a running container.
 * `docker restart` stops and starts a container.
 * `docker pause` pauses a running container, "freezing" it in place.
 * `docker unpause` will unpause a running container.
 * `docker wait` blocks until running container stops.
 * `docker kill` sends a SIGKILL to a running container.
 * `docker attach` will connect to a running container.
 * `docker ps` shows running containers.
 * `docker logs` gets logs from container. (You can use a custom log driver, but logs is only available for json-file and journald in 1.10).
 * `docker inspect` looks at all the info on a container (including IP address).
 * `docker events` gets events from container.
 * `docker port` shows public facing port of container.
 * `docker top` shows running processes in container.
 * `docker stats` shows containers' resource usage statistics.
 * `docker diff` shows changed files in the container's FS.
 * `docker ps -a` **shows running and stopped containers.**
 * `docker stats --all` shows a running list of containers.

# Images
* `docker images` **shows all images.**
* `docker import` creates an image from a tarball.
* `docker build` **creates image from Dockerfile.**
* `docker commit` creates image from a container, pausing it temporarily if it is running.
* `docker rmi` **removes an image.**
* `docker load` loads an image from a tar archive as STDIN, including images and tags (as of 0.7).
* `docker save` saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions.
* `docker history` shows history of image.
* `docker tag` **tags an image to a name (local or registry).**

# Registry & Repository
* `docker login` to login to a registry.
* `docker logout` to logout from a registry.
* `docker search` searches registry for image.
* `docker pull` pulls an image from registry to local machine.
* `docker push` pushes an image to the registry from local machine.

# Dockerfile
* `FROM` Sets the Base Image for subsequent instructions.
* `MAINTAINER` Set the Author field of the generated images..
* `RUN` execute any commands in a new layer on top of the current image and commit the results.
* `CMD` provide defaults for an executing container.
* `EXPOSE` informs Docker that the container listens on the specified network ports at runtime. NOTE: does not actually make ports accessible.
* `ENV` sets environment variable.
* `ADD` copies new files, directories or remote file to container. Invalidates caches. Avoid ADD and use COPY instead.
* `COPY` copies new files or directories to container.
* `ENTRYPOINT` configures a container that will run as an executable.
* `VOLUME` creates a mount point for externally mounted volumes or other containers.
* `USER` sets the user name for following RUN / CMD / ENTRYPOINT commands.
* `WORKDIR` sets the working directory.
* `ARG` defines a build-time variable.
* `ONBUILD` adds a trigger instruction when the image is used as the base for another build.
* `STOPSIGNAL` sets the system call signal that will be sent to the container to exit.
* `LABEL` apply key/value metadata to your images, containers, or daemons.

# Volumnes
* `docker volume create`
* `docker volume rm`
* `docker volume ls`
* `docker volume inspect`

# Prune (Docker 1.13)
* `docker system prune`
* `docker volume prune`
* `docker network prune`
* `docker container prune`
* `docker image prune`
