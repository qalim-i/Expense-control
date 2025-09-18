# Expense Control

Expense Control is a Django-based web application for managing and tracking personal expenses. It allows users to add, edit, and delete expenses, as well as view a list of all expenses. The project is structured with a main Django app and an 'expenses' app for expense management features.

## Features
- User registration and login
- Add, edit, and delete expenses
- View a list of expenses
- Simple, clean UI

## Project Structure
```
expense_control/
├── expense_control/        # Main Django project settings
├── expenses/              # App for expense management
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS)
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── tests.py           # Tests
│   ├── urls.py            # App URLs
│   └── views.py           # View functions
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore file
├── LICENSE                # Project license
└── README.md              # Project documentation
```

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (for cloning the repository)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd expense_control
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables (for production):**
   - Create a `.env` file or set the following variables in your environment:
     - `SECRET_KEY` (required for Django security)
     - `DEBUG` (set to `False` in production)
   - For development, the default settings in `settings.py` are sufficient, but do not use them in production.

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Register a new user or log in with existing credentials.
- Add, edit, or delete expenses from the dashboard.
- View your list of expenses.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For questions or support, please open an issue in the repository.
