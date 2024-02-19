## Installing Docker Engine and Docker Desktop

### Windows

Follow the instructions in the following article to install Docker on Windows:

- https://docs.docker.com/desktop/install/windows-install/

### Linux

Follow the instructions to install Docker Engine and Docker Desktop.

- https://docs.docker.com/engine/install/ubuntu/

- https://docs.docker.com/desktop/install/linux-install/

#### Testing Docker

Open the terminal and run the following command

```shell
docker version
```

You should get an output similliar to the screenshot below if the installation was successful.

![My-image](/home/c99/Pictures/Screenshots/successfull-docker-installation.png)

To test if you can successfully run images, enter the following command in your terminal.

```shell
docker container run hello-world
```

You should get the following output in your command line

![My Image](/home/c99/Pictures/Screenshots/hello-world.png)

An alternative test to check if docker engine is working, run the following command in your terminal. 

```shell
docker container run rancher/cowsay Hello
```

You should get the following image:

![My Image](/home/c99/Pictures/Screenshots/Screenshot%20from%202024-02-10%2022-54-57.png)

### Recommended Resources

- [Docker Desktop for Windows 10/11 Setup and Tips - YouTube](https://www.youtube.com/watch?v=rATNU0Fr8zs)

- [Get started with Docker containers on WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)
