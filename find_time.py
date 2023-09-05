import times
import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('task_tracker.db')
cursor = conn.cursor()

# total time for one task (beta approach)
def calculate_total_time(worker_name):
    cursor.execute('''SELECT tasks.start_time, tasks.end_time
                      FROM tasks
                      INNER JOIN workers ON tasks.worker_id = workers.id
                      WHERE workers.name = ?''', (worker_name,))
    
    total_time_elapsed = timedelta(seconds = 0)  # initializes total time elapsed as a timedelta object to track seconds

    # extracts time elapsed from database
    for row in cursor.fetchall():
        start_time_str, end_time_str = row
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        task_duration = end_time - start_time
        total_time_elapsed += task_duration

    # calculates the time elapsed in seconds (there's a better way, I just don't know right now)
    total_seconds = total_time_elapsed.total_seconds()
    
    return total_seconds

