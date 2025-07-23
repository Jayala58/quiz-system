# quiz-system
# Quiz System (Python + SQLite)

This is a simple terminal-based Quiz App built using Python and SQLite. It asks multiple-choice questions and displays your score at the end. A leaderboard is also included to track top scores.

---

## 📁 Files Included

- `create_db.py` – Creates the `quiz.db` database and adds questions.
- `main.py` – Runs the quiz in the terminal.
- `quiz.db` – SQLite database file (auto-created).
- `scores.txt` – Stores user scores 

---

## ▶️ How to Run

1. **Run the database setup script**  
   This will create the database and add sample questions.

   ```
   python create_db.py
   ```

2. **Start the quiz**

   ```
   python main.py
   ```

---

## ✨ Features

- 10 multiple-choice questions (Python + SQL)
- 10-second timer for each question
- Shows correct/wrong answers
- Score is stored in a leaderboard
- Works in terminal (no external libraries needed)

---

## 💡 Example

```
Enter your name: Jaya

Question 1: What is the output of len([1, 2, 3])?
A. 2
B. 3
C. 4
D. Error
Your answer: b
Correct!

...

Final Score: 7 out of 10
```

---

## 🧑‍💻 Created By

**Jaya Lakshmi**

GitHub: [@Jayala58](https://github.com/Jayala58)
