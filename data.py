import json
import os
from datetime import datetime

class DataManager:
    """Manages user data persistence using JSON files"""
    
    def __init__(self, data_file='user_data.json'):
        self.data_file = data_file
    
    def load_user_data(self):
        """Load user data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading user data: {e}")
            return {}
    
    def save_user_data(self, data):
        """Save user data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False
    
    def get_progress_summary(self, user_data):
        """Get a summary of user progress"""
        if 'progress' not in user_data:
            return {}
        
        summary = {}
        for date, activities in user_data['progress'].items():
            summary[date] = len(activities)
        
        return summary
    
    def get_current_goals(self, user_data):
        """Get current active goals"""
        if 'goals' not in user_data:
            return []
        
        current_goals = []
        today = datetime.now().date()
        
        for goal in user_data['goals']:
            start_date = datetime.fromisoformat(goal['start_date']).date()
            days_elapsed = (today - start_date).days
            
            if days_elapsed < goal['program_length']:
                current_goals.append({
                    **goal,
                    'days_remaining': goal['program_length'] - days_elapsed,
                    'progress_percentage': (days_elapsed / goal['program_length']) * 100
                })
        
        return current_goals
