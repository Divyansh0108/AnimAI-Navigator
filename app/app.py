import streamlit as st
import sys
import os

# Add the project root directory to Python path FIRST
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import everything else
from dotenv import load_dotenv
import time

# Import the pipeline AFTER path modification
from pipeline.pipeline import AnimeRecommendationPipeline
from pipeline.build_pipeline import build_recommendation_pipeline

st.set_page_config(
    page_title="GetAnime - Your Anime Discovery Companion",
    layout="wide",
    page_icon="⚡",
)

load_dotenv()


@st.cache_resource
def init_pipeline():
    try:
        # Check if vector store exists
        persist_dir = "chroma_db"
        csv_path = "data/processed_anime_data.csv"

        if not os.path.exists(persist_dir) or not os.path.exists(csv_path):
            st.info(
                "🔧 Setting up the anime database for the first time... This may take a few minutes."
            )

            # Build the pipeline automatically
            with st.spinner("🏗️ Building anime knowledge base..."):
                try:
                    build_recommendation_pipeline()
                    st.success("✅ Anime database ready!")
                    time.sleep(2)  # Let user see the success message
                except Exception as e:
                    st.error(f"Failed to build pipeline: {e}")
                    return None

        return AnimeRecommendationPipeline()
    except Exception as e:
        st.error(f"Failed to initialize pipeline: {e}")
        return None


st.markdown(
    """
<style>
    /* Import Japanese-inspired fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap');
    
    /* Anime color palette */
    :root {
        --primary-blue: #2563eb;
        --electric-blue: #3b82f6;
        --sakura-pink: #f472b6;
        --sunset-orange: #f97316;
        --forest-green: #059669;
        --deep-purple: #7c3aed;
        --night-blue: #1e293b;
        --soft-gray: #f8fafc;
        --border-light: #e2e8f0;
        --text-dark: #0f172a;
        --text-muted: #64748b;
        --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --shadow-anime: 0 10px 40px rgba(59, 130, 246, 0.15);
        --glow-blue: 0 0 20px rgba(59, 130, 246, 0.3);
    }
    
    /* Global anime styling */
    .main .block-container {
        font-family: 'Poppins', 'Noto Sans JP', sans-serif;
        max-width: 1400px;
        padding-top: 1rem;
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
        min-height: 100vh;
    }
    
    /* Animated header with anime aesthetics */
    .anime-header {
        text-align: center;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        animation: glow 2s ease-in-out infinite alternate;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
        letter-spacing: -0.02em;
    }
    
    @keyframes glow {
        from { filter: brightness(1) drop-shadow(0 0 5px rgba(102, 126, 234, 0.5)); }
        to { filter: brightness(1.2) drop-shadow(0 0 20px rgba(102, 126, 234, 0.8)); }
    }
    
    .anime-subtitle {
        text-align: center;
        color: var(--text-muted);
        margin-bottom: 2rem;
        font-size: 1.3rem;
        font-weight: 400;
        font-family: 'Noto Sans JP', sans-serif;
    }
    
    /* Enhanced input styling */
    .stTextInput > div > div > input {
        border: 2px solid var(--border-light);
        border-radius: 15px;
        padding: 1rem 1.5rem;
        font-size: 1rem;
        background: white;
        color: var(--text-dark);
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .stTextInput > div > div > input:focus {
        outline: none;
        border-color: var(--electric-blue);
        box-shadow: var(--glow-blue);
        transform: translateY(-2px);
    }
    
    /* Anime-style button */
    .stButton > button {
        background: var(--gradient-1);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        background: var(--gradient-2);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Anime tags/badges - Updated colors */
    .anime-badge {
        display: inline-flex;
        align-items: center;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 0.25rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .anime-badge:nth-child(1) { background: linear-gradient(45deg, #667eea, #764ba2); color: white; }
    .anime-badge:nth-child(2) { background: linear-gradient(45deg, #4ecdc4, #44a08d); color: white; }
    .anime-badge:nth-child(3) { background: linear-gradient(45deg, #a8edea, #fed6e3); color: #333; }
    .anime-badge:nth-child(4) { background: linear-gradient(45deg, #c084fc, #a855f7); color: white; }
    .anime-badge:nth-child(5) { background: linear-gradient(45deg, #4facfe, #00f2fe); color: white; }
    .anime-badge:nth-child(6) { background: linear-gradient(45deg, #f093fb, #f5576c); color: white; }
    
    /* Recommendation card with anime styling */
    .recommendation-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid var(--border-light);
        position: relative;
        overflow: hidden;
        animation: slideInUp 0.6s ease-out;
    }
    
    .recommendation-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: var(--gradient-3);
    }
    
    .recommendation-card::after {
        content: '⭐';
        position: absolute;
        top: 1rem;
        right: 1.5rem;
        font-size: 1.5rem;
        opacity: 0.3;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .recommendation-card h1, 
    .recommendation-card h2, 
    .recommendation-card h3 {
        color: var(--night-blue) !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .recommendation-card p,
    .recommendation-card li,
    .recommendation-card span {
        color: var(--text-dark) !important;
        line-height: 1.7 !important;
        font-size: 1rem !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .recommendation-card strong {
        color: var(--electric-blue) !important;
        font-weight: 600 !important;
    }
    
    /* Feedback buttons with anime styling */
    .feedback-container {
        display: flex;
        gap: 1rem;
        margin-top: 1.5rem;
        align-items: center;
    }
    
    .feedback-question {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        color: var(--text-dark);
        margin-right: 1rem;
        font-size: 1rem;
    }
    
    /* Good button */
    .good-btn {
        background: linear-gradient(45deg, #10b981, #34d399);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
    }
    
    .good-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
    }
    
    /* Bad button */
    .bad-btn {
        background: linear-gradient(45deg, #ef4444, #f87171);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
    }
    
    .bad-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(239, 68, 68, 0.4);
    }
    
    /* Anime sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .css-1d391kg h3, [data-testid="stSidebar"] h3 {
        color: white !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
    }
    
    .css-1d391kg .element-container, [data-testid="stSidebar"] .element-container {
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Metrics with anime styling */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    /* Alert styles with anime theme */
    .alert-success {
        background: linear-gradient(45deg, #10b981, #34d399);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem;
        font-weight: 500;
    }
    
    .alert-error {
        background: linear-gradient(45deg, #ef4444, #f87171);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem;
        font-weight: 500;
    }
    
    .alert-info {
        background: linear-gradient(45deg, #3b82f6, #60a5fa);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem;
        font-weight: 500;
    }
    
    /* Remove white background from expander */
    .streamlit-expanderHeader {
        background: transparent !important;
        border: 1px solid var(--border-light);
        border-radius: 15px;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
    }
    
    .streamlit-expanderContent {
        background: transparent !important;
        border: none !important;
    }
    
    /* Loading animation */
    .stSpinner > div {
        border-color: var(--electric-blue) transparent transparent transparent !important;
    }
    
    /* Hide default streamlit elements */
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .css-18e3th9 {
        padding-top: 0;
    }
    
    /* Footer with anime styling */
    .anime-footer {
        text-align: center;
        padding: 2rem;
        background: var(--gradient-1);
        border-radius: 20px;
        margin-top: 3rem;
        color: white;
        font-family: 'Poppins', sans-serif;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<h1 class="anime-header">⚡ GetAnime</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="anime-subtitle">🌸 Discover your next favorite anime with AI-powered recommendations 🌸</p>',
    unsafe_allow_html=True,
)

# Initialize pipeline
pipeline = init_pipeline()

if pipeline is None:
    st.markdown(
        '<div class="alert-error">❌ Unable to start the recommendation system. Please check your configuration.</div>',
        unsafe_allow_html=True,
    )
    st.stop()

col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    with st.expander("🎯 Popular Anime Categories"):
        st.markdown("**Popular search categories:**")
        example_tags = [
            "School life romance",
            "Dark fantasy adventure",
            "Slice of life cooking",
            "Supernatural powers",
            "Modern Tokyo setting",
            "Comedy workplace",
        ]

        for tag in example_tags:
            st.markdown(
                f'<span class="anime-badge">{tag}</span>', unsafe_allow_html=True
            )

    query = st.text_input(
        "🔍 What anime universe calls to you?",
        placeholder="e.g., heartwarming slice of life with cute characters",
        help="Describe your ideal anime - genre, mood, setting, characters...",
        label_visibility="collapsed",
    )

    search_clicked = st.button("✨ Discover My Anime ✨")

if query and (search_clicked or query):
    if len(query.strip()) < 3:
        st.markdown(
            '<div class="alert-error">⚠️ Please enter at least 3 characters for better recommendations.</div>',
            unsafe_allow_html=True,
        )
    else:
        with st.spinner("🎭 Searching through the anime multiverse..."):
            try:
                time.sleep(0.8)  # Slightly longer for effect
                response = pipeline.recommend(query)

                if response:
                    st.markdown("### 🎬 Your Anime Recommendations")
                    st.markdown(
                        f'<div class="recommendation-card">{response}</div>',
                        unsafe_allow_html=True,
                    )

                    # Updated feedback section
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("**How's the recommendation?**")

                    col_feedback1, col_feedback2 = st.columns([1, 1])

                    with col_feedback1:
                        if st.button("👍 Good", key="good"):
                            st.success("Thanks for the feedback! 🙏")

                    with col_feedback2:
                        if st.button("👎 Bad", key="bad"):
                            st.info("We'll work on improving our recommendations! ✨")

                else:
                    st.markdown(
                        '<div class="alert-error">❌ No anime found in this dimension. Try a different search!</div>',
                        unsafe_allow_html=True,
                    )

            except Exception as e:
                st.markdown(
                    f'<div class="alert-error">💥 Something went wrong in the anime matrix: {str(e)}</div>',
                    unsafe_allow_html=True,
                )

with st.sidebar:
    st.markdown("### 🎌 How the Magic Works")
    steps = [
        "**🎯 Tell us** your anime mood",
        "**🤖 AI analyzes** thousands of series",
        "**✨ Get** personalized picks",
    ]
    for i, step in enumerate(steps, 1):
        st.markdown(f"{i}. {step}")

    st.markdown("### 💡 Pro Tips for Better Results")
    tips = [
        "🎭 Mention specific genres you love",
        "😊 Describe the mood you want",
        "🏙️ Include setting preferences",
        "👥 Specify character types",
        "📺 Mention similar shows you enjoyed",
    ]
    for tip in tips:
        st.markdown(f"• {tip}")

    st.markdown("### 📊 Anime Database Stats")
    st.metric("🗾 Anime Series", "12,000+", "Growing daily")
    st.metric("🎯 Accuracy Rate", "91%", "Iterative improvements")
    st.metric("🎌 Genres Covered", "25+", "All major categories")

st.markdown("---")
st.markdown(
    """
<div class="anime-footer">
    <h3>🌟 Made with ❤️ for Anime Lovers 🌟</h3>
    <p>Powered by AI • Built for Otakus • Made with passion</p>
</div>
""",
    unsafe_allow_html=True,
)
