# State Government Education Management & Analytics System

## Overview

This project is a backend system built with Django and Django REST Framework to manage and analyze educational data across schools and Local Government Areas (LGAs).

It addresses a key challenge in Nigeria:

> Lack of centralized data for tracking student enrollment and academic performance.

---

## Features

### 🔐 Authentication & Roles

* Role-based access system:

  * Teachers
  * Principals
  * Ministry Officials
* Secure data access using Django permissions

---

### 🏫 Core Data Management

* Student management
* School management
* Exam records (WAEC / NECO)
* Subject-based results tracking

---

### 📡 API Endpoints

#### Students

```
GET /Analysis/Students/
POST /Analysis/Students/
GET /Analysis/Students/<id>/
PUT /Analysis/students/<id>/
DELETE /Analysis/students/<id>/
```

#### Exams / Results

```
GET /Analysis/Exams/
POST /Analysis/Exams/
GET /Analysis/Exams/<id>/
```

---

### 🔍 Filtering (Advanced Querying)

Supports dynamic filtering via query parameters:

```
GET /Analysis/Exams/?year=2024
GET /Analysis/Exams/?exam_type=WAEC
GET /Analysis/Exams/?subject=Mathematics
GET /Analysis/Exams/?lga=Ikeja
GET /Analysis/Exams/?year=2024&exam_type=NECO
```

✔ Case-insensitive filtering
✔ Relational filtering (Student → School → LGA)

---

### 📊 Analytics Endpoints

#### Performance Trends

```
GET /analytics/performance-trends/
```

Returns average student performance over time:

```json
[
  {"year": 2020, "average_score": 65.4},
  {"year": 2021, "average_score": 70.2}
]
```

#### With Filters:

```
/analytics/performance-trends/?exam_type=WAEC
/analytics/performance-trends/?subject=English
/analytics/performance-trends/?lga=Ikeja
```

---

## 🧠 Data Relationships

```
Exam → Student → School → LGA
```

This structure enables:

* Location-based analytics
* Performance comparison across regions

---

## ⚙️ Tech Stack

* Backend: Django
* API: Django REST Framework
* Database: PostgreSQL (via Supabase)
* Filtering: django-filter

---

## 🛠 Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd education-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create `.env` file:

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

---

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Seed Database

```bash
python manage.py seed_db
python manage.py seed_ex
```

---

### 7. Run Server

```bash
python manage.py runserver
```

---

## 🧪 Testing

Run tests:

```bash
python manage.py test
```

---

## ⚡ Performance Considerations

* Optimized queries using `select_related`
* Reduced database hits in analytics endpoints
* Structured for future caching (Redis integration)

---

## 🔐 Security

* Role-based access control
* Restricted data visibility per user role
* Secure API design using DRF permissions

---

## 📈 Future Improvements

* Redis caching for analytics endpoints
* Pagination for large datasets
* WAEC grading system (A1–F9)
* Dashboard frontend (React or Django templates)
* LGA ranking and comparison analytics

---

## 👩‍💻 Author

Jennifer Cosmas

---

## 📬 Submission Note

This project demonstrates:

* Scalable API design
* Data analytics using ORM aggregation
* Real-world problem solving in public-sector education

---
