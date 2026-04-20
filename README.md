

***

```markdown
# Finance Tracker

A production-ready full-stack web application designed to track personal expenses, manage spending categories, and provide user-specific financial dashboards. 

Built with a robust, enterprise-grade architecture, this project features isolated development and production environments, secure media storage, and automated cloud deployment.

## 🚀 Features
* **Custom Authentication:** Secure login, logout, and user session management utilizing a custom `TrackerUser` model.
* **Expense Management:** Add, categorize, and track daily financial transactions.
* **Dynamic Categories:** Database-driven category assignment for precise financial filtering.
* **Media Management:** Secure upload and serving of user profile images and receipt attachments.
* **Environment-Aware Architecture:** Automated routing between local (SQLite/Local Storage) and production (PostgreSQL/Cloudinary) environments based on environment variables.

## 🛠️ Tech Stack
* **Backend:** Python, Django 4.2+
* **Database:** SQLite (Local) / PostgreSQL via Neon (Production)
* **Storage:** Cloudinary (Media files) / WhiteNoise (Static files)
* **Deployment & Hosting:** Render
* **Version Control:** Git, GitHub

## 🏗️ Architecture & Security
This project employs a secure "Master Switch" configuration in `settings.py`. It guarantees that local testing never accidentally overwrites live production data:
* **Track A (Development):** Utilizes a local SQLite database and local file system storage.
* **Track B (Production):** Automatically routes database connections to a remote Neon PostgreSQL cluster and delegates media storage to the Cloudinary API.

## 💻 Local Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/Rohan-malhotra555/solo-finance-tracker.git
cd finance-tracker
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**
Create a `.env` file in the root directory and add the following:
```ini
DEBUG=True
SECRET_KEY=your_secure_secret_key
DATABASE_URL=your_neon_postgresql_url
CLOUDINARY_URL=your_cloudinary_url
```

**5. Apply migrations and create a superuser**
```bash
python manage.py migrate
python manage.py createsuperuser
```

**6. Run the local development server**
```bash
python manage.py runserver
```

## ☁️ Cloud Deployment
This application is fully configured for automated deployment on Render. The production server securely injects environment variables (`DEBUG=False`) to trigger the PostgreSQL and Cloudinary production track. Static files are compressed, cached, and served efficiently via WhiteNoise.

---
*Developed by Rohan Malhotra*
```

***
