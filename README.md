# AI Chatbot Bhagavad Gita

This project is an AI chatbot that answers user's queries and life problems by quoting examples from The Bhagavad Gita using Meta's Llama 2 model. The backend is deployed on Azure using Docker.

## Project Structure

The project has the following files:

- `src/app.py`: This file is the entry point of the application. It creates an instance of the Flask app and sets up routes and handlers.
- `src/bot.py`: This file exports a class `BhagavadGitaBot` which has a method `get_response` that handles the user's queries and returns a response by quoting examples from The Bhagavad Gita using Meta's Llama 2 model.
- `Dockerfile`: This file is used to build a Docker image of the application. It specifies the base image, copies the source code, installs dependencies, and sets the entry point.
- `requirements.txt`: This file lists the Python dependencies required by the application.
- `README.md`: This file contains the documentation for the project.

## Usage

To use the chatbot, run the Docker container and navigate to `http://localhost:5000` in your web browser. The chatbot interface will be displayed and you can start interacting with it.

## Dependencies

The project requires the following dependencies:

- Flask
- Transformers
- Torch
- Accelerate

These dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

## Acknowledgements

This project was inspired by the teachings of The Bhagavad Gita and the work of Meta's Llama 2 model.



## Docker Commands

```bash
docker build -t my-flask-app .
docker tag my-flask-app my-container-registry.azurecr.io/my-flask-app:v1
```

```bash
docker login my-container-registry.azurecr.io
docker push my-container-registry.azurecr.io/my-flask-app:v1
```


To deploy your Docker container on Azure, you can follow these steps:

Create a new Azure Container Registry by following these steps:

a. Go to the Azure portal and click on "Create a resource".

b. Search for "Container Registry" and select "Container Registry" from the results.

c. Click on "Create" to create a new Container Registry.

d. Fill in the required details such as the name, subscription, resource group, and SKU.

e. Click on "Review + create" and then click on "Create" to create the Container Registry.

Build and tag your Docker image using the docker build and docker tag commands:

In this example, the -t option specifies the name of the Docker image, and the . specifies the build context. The docker tag command tags the Docker image with the name of your Azure Container Registry and a version number.

Push your Docker image to your Azure Container Registry using the docker push command:

In this example, the docker login command logs you in to your Azure Container Registry, and the docker push command pushes your Docker image to the registry.

Create a new Azure Web App for Containers by following these steps:

a. Go to the Azure portal and click on "Create a resource".

b. Search for "Web App for Containers" and select "Web App for Containers" from the results.

. Click on "Create" to create a new Web App for Containers.

d. Fill in the required details such as the name, subscription, resource group, and operating system.

e. Under "Container settings", select "Azure Container Registry" as the source type, and select your Azure Container Registry and Docker image.

f. Click on "Review + create" and then click on "Create" to create the Web App for Containers.

Configure your Flask web application on Azure by following these steps:

a. Click on "Configuration" in the left-hand menu.

b. Add a new application setting with the key PORT and the value 80.

c. Add a new application setting with the key WEBSITE_PYTHON_VERSION and the value 3.8.

d. Add a new application setting with the key WEBSITE_WSGI_HANDLER and the value app.app.

e. Click on "Save" to save the configuration changes.

