# 📋 Task Manager

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.1+-green.svg)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18-61dafb.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, responsive web application for managing tasks and comments built with React and Flask.

<img width="1900" height="925" alt="Image" src="https://github.com/user-attachments/assets/f00d0ad4-6b46-4f45-bd88-d0b8326428f3" />

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/task-manager.git
cd task-manager

# Backend setup
cd backend
pip install -r requirements.txt
python app.py

# Frontend (open in browser)
cd ../frontend
python -m http.server 8000
```

Visit `http://localhost:8000` to see the app in action!

## ✨ Features

- **Task Management**: Create, edit, and delete tasks with descriptions
- **Task Status**: Track tasks as pending, in-progress, or completed
- **Priority Levels**: Assign low, medium, or high priority to tasks
- **Filtering**: Filter tasks by status and priority
- **Comments System**: Add, edit, and delete comments for each task
- **Modern UI**: Clean, professional interface with gradient backgrounds and card layouts
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: AJAX-powered interface for smooth user experience
- **Error Handling**: User-friendly error messages and loading states
- **Input Validation**: Client and server-side validation with max length constraints
- **RESTful API**: Well-structured backend API with proper HTTP methods

## 🛠️ Technologies Used

### Frontend
- React 18
- Babel (for JSX compilation)
- Font Awesome (icons)
- CSS3 with modern styling

### Backend
- Flask (Python web framework)
- Flask-SQLAlchemy (ORM)
- Flask-CORS (Cross-Origin Resource Sharing)
- Marshmallow (Data validation)
- SQLite (Database)
- RESTful API design

## 📁 Project Structure

```
task-manager/
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
├── backend/
│   ├── app.py              # Main Flask application
│   ├── app.db              # SQLite database file
│   ├── config.py           # Application configuration
│   ├── models.py           # Database models
│   ├── requirements.txt    # Python dependencies
│   ├── schemas.py          # Data validation schemas
│   ├── .env.example        # Environment variables example
│   ├── routes/
│   │   ├── tasks.py        # Task-related API endpoints
│   │   └── comments.py     # Comment-related API endpoints
│   └── tests/
│       ├── conftest.py     # Test configuration
│       └── test_comments.py # Comment API tests
└── frontend/
    ├── index.html          # Main HTML file with React components
    ├── style.css           # Application styles
    └── config.js           # Frontend configuration
```

## 💻 Installation & Setup

### Prerequisites
- Python 3.7+
- A modern web browser

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Create a `.env` file for environment variables:
   ```bash
   cp .env.example .env
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```

The backend will start on `http://127.0.0.1:5000`

### Frontend Setup

1. Open `frontend/index.html` in your web browser, or serve it through a local server.

2. For development, you can use Python's built-in server:
   ```bash
   cd frontend
   python -m http.server 8000
   ```

Then navigate to `http://localhost:8000/index.html`

## 🔌 API Endpoints

### Tasks
- `GET /api/tasks` - Retrieve all tasks (supports pagination and filtering)
  - Query params: `page`, `per_page`, `status`, `priority`
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/<id>` - Get a specific task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

### Comments
- `GET /api/tasks/<task_id>/comments` - Get comments for a task
- `POST /api/tasks/<task_id>/comments` - Add a comment to a task
- `GET /api/tasks/<task_id>/comments/<comment_id>` - Get a specific comment
- `PUT /api/tasks/<task_id>/comments/<comment_id>` - Update a comment
- `DELETE /api/tasks/<task_id>/comments/<comment_id>` - Delete a comment

## 📖 Usage

1. **Adding Tasks**: Fill in the task form with title, description, status, and priority
2. **Filtering Tasks**: Use the status and priority dropdowns to filter tasks
3. **Editing Tasks**: Click the pencil icon to edit task details
4. **Viewing Comments**: Click the "Comments" button to view and manage comments
5. **Adding Comments**: Use the comment form in the comments panel
6. **Deleting Items**: Use the delete buttons with confirmation dialogs

## 🎯 Features Overview

- **Status Tracking**: Visual badges showing task status (pending, in-progress, completed)
- **Priority System**: Color-coded priority badges (low, medium, high)
- **Responsive Grid Layout**: Tasks and comments displayed in responsive grids
- **Interactive UI**: Hover effects, smooth transitions, and intuitive controls
- **Form Validation**: Client and server-side validation for required fields
- **Max Length Constraints**: Title (200), Description (2000), Author (120), Comment (1000)
- **Confirmation Dialogs**: Prevents accidental deletions
- **Loading States**: Visual feedback during API operations
- **Error Messages**: Clear error messages for failed operations
- **Pagination Support**: Backend supports paginated task retrieval

## 🔒 Security Features

- Input sanitization (trimming whitespace)
- Max content length restrictions
- CORS configuration
- Environment variable support for sensitive data
- SQL injection protection via SQLAlchemy ORM

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔮 Future Enhancements

- 🔐 User authentication and authorization
- 🏷️ Task categories and tags
- 📅 Due dates and reminders
- 🔍 Search capabilities
- 👥 Task assignment to users
- 📧 Email notifications
- 🌙 Dark mode support
- 📤 Export/import functionality

## 🐛 Known Issues

None at the moment. Please report any issues you find!

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ Star this repo if you find it helpful!
