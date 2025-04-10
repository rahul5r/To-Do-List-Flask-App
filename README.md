# Flask To-Do List Application

A simple web application built with Flask to manage your daily tasks. Add, view, update, and delete tasks easily through a web interface.

## Description

This project is a basic Create, Read, Update, Delete (CRUD) application demonstrating the fundamentals of Flask web development. It allows users to maintain a list of tasks, mark them as complete, or remove them entirely. Task data is typically stored in a database (like SQLite).

*"This project was built as part of learning Flask and SQLAlchemy."*

## Features

* Add new tasks to the list.
* View all current tasks.
* Mark tasks as completed.
* Update tasks as you wish.
* Delete tasks from the list.
* Persistent storage of tasks.

## Technologies Used

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML, CSS
* **Templating:** Jinja2 (comes with Flask)
`
## Setup and Installation

Follow these steps to get the application running locally:

1.  **Prerequisites:**
    * Python 3.x installed (Preferably Python 3.12.10)
    * `pip` (Python package installer)
    * `git` (for cloning)

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/rahul5r/To-Do-List-Flask-App
    cd https://github.com/rahul5r/To-Do-List-Flask-App
    ```

3.  **Create and activate a virtual environment (Recommended):**
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
        ```bash
        python app.py
        ```

6.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

* Enter a task description in the input field and click "Add Task".
* Click the "Completed" button next to a task to mark it as finished.
* Click the "Update" button to update that task.
* Click the "Delete" button to remove a task permanently.

*(Adjust based on your actual UI elements and workflow)*

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request