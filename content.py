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
        """Generate an intelligent AI response based on user input"""
        input_lower = user_input.lower()
        
        # Enhanced keyword-based responses with more variety
        if any(word in input_lower for word in ['afraid', 'scared', 'fear', 'terrified', 'frightened']):
            responses = [
                "I understand you're feeling afraid. Remember that God has not given you a spirit of fear, but of power, love, and sound mind. He is with you always. What specifically is causing you to feel afraid?",
                "Fear can feel overwhelming, but you're not alone in this. Isaiah 41:10 says 'Do not fear, for I am with you; do not be dismayed, for I am your God.' Can you tell me more about what's frightening you?",
                "When fear grips our hearts, it's natural to feel small. But remember, the God who created the universe lives within you. Let's talk through what's causing this fear together."
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['sad', 'depressed', 'down', 'hopeless', 'despair', 'empty']):
            responses = [
                "I'm sorry you're going through a difficult time. God is close to the brokenhearted and He cares deeply about your pain. Would you like to talk about what's troubling you?",
                "Your sadness is valid, and God sees every tear. Psalm 30:5 reminds us that 'weeping may stay for the night, but rejoicing comes in the morning.' What's been weighing heavy on your heart?",
                "Depression can make everything feel dark, but even in the valley, God walks with you. You matter deeply to Him. What would help you feel supported right now?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['stressed', 'worried', 'anxious', 'overwhelmed', 'panic']):
            responses = [
                "Anxiety can be overwhelming, but remember Philippians 4:6-7 - we can bring all our worries to God in prayer. He wants to give you His peace. What's been weighing on your heart lately?",
                "Stress has a way of making everything feel urgent. But God invites us to 'cast all our anxiety on him because he cares for us' (1 Peter 5:7). What's causing you the most stress right now?",
                "When we're overwhelmed, it's hard to see clearly. Let's take this one step at a time. God promises His peace that surpasses understanding. What's the biggest worry on your mind today?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['thank', 'grateful', 'blessed', 'praise', 'amazing', 'wonderful']):
            responses = [
                "Praise God! It's wonderful to hear your heart of gratitude. Thanksgiving is such a powerful practice that draws us closer to God's heart. What are you most thankful for today?",
                "Your gratitude is beautiful! A thankful heart is like a magnet for God's blessings. It's encouraging to see you recognizing His goodness in your life.",
                "Hallelujah! Your praise lifts my spirit too. God inhabits the praises of His people. What specific blessing has touched your heart recently?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['pray', 'prayer', 'praying']):
            responses = [
                "Prayer is such a gift - direct communication with our Creator! Is there something specific you'd like prayer for, or would you like guidance on how to deepen your prayer life?",
                "It's beautiful that you want to pray. God loves hearing from His children. What's on your heart that you'd like to bring before Him?",
                "Prayer changes everything - including us. Whether you need intercession or want to learn more about prayer, I'm here to support you. What kind of prayer guidance are you seeking?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['bible', 'scripture', 'verse', 'word']):
            responses = [
                "God's Word is living and active! It's wonderful that you're seeking scripture. Is there a particular topic or life situation you'd like biblical guidance on?",
                "The Bible is our lamp and light. What area of your life would you like God's Word to illuminate today?",
                "Scripture has the power to transform hearts and minds. Are you looking for comfort, guidance, or wisdom from God's Word?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['tempted', 'temptation', 'struggle', 'addiction', 'sin']):
            responses = [
                "Temptation is something we all face. Remember, 1 Corinthians 10:13 promises that God will provide a way out. You're not alone in this struggle. What specific area do you need strength in?",
                "I appreciate your honesty about struggling. God's grace is sufficient for every weakness. He's not disappointed in you - He's ready to help. What kind of support would be most helpful right now?",
                "Every believer faces temptation. The fact that you're reaching out shows your heart's desire to honor God. That's already a victory. How can I help you find strength for this battle?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['lonely', 'alone', 'isolated', 'abandoned']):
            responses = [
                "Loneliness can feel so heavy, but you're never truly alone. God promises 'I will never leave you nor forsake you.' He sees you and loves you deeply. What's making you feel isolated?",
                "I hear the loneliness in your words. Even when we feel most alone, God is present with us. He understands what it's like to feel abandoned. You matter to Him and to me.",
                "Feeling alone is one of the hardest human experiences. But remember, even Jesus felt lonely at times. God walks with you through every valley. How can I help you feel more connected?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['angry', 'mad', 'frustrated', 'furious']):
            responses = [
                "Anger is a natural emotion, and even Jesus felt angry at injustice. What's important is what we do with that anger. What's causing you to feel this way?",
                "I can sense your frustration. Sometimes anger is a sign that something important to us has been hurt or threatened. Can you tell me more about what's stirring these feelings?",
                "It's okay to feel angry - God gave us emotions for a reason. Ephesians 4:26 says 'be angry but do not sin.' Let's talk through what's causing this frustration."
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['purpose', 'calling', 'direction', 'lost', 'confused']):
            responses = [
                "Questions about purpose are some of the most important we can ask. Jeremiah 29:11 reminds us that God has plans for us - plans for hope and a future. What area of your life feels most unclear right now?",
                "Feeling lost is actually often the beginning of being found. God uses seasons of uncertainty to draw us closer to Him. What's making you question your direction?",
                "Your desire to understand your calling shows a heart that wants to honor God. That's beautiful. Sometimes our purpose becomes clearer through serving others and staying close to Him. What gifts and passions has God given you?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good evening']):
            responses = [
                "Hello! I'm so glad you're here. How is your heart today? Is there something specific you'd like to talk about or pray about?",
                "Hi there! It's wonderful to connect with you. What's on your mind and heart as we start our conversation?",
                "Greetings! I'm here to listen and support you in your spiritual journey. What would be most helpful for you right now?"
            ]
            return random.choice(responses)
        
        elif any(word in input_lower for word in ['help', 'support', 'advice', 'guidance']):
            responses = [
                "I'm honored that you're seeking help. God often works through community and conversation. What specific area of your life would you like support with?",
                "Asking for help shows wisdom and humility. I'm here to listen and offer biblical encouragement. What challenge are you facing that I can help you navigate?",
                "God designed us to need each other. Your willingness to reach out is beautiful. What kind of guidance would be most valuable to you right now?"
            ]
            return random.choice(responses)
        
        else:
            # More varied general responses
            responses = [
                "I'm here to listen and support you in your spiritual journey. What's on your heart today?",
                "Thank you for sharing with me. God sees your heart and He loves you deeply. Tell me more about what you're experiencing.",
                "I'm grateful to be part of your spiritual journey. How can we seek God's guidance together on what you've shared?",
                "Your honesty is refreshing. God honors those who seek Him with sincere hearts. What would be most helpful for you right now?",
                "I hear you, and I want you to know that your thoughts and feelings matter. How can I best support you in this moment?",
                "God is always working, even when we can't see it. What you've shared resonates with me. How can we explore this together?",
                "Thank you for trusting me with your thoughts. Every conversation is an opportunity to grow closer to God. What's the most important thing you'd like to discuss?",
                "I'm listening with both my heart and mind. Sometimes just being heard is the first step toward healing or clarity. What else would you like to share?"
            ]
            return random.choice(responses)
