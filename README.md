# 📘 Project Documentation – Syrian Gov Services Platform

---

## 🗂️ Overview

This is a government service platform built for Syrian citizens, employees, and admins to manage appointments and official service requests. The platform supports both:
- Traditional HTML frontend (via Django templates)
- Modern REST API interface (via Django REST Framework + JWT auth)

The platform allows citizens to:
- Browse available services
- Submit digital requests
- Book appointment slots

Employees:
- Access and review submitted citizen requests
- Approve or reject appointments and service requests

Admins:
- View administrative dashboards
- Access statistics and modify requests/appointments as needed

---

## 🏗️ Project Structure

- `accounts/` → Handles registration, login (HTML + API)
- `users/` → Profiles, user redirection, dashboards
- `services/` → Requesting and managing government services
- `appointments/` → Booking and confirming appointment dates
- `templates/` → Frontend pages using Django Templates
- `api/` folders inside apps → Contain serializers, views, urls for API usage

---

## 🧑‍💻 User Roles
- **Citizen**: Register, log in, submit service requests, book appointments
- **Employee**: View/approve/edit citizen requests and appointments
- **Admin**: Full access to appointments and services (via dashboard), see statistics

---

## 🌐 HTML Frontend Features

### 🔸 Pages:
- `/` → Homepage
- `/register/` → Citizen registration form
- `/login/` → Login page
- `/logout/` → Logout redirect
- `/services/` → Browse list of available services
- `/service/request/` → Submit service request form
- `/booking/` → Book appointments
- `/my_appointments/` → View my appointments
- `/my-requests/` → View submitted service requests
- `/profile/` → Manage citizen profile
- `/employee/requests/` → Staff view of all service requests
- `/employee/dashboard/` → Employee dashboard with appointments
- `/admin/appointments/` → Admin dashboard
- `/admin/statistics/` → View summarized stats of appointments

---

## 🔐 Authentication (JWT API)

### 🔸 Register
**POST** `/api/accounts/api/register/`
```json
{
  "username": "ahmad",
  "password": "ahmad123",
  "national_id": "12345678900",
  "phone": "0999888777",
  "address": "دمشق"
}
```

### 🔸 Login
**POST** `/api/accounts/api/login/`
```json
{
  "username": "ahmad",
  "password": "ahmad123"
}
```
📥 Response contains `access` and `refresh` tokens.

### 🔸 Auth Header (for all protected requests)
```
Authorization: Bearer <access_token>
```

---

## 👤 User APIs

### 🔹 Get Profile
**GET** `/api/users/profile/`

### 🔹 Update Profile
**PUT** `/api/users/profile/update/`
```json
{
  "phone": "0933222111",
  "address": "حلب"
}
```

---

## 🧾 Service APIs

### 🔹 List All Services
**GET** `/api/services/`

### 🔹 Submit Service Request (Citizen only)
**POST** `/api/services/request/`
```json
{
  "service": 1,
  "full_name": "أحمد علي",
  "national_id": "12345678900"
}
```

### 🔹 My Requests (Citizen only)
**GET** `/api/services/my-requests/`

### 🔹 Employee - View All Requests
**GET** `/api/services/employee/requests/`

### 🔹 Employee - Update Request Status
**POST** `/api/services/employee/requests/<id>/update/`
```json
{
  "status": "مقبول"
}
```

---

## 📅 Appointments APIs

### 🔹 Book Appointment (Citizen)
**POST** `/api/appointments/booking/`
```json
{
  "date": "2025-08-01",
  "time": "11:00",
  "reason": "حجز موعد للحصول على جواز سفر"
}
```

### 🔹 My Appointments
**GET** `/api/appointments/my-appointments/`

### 🔹 Employee Appointments View
**GET** `/api/appointments/employee/`

### 🔹 Confirm Appointment
**POST** `/api/appointments/employee/confirm/<id>/`

### 🔹 Admin Edit Appointment
**PUT** `/api/appointments/admin/edit/<id>/`

---

## 🔒 API Permissions
- `IsAuthenticated`: Required for all endpoints (except login/register)
- `IsCitizen`: Citizen-only endpoints (profile, booking, request)
- `IsEmployee`: View/edit service/appointments
- `IsAdmin`: Dashboard access

---

## 🧪 Testing
- 🧰 Tools: Insomnia / Postman
- ✅ Tested all endpoints with sample users and roles

---

## ⚙️ Technologies Used

- **Language**: Python
- **Framework**: Django, Django REST Framework
- **Authentication**: JWT (SimpleJWT)
- **Database**: SQLite (can be swapped with PostgreSQL)
- **Frontend**: Django Templates + Tailwind CSS (customized)
- **API Testing**: Insomnia / Postman

---

📦 **Status**: MVP Complete
🔧 **Backend**: Django, DRF, JWT Auth
🎨 **Frontend**: Django Templates (HTML + Forms)
🚀 **Next**: Deploy on production, CI/CD, API Rate Limiting
