import sqlite3
import time

# creates database for tasks
conn = sqlite3.connect('task_tracker.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                   id INTEGER PRIMARY KEY,
                   name TEXT
               )''')

# outline for a worker in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY,
                   task_name TEXT,
                   worker_id INTEGER,
                   start_time TIMESTAMP,
                   end_time TIMESTAMP,
                   FOREIGN KEY (worker_id) REFERENCES workers (id)
               )''')

# creates said worker
def create_worker(worker_name):
    cursor.execute('INSERT INTO workers (name) VALUES (?)', (worker_name,))
    conn.commit()


def start_task(worker_id, task_name):
   start_time = time.strftime('%Y-%m-%d %H:%M:%S')
   cursor.execute('INSERT INTO tasks (task_name, worker_id, start_time) VALUES (?, ?, ?)', (task_name, worker_id, start_time))
   conn.commit()

def end_task(task_id):
   end_time = time.strftime('%Y-%m-%d %H:%M:%S')
   cursor.execute('UPDATE tasks SET end_time = ? WHERE id = ? AND end_time IS NULL', (end_time, task_id))
   conn.commit()

# need to get input in order to start and end the task for delta T as shown in pictures
    # start task input

    # end task input


# closes the database connection when done
conn.close()
