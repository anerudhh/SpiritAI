import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///dscpl.db')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    goals = relationship("Goal", back_populates="user")
    progress = relationship("Progress", back_populates="user")
    chat_messages = relationship("ChatMessage", back_populates="user")

class Goal(Base):
    __tablename__ = "goals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String(50), nullable=False)
    topic = Column(String(100), nullable=False)
    program_length = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="goals")

class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String(50), nullable=False)
    topic = Column(String(100), nullable=False)
    completed = Column(Boolean, default=True)
    completion_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="progress")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sender = Column(String(20), nullable=False)  # 'user' or 'ai'
    message_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="chat_messages")

class DatabaseManager:
    """Manages database operations for the DSCPL app"""
    
    def __init__(self):
        self.session = SessionLocal()
    
    def create_tables(self):
        """Create all database tables"""
        Base.metadata.create_all(bind=engine)
    
    def get_or_create_user(self, username="default_user", email=None):
        """Get existing user or create a new one"""
        user = self.session.query(User).filter(User.username == username).first()
        if not user:
            user = User(username=username, email=email or f"{username}@dscpl.app")
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
        return user
    
    def create_goal(self, user_id, category, topic, program_length, start_date):
        """Create a new goal for a user"""
        goal = Goal(
            user_id=user_id,
            category=category,
            topic=topic,
            program_length=program_length,
            start_date=start_date
        )
        self.session.add(goal)
        self.session.commit()
        return goal
    
    def get_user_goals(self, user_id, active_only=True):
        """Get all goals for a user"""
        query = self.session.query(Goal).filter(Goal.user_id == user_id)
        if active_only:
            query = query.filter(Goal.is_active == True)
        return query.all()
    
    def save_progress(self, user_id, category, topic, completed=True, notes=None):
        """Save user progress for a completed activity"""
        progress = Progress(
            user_id=user_id,
            category=category,
            topic=topic,
            completed=completed,
            notes=notes
        )
        self.session.add(progress)
        self.session.commit()
        return progress
    
    def get_user_progress(self, user_id, days=30):
        """Get user progress for the last N days"""
        from datetime import timedelta
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        return self.session.query(Progress).filter(
            Progress.user_id == user_id,
            Progress.completion_date >= cutoff_date
        ).order_by(Progress.completion_date.desc()).all()
    
    def save_chat_message(self, user_id, sender, message_text):
        """Save a chat message"""
        chat_message = ChatMessage(
            user_id=user_id,
            sender=sender,
            message_text=message_text
        )
        self.session.add(chat_message)
        self.session.commit()
        return chat_message
    
    def get_chat_history(self, user_id, limit=50):
        """Get chat history for a user"""
        return self.session.query(ChatMessage).filter(
            ChatMessage.user_id == user_id
        ).order_by(ChatMessage.timestamp.asc()).limit(limit).all()
    
    def get_user_stats(self, user_id):
        """Get comprehensive user statistics"""
        total_activities = self.session.query(Progress).filter(Progress.user_id == user_id).count()
        total_goals = self.session.query(Goal).filter(Goal.user_id == user_id).count()
        active_goals = self.session.query(Goal).filter(
            Goal.user_id == user_id, 
            Goal.is_active == True
        ).count()
        
        # Get progress by category
        from sqlalchemy import func
        category_stats = self.session.query(
            Progress.category,
            func.count(Progress.id).label('count')
        ).filter(Progress.user_id == user_id).group_by(Progress.category).all()
        
        return {
            'total_activities': total_activities,
            'total_goals': total_goals,
            'active_goals': active_goals,
            'category_breakdown': {category: count for category, count in category_stats}
        }
    
    def close(self):
        """Close database session"""
        self.session.close()

# Initialize database manager
def get_db_manager():
    """Get a database manager instance"""
    return DatabaseManager()