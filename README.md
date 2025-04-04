Fitness Tracker App
The **Fitness Tracker App** is a Python-based application designed to help users track their fitness goals, log daily activities, and receive personalized food recommendations. This app provides features for secure user authentication, health metric calculations (BMI, BMR, TDEE), and storing user data in a structured format. It is ideal for anyone looking to monitor their health and fitness progress.

Features
 - **Secure Authentication**: Users can securely register with a hashed password and log in to access their profile and data.
 - **Profile Management**: Users can create and update their profile with personal details such as age, weight, height, and activity level.
 - **Health Metrics**: The app calculates and displays:
     - **BMI** (Body Mass Index)
     - **BMR** (Basal Metabolic Rate)
     - **TDEE** (Total Daily Energy Expenditure)
 - **Daily Logs**: Track daily activities, including calories consumed, sleep hours, and stress levels.
 - **Food Recommendations**: Based on health metrics, the app provides personalized food recommendations.
 - **Visualization**: View graphs of your health logs for the past 7 days to analyze trends.
 - **User Data Update**: Users can update their profile (e.g., height, weight, activity level) anytime.

Tech Stack
- **bcrypt**: For secure password hashing and verification.
- **json**: Used for storing user and food data in JSON format.
- **os**: For managing directories and file paths.
- **tabulate**: For displaying health logs in a table format for easy visualization.

File Structure
```
fitness_tracker/
├── data/
│   ├── users/              # User-specific data files
│   │   └── username.json   # JSON file for each user's data
│   ├── user_db.json        # Main user database (usernames and hashed passwords)
│   └── food_db.json        # Database for food recommendations
├── auth.py                 # User authentication (signup, login, password hashing)
├── calculations.py         # Functions for BMI, BMR, TDEE calculations
├── main.py                 # Main app logic (user interface, login, registration)
├── recommendations.py      # Provides food recommendations based on health data
├── utils.py                # Utility functions (fetching user data, daily log updates)
├── visualization.py        # Visualize user health logs (past 7 days)
└── README.md               # Project overview and instructions
```
How to Use
Prerequisites
Make sure you have **Python 3.x** installed on your machine. You will also need to install the required libraries by running:
```bash
pip install bcrypt tabulate
```

Running the Application
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/fitness-tracker.git
    cd fitness-tracker
    ```
2. Run the app:
    ```bash
    python main.py
    ```

Menu Options
Once you start the app, you'll see the following options:
 - **Login**: Enter your username and password to access your profile.
 - **Register**: Create a new account by providing a username, password, and personal details.
 - **Exit**: Close the application.
After logging in, you can choose from the following options:
 - **Log Data**: Record your daily activities such as calories consumed, sleep hours, and stress levels.
 - **View Logs**: View your health logs and metrics (e.g., calories, sleep, etc.) for the past week.
 - **Food Recommendations**: Get personalized food suggestions based on your health data.
 - **Update Profile**: Update your profile information (height, weight, activity level).
 - **Visualization**: View graphs of your health metrics and logs for the past 7 days.

Detailed File Descriptions
auth.py
Handles user authentication, including:
 - **Signup**: Prompts users to create an account by providing a username, password, and personal details.
   - Passwords are securely hashed using bcrypt.
   - User data is stored in JSON format under `data/users/` and in the global `data/user_db.json` file.
 - **Login**: Verifies user credentials by comparing the entered password with the hashed password stored in `user_db.json`.
 - **Password Hashing**: Uses bcrypt to hash passwords and ensure secure storage.
Functions:
 - `hash_password(password)`: Hashes the provided password using bcrypt.
 - `verify_password(entered_password, stored_hash)`: Verifies the entered password against the stored hash.
 - `signup()`: Registers a new user by collecting personal details and storing them in a JSON file.
 - `login()`: Handles user login and verifies credentials.

calculations.py
Contains functions for calculating health metrics:
 - **BMI** (Body Mass Index): Helps users understand whether they are underweight, normal weight, overweight, or obese.
 - **BMR** (Basal Metabolic Rate): The number of calories a person needs at rest to maintain basic bodily functions.
 - **TDEE** (Total Daily Energy Expenditure): The total number of calories a person burns in a day, considering activity levels.
Functions:
 - `calculate_bmi(weight, height)`: Computes BMI from weight and height.
 - `calculate_bmr(weight, height, age, gender)`: Computes BMR based on weight, height, age, and gender.
 - `calculate_tdee(bmr, activity_level)`: Computes TDEE based on BMR and the user's activity level.

main.py
The entry point for the application:
 - **User Interface**: Provides the main menu and allows users to choose options such as login, register, or exit.
 - **App Logic**: Handles user input and redirects to appropriate functions (e.g., login, signup, logging data).
Functions:
 - `main_menu()`: Displays the main menu options and calls the appropriate function based on user input.
 - `run_app()`: Starts the application and controls the flow of execution.

recommendations.py
Provides food recommendations based on a user's health data:
 - **Food Database**: Contains a list of food items and their respective nutritional values (calories, protein, fat, carbs).
Functions:
 - `get_food_recommendations(bmi, tdee)`: Suggests food based on the user's BMI and TDEE, helping them meet their fitness goals (e.g., weight loss or muscle gain).

utils.py
Utility functions that help with various operations within the app:
 - **User Data Management**: Functions to retrieve and update user data.
 - **Daily Log Updates**: Functions to record daily activities, including calorie intake, sleep, and stress levels.
Functions:
 - `get_user_data(username)`: Retrieves the user's data from the JSON file.
 - `update_user_data(username, data)`: Updates the user's data in the JSON file.
 - `log_daily_activity(username, activity_data)`: Records daily activities like calories consumed, sleep, and stress.

visualization.py
Generates visual reports of the user's health metrics and logs:
 - **Visualization**: Uses tabulate to display user health logs in a clean, readable table format.
Functions:
 - `visualize_logs(username)`: Displays a table of the user's health logs for the past 7 days.
 - `visualize_metrics(username)`: Displays the user's BMI, BMR, and TDEE metrics.

Future Improvements
While the app is fully functional, there are several areas for potential enhancement:
 - **Database Integration**: Integrate a relational or NoSQL database (e.g., SQLite or MongoDB) for more robust data storage and improved scalability.
 - **Mobile Application**: Develop a mobile version of the app using frameworks like **React Native** or **Flutter**, enabling users to track their fitness on-the-go.
 - **API Integration**: Integrate third-party APIs for additional features, such as syncing with wearable devices (e.g., Fitbit, Apple Health), or providing real-time food nutrition data.
 - **Advanced Analytics**: Add advanced analytics and machine learning models to track user progress over time and offer personalized fitness insights.
 - **User Dashboard**: Create an interactive user dashboard with detailed reports, progress tracking, and visual comparisons.

About the Project
This project was developed as part of my learning journey with **Python**. As I progressed in learning the language, I built this **Fitness Tracker App** to practice and apply my skills in real-world scenarios. The app covers key concepts such as file handling, user authentication, health calculations, and data visualization. This project has helped me deepen my understanding of Python and expand my problem-solving abilities.

Contributing
Contributions to this project are welcome! If you have suggestions, bug fixes, or improvements, feel free to fork this repository, create a new branch, and submit a pull request.

License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Acknowledgments
 - **bcrypt**: For providing secure password hashing.
 - **tabulate**: For helping generate user-friendly tables for health logs.
 - **Python**: For being the core language that powers this project.

Author
[Abhay Mahendera](abhaymahendera@gmail.com)

