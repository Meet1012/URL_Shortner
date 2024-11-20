# 🌐✂️ Django URL Shortener

[![Django](https://img.shields.io/badge/Django-4.0%2B-brightgreen)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

A Django-based web application for creating, retrieving, updating, and deleting shortened URLs. This app provides functionalities to map long URLs to short codes, fetch original URLs using the short code, and manage the stored URLs.

[Project URL](https://roadmap.sh/projects/url-shortening-service)

## ✨ Features

- **Shorten URL**: Generate a short code for a given long URL.
- **Retrieve URL**: Fetch the original URL using the short code.
- **Update URL**: Update the original URL linked to a specific short code.
- **Delete URL**: Delete a URL and its corresponding short code.
- **Usage Statistics**: Count how many times a short URL is accessed.

---

## 📋 Prerequisites

- Python 3.x
- Django 4.x or above
- Hashlib library (comes pre-installed with Python)

---

## ⚙️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/url-shortener.git
   cd url-shortener
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```
    python manage.py runserver
    ```

## 🖱️ Usage

### Shorten URL
1. Navigate to `/` (Home page).
2. Enter the long URL in the provided input field and click **Submit**.
3. If successful, a shortened URL will be displayed.

### Retrieve URL
1. Navigate to `/fetch/` (Fetch page).
2. Enter the short code of the URL in the input field and click **Submit**.
3. If the short code exists, the original URL will be displayed along with the number of times it has been accessed.

### Update URL
1. Navigate to `/update/` (Update page).
2. Enter the short code and the new URL to associate with it.
3. Click **Submit**. If the short code exists, the URL will be updated, and the update time will be recorded.

### Delete URL
1. Navigate to `/delete/` (Delete page).
2. Enter the short code of the URL to delete.
3. Click **Submit**. If the short code exists, the URL will be removed from the database.

---

## 🗂️ Project Structure

- **Forms**: 
  - `Create_form`: Handles the creation of new URLs and short codes.
  - `Fetch_form`: Used for retrieving the original URL based on the short code.
  - `Edit_form`: Allows editing the original URL associated with a short code.
  - `Delete_form`: Facilitates the deletion of a URL-short code pair.
  
- **Models**:
  The `url_schema` model defines the structure of the database table for storing URLs and their metadata:
  ```
  from django.db import models

  class url_schema(models.Model):
      id = models.AutoField(primary_key=True)
      url = models.URLField()
      shortCode = models.CharField(max_length=10)
      count = models.IntegerField(default=0)
      createdAt = models.CharField(max_length=100)
      updatedAt = models.CharField(max_length=100)

      def __hash__(self) -> int:
          return hash((self.id, self.url, self.shortCode, self.createdAt, self.updatedAt))
    ```

### Templates:
- **`index.html`**: 
  - Displays a form for creating a shortened URL.
  - Provides feedback on the generated short URL upon successful submission.

- **`fetch.html`**: 
  - Contains a form for entering a short code to retrieve the original URL.
  - Displays the original URL and access count if the short code exists.

- **`update.html`**: 
  - Provides a form for updating the original URL linked to a short code.
  - Displays a status message upon successful or unsuccessful update.

- **`delete.html`**: 
  - Features a form for entering a short code to delete its associated URL.
  - Displays a confirmation or error message based on the action's result.

### CSS Styling:
All templates use a shared styling approach:
- Comic Sans MS font for a playful design.
- Form inputs styled for clarity and consistency.
- Buttons styled for prominence with hover effects.
- Aesthetic labels and clean layouts for user-friendly interaction.

---

## 🧭 Example Workflow 

1. **Create**:
    - Visit the home page.
    - Enter a long URL, submit, and receive a short code.
2. **Retrieve**:
   - Navigate to the **Fetch URL** page.
   - Enter the short code in the form and submit.
   - The original URL, along with the number of times it has been accessed, is displayed if the short code is valid.

3. **Update**:
   - Go to the **Update URL** page.
   - Enter the short code and the new URL to associate with it.
   - Submit the form to update the record. A status message indicates success or failure.

4. **Delete**:
   - Visit the **Delete URL** page.
   - Enter the short code in the form and submit.
   - A confirmation message is displayed if the record is successfully deleted.

---

## 🛢️ Database Schema

The application uses the following schema to manage URLs:

| Field        | Type         | Description                                   |
|--------------|--------------|-----------------------------------------------|
| `id`         | AutoField    | Unique identifier for each record.           |
| `url`        | URLField     | The original long URL.                       |
| `shortCode`  | CharField    | A 6-character hash representing the short URL. |
| `count`      | IntegerField | Tracks the number of times the short URL is accessed. |
| `createdAt`  | CharField    | Timestamp when the record was created.       |
| `updatedAt`  | CharField    | Timestamp when the record was last updated.  |

---

## 🚨 Error Handling

- **Duplicate URLs**: If a URL already exists, its short code is retrieved instead of creating a duplicate entry.
- **Invalid Short Codes**: Fetch, update, or delete operations on nonexistent short codes return appropriate error messages.
- **Form Validation**: Ensures that input data meets requirements for URL format and field constraints.

---


