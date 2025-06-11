import random
from datetime import datetime

class ContentProvider:
    """Provides spiritual content for different categories"""
    
    def __init__(self):
        self.topics = {
            'devotion': [
                'Dealing with Stress',
                'Overcoming Fear',
                'Depression',
                'Relationships',
                'Healing',
                'Purpose & Calling',
                'Anxiety'
            ],
            'prayer': [
                'Personal Growth',
                'Healing',
                'Family/Friends',
                'Forgiveness',
                'Finances',
                'Work/Career'
            ],
            'meditation': [
                'Peace',
                "God's Presence",
                'Strength',
                'Wisdom',
                'Faith'
            ],
            'accountability': [
                'Pornography',
                'Alcohol',
                'Drugs',
                'Sex',
                'Addiction',
                'Laziness'
            ]
        }
        
        self.verses = {
            'stress': {
                'verse': "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
                'reference': "Philippians 4:6-7"
            },
            'fear': {
                'verse': "Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go.",
                'reference': "Joshua 1:9"
            },
            'depression': {
                'verse': "The LORD is close to the brokenhearted and saves those who are crushed in spirit.",
                'reference': "Psalm 34:18"
            },
            'peace': {
                'verse': "Be still, and know that I am God; I will be exalted among the nations, I will be exalted in the earth.",
                'reference': "Psalm 46:10"
            },
            'strength': {
                'verse': "I can do all this through him who gives me strength.",
                'reference': "Philippians 4:13"
            },
            'healing': {
                'verse': "He heals the brokenhearted and binds up their wounds.",
                'reference': "Psalm 147:3"
            }
        }
    
    def get_topics(self, category):
        """Get topics for a specific category"""
        return self.topics.get(category, [])
    
    def get_devotion_content(self, topic):
        """Get devotion content for a topic"""
        topic_key = topic.lower().split()[0]  # Use first word as key
        verse_data = self.verses.get(topic_key, self.verses['peace'])
        
        prayers = {
            'stress': "Lord, I bring my worries and anxieties to You. Help me to trust in Your perfect plan and find peace in Your presence. Amen.",
            'fear': "Heavenly Father, replace my fear with faith. Help me to remember that You are always with me and that Your love casts out all fear. Amen.",
            'depression': "God, You are close to the brokenhearted. Lift my spirit and remind me of Your unfailing love and hope. Amen."
        }
        
        declarations = {
            'stress': "God is my refuge and strength, an ever-present help in trouble.",
            'fear': "I will not fear, for God is with me wherever I go.",
            'depression': "The joy of the Lord is my strength, and His love surrounds me."
        }
        
        return {
            'verse': verse_data['verse'],
            'reference': verse_data['reference'],
            'prayer': prayers.get(topic_key, "Lord, guide me in Your truth and help me grow closer to You. Amen."),
            'declaration': declarations.get(topic_key, "I am fearfully and wonderfully made by God."),
            'video_url': None  # Would be populated from API
        }
    
    def get_prayer_content(self, topic):
        """Get ACTS prayer content for a topic"""
        return {
            'adoration': f"Father, I praise You for Your faithfulness and love. You are mighty and worthy of all honor regarding {topic.lower()}.",
            'confession': f"Lord, I confess my struggles with {topic.lower()}. Forgive me where I have fallen short of Your glory.",
            'thanksgiving': f"Thank You, God, for Your grace and mercy in helping me with {topic.lower()}. I am grateful for Your constant presence.",
            'supplication': f"Please help me, Lord, to grow in {topic.lower()}. Give me wisdom, strength, and Your guidance each day.",
            'prompt': f"Today, pray specifically for someone who might be struggling with {topic.lower()} like you are."
        }
    
    def get_meditation_content(self, topic):
        """Get meditation content for a topic"""
        topic_key = topic.lower().split()[0]
        verse_data = self.verses.get(topic_key, self.verses['peace'])
        
        return {
            'verse': verse_data['verse'],
            'reference': verse_data['reference'],
            'reflection_prompts': [
                "What does this verse reveal about God's character?",
                "How can I apply this truth to my life today?",
                "What is God speaking to my heart through this passage?"
            ]
        }
    
    def get_accountability_content(self, topic):
        """Get accountability content for a topic"""
        scriptures = {
            'pornography': {
                'verse': "I made a covenant with my eyes not to look lustfully at a young woman.",
                'reference': "Job 31:1"
            },
            'alcohol': {
                'verse': "Do not get drunk on wine, which leads to debauchery. Instead, be filled with the Spirit.",
                'reference': "Ephesians 5:18"
            },
            'addiction': {
                'verse': "No temptation has overtaken you except what is common to mankind. And God is faithful; he will not let you be tempted beyond what you can bear.",
                'reference': "1 Corinthians 10:13"
            }
        }
        
        topic_key = topic.lower().split()[0]
        scripture_data = scriptures.get(topic_key, {
            'verse': "I can do all this through him who gives me strength.",
            'reference': "Philippians 4:13"
        })
        
        return {
            'scripture': scripture_data['verse'],
            'reference': scripture_data['reference'],
            'truth_declaration': f"I am not a slave to {topic.lower()}. I am free in Christ Jesus.",
            'alternative_actions': [
                "Take a walk outside",
                "Call a trusted friend",
                "Read a Psalm",
                "Listen to worship music",
                "Practice deep breathing",
                "Write in a journal"
            ]
        }
    
    def get_emergency_content(self):
        """Get emergency support content"""
        return {
            'scripture': "When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you.",
            'reference': "Isaiah 43:2",
            'encouragement': "God sees your struggle and He is with you right now. This moment will pass, and His love for you will never fail.",
            'actions': [
                "Take 10 deep breaths",
                "Call someone you trust",
                "Remove yourself from the tempting situation",
                "Read Psalm 23 aloud",
                "Remember: This feeling is temporary",
                "Focus on one thing you're grateful for"
            ]
        }
    
    def get_ai_response(self, user_input):
        """Generate a simulated AI response"""
        input_lower = user_input.lower()
        
        # Simple keyword-based responses
        if any(word in input_lower for word in ['afraid', 'scared', 'fear']):
            return "I understand you're feeling afraid. Remember that God has not given you a spirit of fear, but of power, love, and sound mind. He is with you always. What specifically is causing you to feel afraid?"
        
        elif any(word in input_lower for word in ['sad', 'depressed', 'down']):
            return "I'm sorry you're going through a difficult time. God is close to the brokenhearted and He cares deeply about your pain. Would you like to talk about what's troubling you, or would you prefer some encouraging scripture?"
        
        elif any(word in input_lower for word in ['stressed', 'worried', 'anxious']):
            return "Anxiety can be overwhelming, but remember Philippians 4:6-7 - we can bring all our worries to God in prayer. He wants to give you His peace. What's been weighing on your heart lately?"
        
        elif any(word in input_lower for word in ['thank', 'grateful', 'blessed']):
            return "Praise God! It's wonderful to hear your heart of gratitude. Thanksgiving is such a powerful practice that draws us closer to God's heart. What are you most thankful for today?"
        
        elif any(word in input_lower for word in ['pray', 'prayer']):
            return "Prayer is such a gift - direct communication with our Creator! Is there something specific you'd like prayer for, or would you like guidance on how to deepen your prayer life?"
        
        elif any(word in input_lower for word in ['bible', 'scripture', 'verse']):
            return "God's Word is living and active! It's wonderful that you're seeking scripture. Is there a particular topic or life situation you'd like biblical guidance on?"
        
        else:
            responses = [
                "I'm here to listen and support you in your spiritual journey. How can I help you grow closer to God today?",
                "Thank you for sharing with me. God sees your heart and He loves you deeply. What's on your mind?",
                "I'm grateful to be part of your spiritual journey. How can we seek God's guidance together?",
                "Your honesty is refreshing. God honors those who seek Him with sincere hearts. Tell me more about what you're experiencing."
            ]
            return random.choice(responses)
