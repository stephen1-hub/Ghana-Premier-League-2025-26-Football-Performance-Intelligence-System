import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="GPL Football Intelligence System",
    layout="wide"
)

st.title("⚽ Ghana Premier League 2025/26 - Intelligence Dashboard")

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("ghana-ghana-premier-league-teams-2025-to-2026-stats.csv")

# ----------------------------
# DATA CLEANING / FEATURES
# ----------------------------

# 🏆 TRUE TITLE RACE INDEX (wins-driven)
df["title_race_index"] = df["wins"] * 3

# ⚖️ HOME ADVANTAGE
df["home_advantage"] = df["wins_home"] - df["wins_away"]

# ⏱️ LATE GAME VULNERABILITY
late_cols = [
    "goals_conceded_min_61_to_70",
    "goals_conceded_min_71_to_80",
    "goals_conceded_min_81_to_90"
]

df["late_game_conceded"] = df[late_cols].sum(axis=1)

# 📉 LOSS IMPACT (normalized penalty)
df["loss_penalty"] = df["loss_percentage_ovearll"] * 0.1

# 📊 PERFORMANCE SCORE (balanced model)
df["performance_score"] = (
    df["wins"] * 3
    + df["draw_percentage_overall"] * 0.05
    - df["loss_penalty"]
)

# ----------------------------
# SIDEBAR FILTER
# ----------------------------
team = st.sidebar.selectbox("Select Team", df["team_name"])
team_data = df[df["team_name"] == team]

st.subheader(f"📊 Team Analysis: {team}")
st.write(team_data)

# ----------------------------
# 1. TITLE RACE
# ----------------------------
st.subheader("🏆 Title Race Index (Wins-based)")

fig1 = px.bar(
    df.sort_values("title_race_index", ascending=False),
    x="team_name",
    y="title_race_index",
    text="title_race_index",
    title="Title Race Ranking"
)

st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# 2. HOME ADVANTAGE
# ----------------------------
st.subheader("🏠 Home vs Away Balance")

fig2 = px.bar(
    df.sort_values("home_advantage", ascending=False),
    x="team_name",
    y="home_advantage",
    text="home_advantage",
    title="Home Advantage Index"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# 3. LATE GAME VULNERABILITY
# ----------------------------
st.subheader("⏱️ Late Game Defensive Weakness")

fig3 = px.bar(
    df.sort_values("late_game_conceded", ascending=False),
    x="team_name",
    y="late_game_conceded",
    text="late_game_conceded",
    title="Late Game Goals Conceded (61–90 mins)"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------
# 4. PERFORMANCE SCORE (OVERALL QUALITY)
# ----------------------------
st.subheader("📊 Overall Performance Score (Balanced Model)")

fig4 = px.bar(
    df.sort_values("performance_score", ascending=False),
    x="team_name",
    y="performance_score",
    text="performance_score",
    title="Team Performance Strength Index"
)

st.plotly_chart(fig4, use_container_width=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown("Author")
st.markdown("Stephen Yaw Ayamah, Football Data Analyst")
st.markdown("---")
st.markdown("Built using Python, Pandas, Plotly, and Streamlit")
