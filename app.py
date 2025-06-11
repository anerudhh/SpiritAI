import streamlit as st
import requests
import json
import datetime
from datetime import datetime, timedelta
import os
import random
from data import DataManager
from content import ContentProvider

# Initialize data manager and content provider
data_manager = DataManager()
content_provider = ContentProvider()

# Page configuration
st.set_page_config(
    page_title="DSCPL - Spiritual AI Companion",
    page_icon="🙏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome'
if 'user_data' not in st.session_state:
    st.session_state.user_data = data_manager.load_user_data()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def navigate_to(page):
    """Navigate to a specific page"""
    st.session_state.current_page = page
    st.rerun()

def save_progress(category, topic, completed=True):
    """Save user progress"""
    today = datetime.now().strftime('%Y-%m-%d')
    if 'progress' not in st.session_state.user_data:
        st.session_state.user_data['progress'] = {}
    if today not in st.session_state.user_data['progress']:
        st.session_state.user_data['progress'][today] = {}
    
    st.session_state.user_data['progress'][today][category] = {
        'topic': topic,
        'completed': completed,
        'timestamp': datetime.now().isoformat()
    }
    data_manager.save_user_data(st.session_state.user_data)

def get_video_content():
    """Fetch video content from external API"""
    try:
        api_token = os.getenv("FLIC_TOKEN", "flic_b1c6b09d98e2d4884f61b9b3131dbb27a6af84788e4a25db067a22008ea9cce5")
        headers = {"Flic-Token": api_token}
        response = requests.get(
            "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Failed to fetch video content: {str(e)}")
        return None

def render_welcome_page():
    """Render the welcome page"""
    st.markdown("# 🙏 DSCPL")
    st.markdown("### Your Spiritual AI Companion")
    st.markdown("---")
    
    st.markdown("## What do you need today?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📖 Daily Devotion", use_container_width=True):
            st.session_state.selected_category = 'devotion'
            navigate_to('topic_selection')
        
        if st.button("🎥 Watch Video Verse", use_container_width=True):
            st.session_state.selected_category = 'video_verse'
            navigate_to('video_verse')
        
        if st.button("📺 Full Video Bible", use_container_width=True):
            st.session_state.selected_category = 'video_bible'
            navigate_to('video_bible')
        
        if st.button("💬 Just Chat", use_container_width=True):
            navigate_to('chat')
    
    with col2:
        if st.button("🙏 Daily Prayer", use_container_width=True):
            st.session_state.selected_category = 'prayer'
            navigate_to('topic_selection')
        
        if st.button("🧘 Daily Meditation", use_container_width=True):
            st.session_state.selected_category = 'meditation'
            navigate_to('topic_selection')
        
        if st.button("🛡️ Daily Accountability", use_container_width=True):
            st.session_state.selected_category = 'accountability'
            navigate_to('topic_selection')
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📊 Dashboard", use_container_width=True):
            navigate_to('dashboard')
    with col2:
        if st.button("🆘 I Need Help Now", use_container_width=True):
            navigate_to('sos')
    with col3:
        if st.button("⚙️ Settings", use_container_width=True):
            navigate_to('settings')

def render_topic_selection():
    """Render topic selection page"""
    category = st.session_state.selected_category
    
    st.markdown(f"# {category.title()} Topics")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    topics = content_provider.get_topics(category)
    
    st.markdown("## Choose a topic:")
    
    selected_topic = st.radio("", topics, key=f"{category}_topic")
    
    st.markdown("### Or enter your own:")
    custom_topic = st.text_input("Something else...", key=f"{category}_custom")
    
    final_topic = custom_topic if custom_topic else selected_topic
    
    if st.button("Continue", use_container_width=True):
        st.session_state.selected_topic = final_topic
        navigate_to('goal_setting')

def render_goal_setting():
    """Render goal setting page"""
    category = st.session_state.selected_category
    topic = st.session_state.selected_topic
    
    st.markdown(f"# Weekly Goal - {category.title()}")
    st.markdown(f"**Topic:** {topic}")
    
    if st.button("← Back"):
        navigate_to('topic_selection')
    
    st.markdown("---")
    
    st.markdown("## 🎯 Your Weekly Goal")
    st.info("By the end of this week, you will feel more connected to God and confident in resisting temptation.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        program_length = st.selectbox("Program Length:", [7, 14, 30], key="program_length")
    
    with col2:
        start_date = st.date_input("Start Date:", datetime.now().date())
    
    st.markdown("### Would you like to begin?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Yes, Let's Start!", use_container_width=True):
            # Save goal to user data
            goal_data = {
                'category': category,
                'topic': topic,
                'program_length': program_length,
                'start_date': start_date.isoformat(),
                'created_at': datetime.now().isoformat()
            }
            
            if 'goals' not in st.session_state.user_data:
                st.session_state.user_data['goals'] = []
            
            st.session_state.user_data['goals'].append(goal_data)
            data_manager.save_user_data(st.session_state.user_data)
            
            navigate_to('content')
    
    with col2:
        if st.button("❌ Not Yet", use_container_width=True):
            navigate_to('welcome')

def render_content_page():
    """Render the main content page based on category"""
    category = st.session_state.selected_category
    topic = st.session_state.selected_topic
    
    st.markdown(f"# {category.title()} - {topic}")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    if category == 'devotion':
        render_devotion_content()
    elif category == 'prayer':
        render_prayer_content()
    elif category == 'meditation':
        render_meditation_content()
    elif category == 'accountability':
        render_accountability_content()
    
    # Mark as completed
    if st.button("✅ Mark as Completed", use_container_width=True):
        save_progress(category, topic)
        st.success("Great job! Your progress has been saved.")
        st.balloons()

def render_devotion_content():
    """Render devotion content"""
    topic = st.session_state.selected_topic
    devotion = content_provider.get_devotion_content(topic)
    
    st.markdown("## 📖 Today's Verse")
    st.markdown(f"*{devotion['verse']}*")
    st.markdown(f"**{devotion['reference']}**")
    
    st.markdown("## 🙏 Prayer")
    st.markdown(devotion['prayer'])
    
    st.markdown("## 💪 Faith Declaration")
    st.info(devotion['declaration'])
    
    st.markdown("## 🎥 Suggested Video")
    if devotion['video_url']:
        st.video(devotion['video_url'])
    else:
        st.warning("Video content not available at the moment.")

def render_prayer_content():
    """Render prayer content using ACTS format"""
    topic = st.session_state.selected_topic
    prayer_content = content_provider.get_prayer_content(topic)
    
    st.markdown("## 🙏 ACTS Prayer Format")
    
    with st.expander("**A** - Adoration (Praise)", expanded=True):
        st.markdown(prayer_content['adoration'])
    
    with st.expander("**C** - Confession", expanded=True):
        st.markdown(prayer_content['confession'])
    
    with st.expander("**T** - Thanksgiving", expanded=True):
        st.markdown(prayer_content['thanksgiving'])
    
    with st.expander("**S** - Supplication (Ask for help)", expanded=True):
        st.markdown(prayer_content['supplication'])
    
    st.markdown("## 💡 Daily Prayer Prompt")
    st.info(prayer_content['prompt'])

def render_meditation_content():
    """Render meditation content"""
    topic = st.session_state.selected_topic
    meditation = content_provider.get_meditation_content(topic)
    
    st.markdown("## 🧘 Focus Verse")
    st.markdown(f"*{meditation['verse']}*")
    st.markdown(f"**{meditation['reference']}**")
    
    st.markdown("## 🤔 Reflection")
    st.markdown("**What does this reveal about God?**")
    st.text_area("Your thoughts:", height=100, key="meditation_reflection")
    
    st.markdown("## 🌬️ Breathing Guide")
    st.info("**Inhale for 4 seconds → Hold for 4 seconds → Exhale for 4 seconds**")
    
    if st.button("Start Guided Breathing"):
        placeholder = st.empty()
        import time
        for i in range(3):  # 3 cycles
            placeholder.markdown("### 🌬️ Inhale... (4s)")
            time.sleep(1)
            placeholder.markdown("### 🫁 Hold... (4s)")
            time.sleep(1)
            placeholder.markdown("### 💨 Exhale... (4s)")
            time.sleep(1)
        placeholder.success("Breathing exercise completed! 🧘‍♀️")

def render_accountability_content():
    """Render accountability content"""
    topic = st.session_state.selected_topic
    accountability = content_provider.get_accountability_content(topic)
    
    st.markdown("## 💪 Scripture of Strength")
    st.markdown(f"*{accountability['scripture']}*")
    st.markdown(f"**{accountability['reference']}**")
    
    st.markdown("## 🗣️ Truth Declaration")
    st.success(accountability['truth_declaration'])
    
    st.markdown("## 📝 Alternative Actions")
    for action in accountability['alternative_actions']:
        st.markdown(f"• {action}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆘 I Need Help Now", use_container_width=True):
            navigate_to('sos')
    with col2:
        if st.button("💬 Chat with Mentor", use_container_width=True):
            navigate_to('chat')

def render_video_verse():
    """Render video verse content"""
    st.markdown("# 🎥 Watch Video Verse")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    # Sample spiritual videos for demonstration
    sample_videos = [
        {
            'title': 'Philippians 4:13 - I Can Do All Things Through Christ',
            'url': 'https://www.youtube.com/watch?v=KO6WlCLFqw4',
            'verse': 'I can do all this through him who gives me strength.',
            'reference': 'Philippians 4:13'
        },
        {
            'title': 'Psalm 23 - The Lord is My Shepherd',
            'url': 'https://www.youtube.com/watch?v=GsNcOzGOm0k',
            'verse': 'The Lord is my shepherd, I lack nothing.',
            'reference': 'Psalm 23:1'
        },
        {
            'title': 'John 3:16 - For God So Loved the World',
            'url': 'https://www.youtube.com/watch?v=Wh1VU-_OF98',
            'verse': 'For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.',
            'reference': 'John 3:16'
        }
    ]
    
    # Try to get video content from API first
    video_data = get_video_content()
    
    if video_data and 'data' in video_data and video_data['data']:
        st.markdown("## Today's Video Verse")
        video_item = video_data['data'][0]  # Get first video
        st.markdown(f"**{video_item.get('title', 'Spiritual Video')}**")
        
        video_url = video_item.get('video_url') or video_item.get('url')
        if video_url:
            st.video(video_url)
        else:
            st.warning("Video URL not available for this content.")
    else:
        # Use sample videos as fallback
        st.markdown("## Today's Video Verse")
        selected_video = random.choice(sample_videos)
        
        st.markdown(f"**{selected_video['title']}**")
        st.markdown(f"*{selected_video['verse']}*")
        st.markdown(f"**{selected_video['reference']}**")
        
        st.video(selected_video['url'])
        
        st.markdown("### More Video Verses")
        for i, video in enumerate(sample_videos):
            if video != selected_video:
                with st.expander(f"{video['title']}"):
                    st.markdown(f"*{video['verse']}*")
                    st.markdown(f"**{video['reference']}**")
                    st.video(video['url'])

def render_video_bible():
    """Render full video bible content"""
    st.markdown("# 📺 Full Video Bible")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    video_data = get_video_content()
    
    if video_data and 'data' in video_data:
        st.markdown("## Available Bible Videos")
        
        for i, video_item in enumerate(video_data['data'][:10]):  # Show first 10 videos
            with st.expander(f"{video_item.get('title', f'Video {i+1}')}"):
                video_url = video_item.get('video_url') or video_item.get('url')
                if video_url:
                    st.video(video_url)
                else:
                    st.warning("Video URL not available for this content.")
    else:
        st.error("Unable to fetch video content. Please try again later.")

def render_chat():
    """Render chat interface"""
    st.markdown("# 💬 Chat with Your Spiritual Companion")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    # Display chat history in containers
    chat_container = st.container()
    
    with chat_container:
        if st.session_state.chat_history:
            for message in st.session_state.chat_history:
                if message['sender'] == 'user':
                    with st.chat_message("user"):
                        st.write(message['text'])
                else:
                    with st.chat_message("assistant"):
                        st.write(message['text'])
        else:
            st.info("Welcome! I'm here to support you on your spiritual journey. How can I help you today?")
    
    # Chat input at bottom
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        st.session_state.chat_history.append({
            'sender': 'user',
            'text': prompt,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate AI response
        ai_response = content_provider.get_ai_response(prompt)
        st.session_state.chat_history.append({
            'sender': 'ai',
            'text': ai_response,
            'timestamp': datetime.now().isoformat()
        })
        
        st.rerun()

def render_dashboard():
    """Render user dashboard"""
    st.markdown("# 📊 Your Spiritual Journey Dashboard")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    user_data = st.session_state.user_data
    
    # Weekly goals
    if 'goals' in user_data and user_data['goals']:
        st.markdown("## 🎯 Current Goals")
        for goal in user_data['goals']:
            with st.expander(f"{goal['category'].title()} - {goal['topic']}"):
                st.markdown(f"**Program Length:** {goal['program_length']} days")
                st.markdown(f"**Started:** {goal['start_date']}")
                
                # Calculate progress
                start_date = datetime.fromisoformat(goal['start_date']).date()
                days_elapsed = (datetime.now().date() - start_date).days
                progress = min(days_elapsed / goal['program_length'] * 100, 100)
                
                st.progress(progress / 100)
                st.markdown(f"Progress: {progress:.1f}%")
    
    # Daily progress
    if 'progress' in user_data and user_data['progress']:
        st.markdown("## 📈 Recent Activity")
        
        # Get last 7 days of progress
        today = datetime.now().date()
        last_week = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
        
        for date in last_week:
            if date in user_data['progress']:
                st.markdown(f"**{date}:**")
                for category, data in user_data['progress'][date].items():
                    st.markdown(f"  ✅ {category.title()}: {data['topic']}")
            else:
                st.markdown(f"**{date}:** No activity")
    else:
        st.info("Start your spiritual journey today! Complete your first devotion, prayer, or meditation to see your progress here.")

def render_sos():
    """Render emergency support page"""
    st.markdown("# 🆘 I Need Help Now")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    st.error("**You are not alone. God is with you.**")
    
    emergency_content = content_provider.get_emergency_content()
    
    st.markdown("## 🙏 Quick Scripture")
    st.markdown(f"*{emergency_content['scripture']}*")
    st.markdown(f"**{emergency_content['reference']}**")
    
    st.markdown("## 💪 Encouragement")
    st.success(emergency_content['encouragement'])
    
    st.markdown("## 🏃‍♂️ Immediate Actions")
    for action in emergency_content['actions']:
        st.markdown(f"• {action}")
    
    if st.button("💬 Chat with Spiritual Companion", use_container_width=True):
        navigate_to('chat')

def render_settings():
    """Render settings page"""
    st.markdown("# ⚙️ Settings")
    
    if st.button("← Back to Home"):
        navigate_to('welcome')
    
    st.markdown("---")
    
    st.markdown("## Program Preferences")
    
    default_program_length = st.selectbox("Default Program Length:", [7, 14, 30], key="default_program")
    
    st.markdown("## Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📤 Export Progress", use_container_width=True):
            data_json = json.dumps(st.session_state.user_data, indent=2)
            st.download_button(
                label="Download Data",
                data=data_json,
                file_name="dscpl_progress.json",
                mime="application/json"
            )
    
    with col2:
        if st.button("🗑️ Clear All Data", use_container_width=True):
            if st.button("⚠️ Confirm Clear All Data"):
                st.session_state.user_data = {}
                data_manager.save_user_data(st.session_state.user_data)
                st.success("All data cleared successfully.")
                st.rerun()

# Main app routing
def main():
    page = st.session_state.current_page
    
    if page == 'welcome':
        render_welcome_page()
    elif page == 'topic_selection':
        render_topic_selection()
    elif page == 'goal_setting':
        render_goal_setting()
    elif page == 'content':
        render_content_page()
    elif page == 'video_verse':
        render_video_verse()
    elif page == 'video_bible':
        render_video_bible()
    elif page == 'chat':
        render_chat()
    elif page == 'dashboard':
        render_dashboard()
    elif page == 'sos':
        render_sos()
    elif page == 'settings':
        render_settings()

if __name__ == "__main__":
    main()
