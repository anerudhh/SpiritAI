# Spirit AI

Spirit AI is a spiritual AI companion web application designed to help users with daily spiritual growth through devotions, prayers, meditations, accountability resources, and AI-driven support. Built with Python and Streamlit, it offers a clean, interactive, and modern user experience.

## Features

- **Devotions, Prayers, Meditations, Accountability:** Get daily spiritual content and tools tailored to your needs.
- **Progress Tracking:** Track your goals and spiritual growth over time, both in a PostgreSQL database and as a JSON backup.
- **Chatbot Support:** Receive AI-driven spiritual guidance, encouragement, and scripture based on your input and emotional state.
- **Video Content:** Watch spiritual videos from Socialverse API or YouTube.
- **User Dashboard:** Visualize your progress and manage your spiritual journey.
- **Modern UI/UX:** Clean, professional interface with custom styling.

## Tech Stack

- **Frontend:** Streamlit (Python web framework)
- **Backend:** Python 3.11, Object-Oriented Programming
- **Database:** PostgreSQL (via SQLAlchemy ORM and psycopg2-binary)
- **Data Management:** JSON for session state and backup
- **External APIs:** Socialverse API, YouTube, Requests

## File Structure

```
├── app.py              # Main Streamlit application
├── content.py          # Spiritual content provider
├── data.py             # JSON data management
├── database.py         # PostgreSQL database models
├── requirements.txt    # Python dependencies
├── user_data.json      # Backup user data storage
├── TECH_STACK.md       # Technical documentation
└── .streamlit/
    └── config.toml     # Streamlit configuration
```

## Setup & Installation

1. **Clone the repository**
2. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Set up PostgreSQL database** and configure environment variables:
   - `DATABASE_URL` (or `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`)
   - `FLIC_TOKEN` (optional, for Socialverse API)
5. **Run the app:**
   ```powershell
   streamlit run app.py
   ```
6. **Open the app** in your browser at the URL provided by Streamlit (usually http://localhost:8501).

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE` - Database credentials
- `FLIC_TOKEN` - Socialverse API token (optional)

## Development & Deployment
- Use `uv` for package management (optional)
- Deploy on Replit or any platform supporting Python and PostgreSQL
- Port 5000 is recommended for deployment

## License
This project is for educational and spiritual growth purposes. Please see LICENSE file for details if provided.

---

For more details, see the [TECH_STACK.md](TECH_STACK.md) file.
