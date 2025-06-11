# Spirit AI - Technical Documentation

## Tech Stack Used

### Frontend Framework
- **Streamlit** - Python web framework for creating interactive web applications
- **HTML/CSS** - Built-in Streamlit components with custom styling via `.streamlit/config.toml`

### Backend & Core Logic
- **Python 3.11** - Main programming language
- **JSON** - Session state management and backup data storage
- **Object-Oriented Programming** - Modular architecture with separate classes

### Database & Data Persistence
- **PostgreSQL** - Primary database for persistent storage
- **SQLAlchemy** - ORM (Object-Relational Mapping) for database operations
- **psycopg2-binary** - PostgreSQL adapter for Python

### Data Models
- Users table (id, username, email, created_at)
- Goals table (id, user_id, category, topic, program_length, start_date, is_active)
- Progress table (id, user_id, category, topic, completed, completion_date, notes)
- Chat Messages table (id, user_id, sender, message_text, timestamp)

### External APIs & Services
- **Socialverse API** - Video content fetching (with fallback to YouTube)
- **YouTube** - Embedded spiritual video content
- **Requests** - HTTP client for API calls

### Core Features Architecture
- **Content Management** - `content.py` with spiritual content database
- **Data Management** - `data.py` for JSON file operations
- **Database Operations** - `database.py` with SQLAlchemy models
- **Session Management** - Streamlit session state for user experience

### Development Tools
- **uv** - Python package manager
- **Replit** - Development and hosting environment
- **Git** - Version control

### Deployment
- **Replit Workflows** - Automated deployment and server management
- **Port 5000** - Web server configuration

## Chatbot Keywords & Responses

### Emotional Keywords
- **Fear/Anxiety:** "afraid", "scared", "fear", "terrified", "frightened", "anxious", "worried", "stressed", "overwhelmed", "panic"
- **Sadness/Depression:** "sad", "depressed", "down", "hopeless", "despair", "empty"
- **Gratitude:** "thank", "grateful", "blessed", "praise", "amazing", "wonderful"
- **Anger:** "angry", "mad", "frustrated", "furious"
- **Loneliness:** "lonely", "alone", "isolated", "abandoned"

### Spiritual Keywords
- **Prayer:** "pray", "prayer", "praying"
- **Scripture:** "bible", "scripture", "verse", "word"
- **Struggle:** "tempted", "temptation", "struggle", "addiction", "sin"
- **Purpose:** "purpose", "calling", "direction", "lost", "confused"

### General Keywords
- **Greetings:** "hello", "hi", "hey", "good morning", "good evening"
- **Help:** "help", "support", "advice", "guidance"

### Example Conversations
- Type "I'm feeling anxious" → Get anxiety-specific scripture and guidance
- Type "I need prayer" → Receive prayer support and questions
- Type "I'm struggling with temptation" → Get accountability resources
- Type "I feel lost" → Receive purpose and calling guidance
- Type "Thank you God" → Get gratitude and praise responses

## File Structure
```
├── app.py              # Main Streamlit application
├── content.py          # Spiritual content provider
├── data.py             # JSON data management
├── database.py         # PostgreSQL database models
├── .streamlit/
│   └── config.toml     # Streamlit configuration
├── pyproject.toml      # Python dependencies
└── user_data.json      # Backup user data storage
```

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE` - Database credentials
- `FLIC_TOKEN` - Socialverse API token (optional)