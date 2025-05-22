# Personal Portfolio Website

This is a simple personal portfolio website built with Flask.

## Setup and Running

1.  **Clone the repository.**
2.  **Navigate to the `module_1` directory:**
    ```bash
    cd module_1
    ```
3.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the application:**
    ```bash
    python run.py
    ```
6.  Open your web browser and go to `http://127.0.0.1:8000/`

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

## Screenshots

[Home](screenshots/Home.pdf)

[Contact](screenshots/Contact.pdf)

[Projects](screenshots/Projects.pdf)

