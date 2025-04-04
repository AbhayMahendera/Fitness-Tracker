
# 🏋️‍♂️ Fitness Tracker App

The **Fitness Tracker App** is a Python-based application designed to help users track their fitness goals, log daily activities, and receive personalized food recommendations. It features secure user authentication, health metric calculations (BMI, BMR, TDEE), and structured data storage. This app is ideal for anyone looking to monitor and improve their health and fitness progress.

---

## ✨ Features

- **🔐 Secure Authentication** – Register and log in with bcrypt-hashed passwords.  
- **🧑‍💻 Profile Management** – Store personal details like age, weight, height, and activity level.  
- **📊 Health Metrics** – Automatically calculates:
  - **BMI** (Body Mass Index)
  - **BMR** (Basal Metabolic Rate)
  - **TDEE** (Total Daily Energy Expenditure)
- **📅 Daily Logs** – Track calories consumed, sleep hours, and stress levels.
- **🥗 Food Recommendations** – Personalized nutrition suggestions based on your metrics.
- **📈 Visualization** – View tabular reports of your health logs from the past 7 days.
- **🔄 Profile & Data Updates** – Edit your personal info or update logs anytime.

---

## 🛠 Tech Stack

| Library     | Purpose                                      |
|-------------|----------------------------------------------|
| `bcrypt`    | Secure password hashing                      |
| `json`      | Data storage (users, food data)              |
| `os`        | File and directory management                |
| `tabulate`  | Visual representation of health logs         |

---

## 📁 Project Structure

```
fitness_tracker/
├── data/
│   ├── users/              # Individual user data files
│   │   └── username.json   # Each user's profile and log data
│   ├── user_db.json        # Username & hashed password store
│   └── food_db.json        # Food items & nutrition info
├── auth.py                 # Signup, login, password hashing
├── calculations.py         # BMI, BMR, TDEE calculations
├── main.py                 # Entry point & app logic
├── recommendations.py      # Nutrition recommendations
├── utils.py                # Helpers: data fetch/update, logs
├── visualization.py        # Displays logs in table format
└── README.md               # This file
```

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure Python 3.x is installed, then install dependencies:

```bash
pip install bcrypt tabulate
```

### ▶️ Run the App

```bash
git clone https://github.com/AbhayMahendera/Fitness-Tracker
cd fitness-tracker
python main.py
```

---

## 🧭 Menu Options

### On Startup
- `Login` – Access your fitness profile.
- `Register` – Create a new account.
- `Exit` – Quit the app.

### After Logging In
- `Log Data` – Record daily calories, sleep, and stress.
- `View Logs` – Display last 7 days' health metrics.
- `Food Recommendations` – Get personalized suggestions.
- `Update Profile` – Modify your details (weight, height, etc.).
- `Visualization` – See your progress in table format.

---

## 🔍 Module Overview

### `auth.py`
Handles secure login/registration using bcrypt.

- `signup()` – Creates a new user account.
- `login()` – Verifies user credentials.
- `hash_password()` – Encrypts passwords.
- `verify_password()` – Validates password on login.

### `calculations.py`
Computes essential health metrics.

- `calculate_bmi()`
- `calculate_bmr()`
- `calculate_tdee()`

### `main.py`
Runs the interface and app logic.

- `main_menu()` – Main options.
- `run_app()` – Core app loop.

### `recommendations.py`
Gives food suggestions based on BMI/TDEE.

- `get_food_recommendations()`

### `utils.py`
Utility functions for user data management.

- `get_user_data()`
- `update_user_data()`
- `log_daily_activity()`

### `visualization.py`
Uses `tabulate` to display logs cleanly.

- `visualize_logs()`
- `visualize_metrics()`

---

## 📌 Future Improvements

- 🔗 **Database Integration** – Move to SQLite or MongoDB.  
- 📱 **Mobile App** – Build with React Native or Flutter.  
- 🔄 **API Integration** – Sync with devices like Fitbit/Apple Health.  
- 📉 **Advanced Analytics** – ML-based predictions and progress analysis.  
- 🧾 **Interactive Dashboard** – Build a GUI for visual insights.

---

## 📚 About This Project

This app was created as part of my learning journey with **Python**. I built it to apply real-world concepts like authentication, file handling, modular programming, and data visualization. It’s helped deepen my understanding of the language and solve a problem I care about—staying healthy!

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, make your changes, and open a pull request.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **bcrypt** – Secure password encryption  
- **tabulate** – Table display formatting  
- **Python** – The foundation of this project  

---

## 👤 Author

**Abhay Mahendera**  
📧 [abhaymahendera@gmail.com](mailto:abhaymahendera@gmail.com)

```

