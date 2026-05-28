# Overview

A data analytics project that transforms Ghana Premier League team statistics into actionable football intelligence.

The system evaluates team performance beyond the league table by analyzing:

Team strength and consistency
Home vs away performance balance
Defensive stability in late-game phases
Performance vs expectation gaps
# Objectives
Identify title contenders and relegation risks
Analyze home vs away performance dependency
Detect late-game defensive weaknesses
Determine key drivers of winning
Measure overperformance and underperformance
# Dataset

Team-level aggregated statistics (2025/26 Ghana Premier League season footystats)

Key features include:

Wins, draws, losses
Home and away performance splits
Goal difference metrics
Time-based defensive data (61–90 minutes)
Derived performance indices
# Key Insights
Home advantage is a major factor in GPL performance, with many teams showing strong home dependency.
Late-game (81–90 min) is the most vulnerable defensive period across the league.
Winning is driven more by consistency and goal difference than raw win totals.
Several top teams are underperforming relative to their underlying strength.
The league shows competitive balance with no fully dominant team.
# Streamlit Dashboard

Run the interactive app locally:

streamlit run app/streamlit_app.py
# Tech Stack
Python
Pandas
Plotly
Streamlit
# Future Improvements
Add match-level event data (shots, passes, xG)
Build predictive model for match outcomes
Integrate expected goals (xG) analysis
Add player-level performance metrics
Deploy dashboard to Streamlit Cloud / Render
# Recommendations

Based on the analysis, the following recommendations are made:

⚽ For Clubs
Improve away performance strategies, as away wins are a key differentiator between contenders and mid-table teams.
Focus on late-game game management, especially after the 70th minute where most defensive breakdowns occur.
Prioritize goal difference improvement, not just winning matches, as dominance correlates strongly with success.
Investigate inefficiencies in chance conversion, especially for teams with high strength but low results.
🧠 For Coaches
Introduce structured late-game substitution strategies to reduce fatigue-related errors.
Strengthen defensive organization during transition phases (60–90 minutes).
Develop tactical plans to reduce reliance on home advantage performance.
📊 For Analysts
Use performance gap analysis to identify overperforming and underperforming teams.
Incorporate home/away splits when evaluating team strength.
Prioritize consistency metrics over raw win totals for predictive modeling.
# Conclusion

This project demonstrates that Ghana Premier League team performance is not fully captured by traditional league tables alone.

Key findings show that:

Team success is heavily influenced by home advantage and consistency
Many teams exhibit significant late-game defensive vulnerabilities
There is a clear distinction between performance-driven teams and results-driven teams
Several top teams are currently underperforming relative to their underlying strength

Overall, the league is highly competitive, with no single dominant team, making consistency, game management, and away performance the key factors that separate contenders from mid-table teams.
