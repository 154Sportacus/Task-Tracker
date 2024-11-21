# Task Manager CLI

A simple command-line task manager written in Python. This program allows you to create, update, delete, and manage tasks through a basic CLI interface. Tasks are stored in a JSON file, which ensures persistence across program runs.

## Features

- **Add tasks**: Create a new task with a description.
- **Update tasks**: Modify the description of an existing task.
- **Delete tasks**: Remove a task from the system.
- **Mark tasks as in-progress or done**: Change the status of a task.
- **List tasks**: View tasks filtered by status (todo, in-progress, done) or all tasks.
- **Persistent storage**: Tasks are saved to a `tasks.json` file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/154Sportacus/task-manager-cli.git
    ```

2. Navigate into the project directory:

    ```bash
    cd task-manager-cli
    ```

3. Ensure you have Python installed (version 3.x recommended).

4. No additional dependencies are required.

## Usage

### Running the program

To run the Task Manager CLI, execute the `task_tracker_cli.py` script:

```bash
python3 task_tracker_cli.py
