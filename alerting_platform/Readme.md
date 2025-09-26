# Alerting Notification Platform

## Overview

This project is a robust, extensible **Alerting & Notification System** designed for enterprise use—built as a company assignment to demonstrate strong backend skills, clean architecture, and scalable feature development. It enables administrators to schedule and manage alerts across organizations, specific teams, and individual users with frequency controls and delivery channels.

---

## Features

- **Admin Dashboard:** Secure login, intuitive UI for alert creation and management.
- **Alert Scheduling:** Admins set start time, expiry, and custom reminder frequency (default: every 2 hours, configurable).
- **Visibility Control:** 
  - Whole organization
  - Specific teams (e.g., Engineering, Marketing)
  - Specific users
- **Severity Levels:** Info, Warning, Critical with clear badge indicators.
- **Reminder System:** Periodic reminders sent until alerts are snoozed or expired.
- **Extensible Delivery Channels:** In-app, Email, SMS, and Push Notification ready.
- **Role-based Access:** Only admins/staff can configure and manage platform-wide features.

---

## Setup Instructions

### Requirements
- Python 3.13+
- Django 5.x
- SQLite (default; can be swapped for other DBs)
- Node.js or yarn (only if using SCSS/CSS build tools)

### Installation

1. **Clone the repository**  