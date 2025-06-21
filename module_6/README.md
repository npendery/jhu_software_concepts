# Personal Portfolio Website in Docker

This is a simple personal portfolio website built with Flask and run in Docker

## Setup and Running

1.  **Clone the repository.**
2.  **Navigate to the `module_6` directory:**
    ```bash
    cd module_6
    ```
3.  **Build a Docker Image:**
    ```bash
    docker build . -t npendery/module_6
    ```
4.  **Run the Docker Image:**
    ```bash
    docker run -p 8080:8080 npendery/module_6
    ```
5.  Open your web browser and go to `http://127.0.0.1:8080/`

## Project Structure

-   `run.py`: Main Flask application file.
-   `requirements.txt`: Python package dependencies.
-   `pages/`: Blueprint module for different pages.
    -   `routes.py`: Defines the routes for the website.
-   `static/`: Contains static files (CSS, images).
    -   `style.css`: Main stylesheet.
    -   `profile.jpg`: Placeholder for your profile picture.
-   `templates/`: Contains HTML templates.
    -   `base.html`: Base template with navigation.
    -   `home.html`: Homepage template.
    -   `contact.html`: Contact page template.
    -   `projects.html`: Projects page template.
-   `Dockerfile`: Docker set up for project

## Link to dockerhub repository used in this module
https://hub.docker.com/repository/docker/npendery/module_6/general

## Screenshots

[Home](screenshots/Home.pdf)

[Contact](screenshots/Contact.pdf)

[Projects](screenshots/Projects.pdf)

[DockerContainer](screenshots/DockerContainer.pdf)
