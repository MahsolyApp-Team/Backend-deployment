# Mahsoly Backend API

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.133.0-009688.svg?logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 1. Project Title & Description

**Mahsoly** is an AI-powered agricultural backend API built with FastAPI. It provides functionalities for plant disease detection, crop recommendation, and fertilizer recommendation using external AI models hosted on Hugging Face spaces. It also includes robust user authentication with OTP-based verification, password management, and email notifications. This backend supports the core features of the Mahsoly agricultural application.

## 2. Features

* **User Authentication**: Register, login, and secure JWT-based session management.
* **OTP Verification**: Email-based OTP for account verification, password resets, and email changes.
* **AI Plant Disease Detection**: Upload an image of a plant to detect diseases and receive confidence scores (powered by Hugging Face models and Cloudinary for image hosting).
* **Crop Recommendation**: Receive crop suggestions based on environmental metrics (Nitrogen, Phosphorous, Potassium, temperature, humidity, pH, and rainfall).
* **Fertilizer Recommendation**: Get fertilizer suggestions based on soil type, crop type, and field conditions.
* **Scan History**: Stores a history of user scans, including image URLs, detected plant/disease names, and confidence scores.

## 3. Tech Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Database**: [SQLAlchemy](https://www.sqlalchemy.org/) (ORM), [Alembic](https://alembic.sqlalchemy.org/) (Migrations), PostgreSQL / SQLite
* **Authentication**: [Passlib](https://passlib.readthedocs.io/) (bcrypt), [Python-JOSE](https://github.com/mpdavis/python-jose) (JWT)
* **External Services**: 
  * [Cloudinary](https://cloudinary.com/) (Image hosting)
  * [Hugging Face Spaces](https://huggingface.co/) (AI Inference APIs)
* **Utilities**: HTTPX (async HTTP requests), Pydantic (data validation)

## 4. Installation

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mahsoly_app.git
   cd mahsoly_app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your configuration details. (Example based on the codebase):
   ```env
   DATABASE_URL=sqlite:///./mahsoly_app.db
   # or for PostgreSQL: postgresql://user:password@localhost:5432/mahsoly_db
   
   SECRET_KEY=your_jwt_secret_key
   CLOUDINARY_CLOUD_NAME=your_cloudinary_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
   
   # Add your SMTP credentials for OTP emails if applicable
   ```

5. **Run Database Migrations**
   ```bash
   alembic upgrade head
   ```

## 5. Usage

To start the development server, run:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### Key API Endpoints Example

* **Register a new user:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/auth/register" \
       -H "Content-Type: application/json" \
       -d '{"name": "John Doe", "email": "john@example.com", "password": "securepassword"}'
  ```

* **Detect Plant Disease:**
  Send a POST request to `/scan` with a Bearer token and an image file:
  ```bash
  curl -X POST "http://127.0.0.1:8000/scan" \
       -H "Authorization: Bearer <your_token>" \
       -F "file=@plant_image.jpg"
  ```

## 6. Project Structure

```text
Mahsoly/
├── .env                # Environment variables configuration
├── main.py             # FastAPI entry point & app configuration
├── models.py           # SQLAlchemy database models & Pydantic schemas
├── database.py         # Database connection setup
├── AI_models.py        # Endpoints for AI inferences (disease, crop, fertilizer)
├── Authentication.py   # User authentication endpoints (register, login, OTP)
├── security.py         # JWT and password hashing utilities
├── verify.py           # Dependency to get current user from token
├── upload.py           # Cloudinary image upload utility
├── email_utils.py      # Email sending utilities for OTP
├── alembic/            # Database migration scripts
├── alembic.ini         # Alembic configuration
└── requirements.txt    # Python dependencies
```

## 7. Contributing

We welcome contributions! To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bugfix (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request for review.

## 8. License

This project is licensed under the MIT License. *(Note: Ensure a `LICENSE` file is present in your repository's root directory to apply this license formally).*
