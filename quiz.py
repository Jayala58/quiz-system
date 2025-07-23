import sqlite3
import time
import threading
import random
from datetime import datetime

def input_with_timeout(prompt, timeout):
    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\n⏰ Time's up!")
        thread.join()
    return answer[0]

def run_quiz():
    name = input("Enter your name: ").strip()
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Fetch all questions and shuffle them
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    random.shuffle(questions)

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q[1]}")
        print(f"A. {q[2]}")
        print(f"B. {q[3]}")
        print(f"C. {q[4]}")
        print(f"D. {q[5]}")

        answer = input_with_timeout("Your answer (A/B/C/D): ", 10)
        if not answer:
            print("❌ Skipped.")
            continue

        if answer.strip().upper() == q[6].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer was {q[6]}")

    total = len(questions)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n✅ Quiz completed, {name}!")
    print(f"🧠 Your final score: {score} out of {total}")
    print(f"📅 Completed on: {now}")

    # Save to scores.txt
    with open("scores.txt", "a") as f:
        f.write(f"{name} - {score}/{total} - {now}\n")

    # Save to leaderboard
    cursor.execute("INSERT INTO leaderboard (name, score, date_taken) VALUES (?, ?, ?)",
                   (name, score, now))
    conn.commit()

    # Show top 5 leaderboard
    print("\n🏆 Leaderboard (Top 5):")
    cursor.execute("SELECT name, score, date_taken FROM leaderboard ORDER BY score DESC, date_taken ASC LIMIT 5")
    for rank, (n, s, d) in enumerate(cursor.fetchall(), 1):
        print(f"{rank}. {n} - {s} points on {d}")

    conn.close()

run_quiz()
