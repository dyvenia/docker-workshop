# Docker Workshop
Hello 👋 Welcome to the Docker Workshop. This is a repository containing two simple exercises, one for building and running a container using a Dockerfile and the other for building and running several containers using docker-compose. Hopefully this material serves as a good introduction to the basic of Docker.

# What is Docker?
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

This separation is possible due to containers. Containers are lightweight and contain everything needed to run the application, so you do not need to rely on what is currently installed on your own machine.

## How is a container created?
To be able to create and run a container, it requires a template to use in the form of an image. An image is built using a set of instructions that are defined in a Dockerfile.

## Why use Docker?
* No need to manage the dependencies
* Isolating the program from your machine
* End-result will “always” be the same
* Modularity
* Packaging
* Ease of running containers

## Essential Docker commands
* `docker pull [image_name]`: Pulls the requested image from the Docker Hub Container Image library.
* `docker build [Dockerfile_location] -t [created_img_name]`: Build an image from a Dockerfile. You can optionally specify the name of the image; by default, the name is randomly generated
* `docker run --name [created_cont_name] [img_name]`: Create and run a container using an image built previously.
* `docker-compose up`: Use the docker compose file in the current directory to spin up container(s). This essentially brings up the whole project.

## What is docker-compose?
Docker-compose is a tool for defining and running multi-container Docker applications. It allows you to spin up multiple Dockerfiles at once with a single command.

## Exercise Overview
### What will we be doing?
1) Simple Hello world app using Dockerfile
2) FastAPI and MkDocs with docker-compose

# Install Docker
* Install Docker Desktop from [this link](https://docs.docker.com/get-docker/)
* If you are unable to install Docker Desktop, refer to the following section of [this page](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) to install Docker CLI

# Workshop exercises
## Exercise 1: Simple Hello world app using Dockerfile
1) **Start up the command line prompt**
2) **Navigate to the directory with the exercise files:** using the `cd` command. The directory is called `Exercise_1`
3) **Build the image:** In this directory, we have the **Dockerfile** ready. Let us build it using this command:  
`docker build . -t exercise1`  
This command will take the Dockerfile we have in this directory and create an image named *exercise1* using it.
4) **Create and run the container:** Now, we need to run the image and create a container. Let us create a container called **Exercise1** using the following command:  
`docker run --name Exercise1 exercise1`
5) Verify if you can see a "Hello World!" message in the command prompt.
6) Open Docker Desktop, then navigate to **Containers/Apps**. There, you should be able to see a container called **Exercise1**.

## Exercise 2: FastAPI and MkDocs with docker-compose
1) **Build the images**: In this exercise, we will have 2 images to build: one located in `fastapi_src` and another in `mkdocs`.
    * Navigate using the `cd` command to `fastapi_src` and run:  
    `docker build . -f Dockerfile -t fastapi-ex`
    * Then, navigate using the `cd` command to `mkdocs` and run:  
    `docker build . -f Dockerfile -t mkdocs-ex`
2) **Spin up the containers using docker-compose**: With the images built, we can now create and start the containers.
    * Ensure you are in the `Exercise_2` directory. In this directory, there should be a `docker-compose.yaml` file.
    * Run `docker-compose up`
    * Open Docker Desktop, then navigate to **Containers/Apps**. There, you should be able to see an entry called called **exercise_2**.
    * Expand **exercise2**, and verify that **fastapi-ex** and **mkdocs-ex** exist there. This means that two containers were spun successfully.
    * For each container, open the page of each container.
    * Verify that you can view the success messages of each page respectively.