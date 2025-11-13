# Prompt Library

A simple Flask application for managing a library of prompts.

## Overview

This application allows users to perform CRUD (Create, Read, Update, Delete) operations on a collection of prompts stored in a SQLite database.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   ```bash
   flask init-db
   ```

## Running the Application

To run the application, use the following command:
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000`.

## Running the Tests

To run the unit tests, use the following command:
```bash
pytest
```

## API

The application exposes the following endpoints:

*   `GET /`: Displays a list of all prompts.
*   `GET /add`: Displays a form to add a new prompt.
*   `POST /add`: Adds a new prompt to the database.
*   `GET /prompt/<int:prompt_id>`: Displays a single prompt.
*   `GET /edit/<int:prompt_id>`: Displays a form to edit a prompt.
*   `POST /edit/<int:prompt_id>`: Updates a prompt in the database.
*   `POST /delete/<int:prompt_id>`: Deletes a prompt from the database.
