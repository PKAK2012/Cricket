#streamlit run cricket/dem.py --theme.base "light" --theme.backgroundColor "#FAF3DD" --theme.textColor "#000000" --theme.secondaryBackgroundColor "#FFFACD"



import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
con = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="251B6WaGrvhDB6j.root",
    port=4000,
    password="X6BdcD5RewwbUdVn",
    database="Cricket",
    ssl_ca=r"C:\Users\engga\Downloads\isrgrootx1 (1).pem"
)
#print("Connected Successfully!")
cur = con.cursor()

import streamlit as st
st.set_page_config(layout="wide")

import streamlit as st




st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #D2691E; display: inline-block;">🏏 Welcome to Cricket Stats</h1>
        <p style="color: #1E90FF; font-size: 18px; margin-top: -10px;">
            Explore cricket matches, players, and statistics!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

Select_Query = ["Query_1","Query_2","Query_3","Query_4","Query_5","Query_6","Query_7",
"Query_8","Query_9","Query_10","Query_11","Query_12","Query_13","Query_14","Query_15","Query_16",
"Query_17","Query_18","Query_19","Query_20"]

table = ["Home","None"]

tab_name = st.sidebar.selectbox("Select",table, index=table.index("Home"))

if tab_name == "Home":
    st.image("https://i.imgur.com/GMVpAVb.jpeg", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True) 

st.sidebar.header("Select_query")
Qry1 = st.sidebar.checkbox(Select_Query[0])
Qry2 = st.sidebar.checkbox(Select_Query[1])
Qry3 = st.sidebar.checkbox(Select_Query[2])
Qry4 = st.sidebar.checkbox(Select_Query[3])
Qry5 = st.sidebar.checkbox(Select_Query[4])
Qry6 = st.sidebar.checkbox(Select_Query[5])
Qry7 = st.sidebar.checkbox(Select_Query[6])
Qry8 = st.sidebar.checkbox(Select_Query[7])
Qry9 = st.sidebar.checkbox(Select_Query[8])
Qry10 = st.sidebar.checkbox(Select_Query[9])
Qry11= st.sidebar.checkbox(Select_Query[10])
Qry12 = st.sidebar.checkbox(Select_Query[11])
Qry13= st.sidebar.checkbox(Select_Query[12])
Qry14= st.sidebar.checkbox(Select_Query[13])
Qry15= st.sidebar.checkbox(Select_Query[14])
Qry16= st.sidebar.checkbox(Select_Query[15])
Qry17= st.sidebar.checkbox(Select_Query[16])
Qry18= st.sidebar.checkbox(Select_Query[17])
Qry19= st.sidebar.checkbox(Select_Query[18])
Qry20= st.sidebar.checkbox(Select_Query[19])

if Qry1:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 1. List of Top 10 Teams That Played the Most ODIs
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True) 
    cur.execute("""
        SELECT team1 AS Team, COUNT(*) AS Matches
        FROM ODI
        GROUP BY team1
        ORDER BY Matches DESC
        LIMIT 10
    """)
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res, columns=columns)
    col1, col2 = st.columns([1, 2])    
    with col1:
        st.dataframe(df)    
    with col2:
        st.bar_chart(df.set_index("Team"))

     
if Qry2:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 2.Find the teams that played in ODI and T20
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)         
    cur.execute("""SELECT all_teams.team, 
       COALESCE(odi.odi_matches, 0) AS odi_match_count, 
       COALESCE(t20.t20_matches, 0) AS t20_match_count,
       (COALESCE(odi.odi_matches, 0) + COALESCE(t20.t20_matches, 0)) AS total_matches
FROM (
    SELECT team1 AS team FROM ODI
    UNION
    SELECT team2 FROM ODI
    UNION
    SELECT team1 FROM T20
    UNION
    SELECT team2 FROM T20
) AS all_teams
LEFT JOIN (
    SELECT team1 AS team, COUNT(*) AS odi_matches
    FROM ODI
    GROUP BY team1
) AS odi ON all_teams.team = odi.team
LEFT JOIN (
    SELECT team1 AS team, COUNT(*) AS t20_matches
    FROM T20
    GROUP BY team1
) AS t20 ON all_teams.team = t20.team
ORDER BY total_matches DESC
LIMIT 10;
""")
    res=cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res,columns=columns)
    st.dataframe(df)
    st.bar_chart(df.set_index("team"))
    
if Qry3:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 3.Get the total number of matches played by each team in ODIs
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)   
    st.markdown("<br>", unsafe_allow_html=True)       
    cur.execute("""SELECT team, COUNT(*) AS total_matches 
FROM (
    SELECT team1 AS team FROM ODI 
    UNION ALL 
    SELECT team2 FROM ODI
) AS all_matches
GROUP BY team
ORDER BY total_matches DESC limit 10""")
    res=cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([1, 2])    
    with col1:
        st.dataframe(df)    
    with col2:
        st.line_chart(df.set_index("team"))
    
if Qry4:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 4.Find teams with the highest win percentage in ODIs
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute(""" SELECT winner, 
       COUNT(*) AS total_wins, 
       (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ODI)) AS win_percentage
FROM ODI
GROUP BY winner
ORDER BY win_percentage DESC
LIMIT 5""")
    res=cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res,columns=columns)
    st.dataframe(df)
    st.scatter_chart(df.set_index("winner"))
    
if Qry5:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 5. List top 10 players with most runs in ODIs
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    
    cur.execute("""SELECT batter, SUM(runs_scored) AS total_runs
FROM ODI
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10""")
    res=cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res,columns=columns)
    st.dataframe(df)    
    fig = px.bar(df, x="batter", y="total_runs", color="total_runs", title="Total")
    fig.update_traces(marker_color="brown")
    st.plotly_chart(fig)
    
if Qry6:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 6. Find teams with the highest number of centuries in T20
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT batting_team, COUNT(*) AS total_centuries
FROM T20
WHERE runs_scored >= 100
GROUP BY batting_team
ORDER BY total_centuries DESC
LIMIT 5""")
    res=cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res,columns=columns)
    st.dataframe(df) 
    fig, ax = plt.subplots()
    sns.barplot(x="batting_team", y="total_centuries", data=df, ax=ax,color = "orange")
    st.pyplot(fig)
    
if Qry7:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 7. Find bowlers with the best economy rate
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute(""" 
    SELECT bowler, 
           ROUND(SUM(runs_conceded) / (SUM(balls_bowled) / 6.0), 2) AS economy_rate
    FROM ODI
    GROUP BY bowler
    HAVING SUM(balls_bowled) >= 300
    ORDER BY economy_rate ASC
    LIMIT 10
    """)    
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res, columns=columns)
    st.dataframe(df)
    if not df.empty:
        chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("bowler", sort="-y", title="Bowler"),
        y=alt.Y("economy_rate", title="Economy Rate"),
        color=alt.value("#EE82EE")
        ).properties(
            title="Top 10 Bowlers with Best Economy Rate in ODIs"
        )
    st.altair_chart(chart)

if Qry8:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 8. Compare average team scores in ODI vs. T20
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT 'ODI' AS format, AVG(total_runs) AS avg_score FROM ODI
                    UNION ALL
                SELECT 'T20', AVG(total_runs) FROM T20""")
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res, columns=columns)
    st.dataframe(df)
    fig = px.bar(df, x="format", y="avg_score", color_discrete_sequence=["#6B8E23"],width=100)  
    st.plotly_chart(fig)


if Qry9:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 9. Find players who scored centuries 
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT batter, run_scored AS total_runs
               FROM (
                   SELECT batter, 'ODI' AS format, runs_scored AS run_scored FROM ODI WHERE runs_scored >= 100
                   UNION ALL
                   SELECT batter, 'T20', runs_scored FROM T20 WHERE runs_scored >= 100
               ) AS centuries
               GROUP BY batter
               HAVING COUNT(DISTINCT format) = 2
               ORDER BY total_runs DESC
               LIMIT 5""")
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res, columns=columns)
    st.dataframe(df)
    fig = px.bar(df, x="batter", y="total_runs", title="CENTURIES", color="total_runs")
    st.plotly_chart(fig)
    
if Qry10:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 10. Find teams with the best win/loss ratio in ODI and T20 formats
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT * 
FROM (
    SELECT team, 
           SUM(CASE WHEN format = 'ODI' THEN wins END) / NULLIF(SUM(CASE WHEN format = 'ODI' THEN losses END), 0) AS ODI_ratio,
           SUM(CASE WHEN format = 'T20' THEN wins END) / NULLIF(SUM(CASE WHEN format = 'T20' THEN losses END), 0) AS T20_ratio
    FROM (
        SELECT winner AS team, 'ODI' AS format, COUNT(*) AS wins, 0 AS losses FROM ODI GROUP BY winner
        UNION ALL
        SELECT team1 AS team, 'ODI' AS format, 0 AS wins, COUNT(*) AS losses FROM ODI WHERE winner != team1 GROUP BY team1
        UNION ALL
        SELECT winner AS team, 'T20' AS format, COUNT(*) AS wins, 0 AS losses FROM T20 GROUP BY winner
        UNION ALL
        SELECT team1 AS team, 'T20' AS format, 0 AS wins, COUNT(*) AS losses FROM T20 WHERE winner != team1 GROUP BY team1
    ) AS all_matches
    GROUP BY team
) AS aggregated_results
WHERE team IS NOT NULL 
  AND ODI_ratio IS NOT NULL AND ODI_ratio > 0 
  AND T20_ratio IS NOT NULL AND T20_ratio > 0 
ORDER BY (ODI_ratio + T20_ratio) DESC
LIMIT 10;
""")
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df = pd.DataFrame(res, columns=columns)
    col1, col2 = st.columns([2, 3])  
    with col1:
        st.dataframe(df)  
    with col2:     
        fig_odi = px.pie(df, names="team", values="ODI_ratio", title="ODI Ratio Distribution")
        fig_t20 = px.pie(df, names="team", values="T20_ratio", title="T20 Ratio Distribution")
        st.plotly_chart(fig_odi)
        st.plotly_chart(fig_t20)
    


if Qry11:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 11. Find teams with the highest average strike rate in ODIs
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3>Find teams with the highest average strike rate in ODIs</h3>", unsafe_allow_html=True)
    cur.execute("""SELECT batting_team, round(AVG(runs_scored * 100.0 / balls_faced),2) AS avg_strike_rate
FROM ODI
GROUP BY batting_team
ORDER BY avg_strike_rate DESC
LIMIT 10""")
    res = cur.fetchall()
    columns = [j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3])  
    with col1:
        st.dataframe(df)  
    with col2:     
        st.line_chart(df,x="batting_team",y="avg_strike_rate")
    
if Qry12:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 12. Find the Toss Winning Percentage of Each Team in IPL
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT toss_win, 
       COUNT(*) AS tosses_won, 
       ROUND((COUNT(*) * 100.0) / (SELECT COUNT(*) FROM IPL)) AS toss_win_percentage 
FROM IPL 
GROUP BY toss_win 
ORDER BY toss_win_percentage DESC limit 10""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    st.dataframe(df)
    fig = px.bar(df, x="toss_win", y="tosses_won",title="toss_win_percentage", color="toss_win_percentage")
    st.plotly_chart(fig)
    
if Qry13:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 13. Find the player name and number of times they got out for a duck
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3> Find the player name and number of times they got out for a duck</h3>", unsafe_allow_html=True)
    cur.execute("""SELECT batter, COUNT(*) AS duck_outs
FROM ODI
WHERE runs_scored = 0 
GROUP BY batter
ORDER BY duck_outs DESC limit 5""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3])  
    with col1:
        st.dataframe(df)  
    with col2:     
        st.line_chart(df,x="batter",y="duck_outs")
 
if Qry14:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 14. Most Common Venues for Matches for IPL
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT venue, COUNT(*) AS matches_played 
FROM IPL 
GROUP BY venue 
ORDER BY matches_played DESC 
LIMIT 10""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3])  
    with col1:
        st.dataframe(df)  
    with col2:     
        fig = px.sunburst(df,path=["venue"],values="matches_played", title="Matches Played at Different Venues")
        fig.update_layout(title_x=0.3)
        st.plotly_chart(fig)

if Qry15:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 15. Player with the Most 'Player of the Match' Awards(min 100 wickets)
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""SELECT POM, COUNT(*) AS awards 
FROM IPL 
GROUP BY POM 
ORDER BY awards DESC 
LIMIT 10""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:  
        fig = px.bar(df, x="awards", y="POM", orientation="h", 
        title="Most Player of the Match Awards in IPL",
        labels={"awards": "Number of Awards", "POM": "Player"},
        color="awards", color_continuous_scale="pinkyl") 
        
    fig.update_layout(
    title_x=0.3,  
    width=400,   
    height=400,   
    margin=dict(l=100, r=50, t=50, b=50) )
    fig.update_layout(title_x=0.3)
    st.plotly_chart(fig)
    
if Qry16:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 16. Find the highest average runs per match in each year(min 100 wickets)
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
 
    cur.execute("""SELECT  year, 
       ROUND(AVG(total_runs)) AS avg_runs_per_match
FROM ODI
GROUP BY year
ORDER BY avg_runs_per_match DESC
LIMIT 10""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:
        fig = px.pie(df, names="year", values="avg_runs_per_match", title="AVERAGE_RUNS",hole=0.3,labels = "avg_runs_per_match")
        fig.update_layout(title_x=0.3)
        st.plotly_chart(fig)
        

if Qry17:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 17. Find the highest successful run chase in ODI history
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""WITH YearlyHighestChase AS (
    SELECT year, team2 AS chasing_team, total_runs AS target_score,
           ROW_NUMBER() OVER (PARTITION BY year ORDER BY total_runs DESC) AS chase_rank
    FROM ODI
    WHERE winner = team2  -- Ensures only successful chases
)
SELECT year, chasing_team, target_score
FROM YearlyHighestChase
WHERE chase_rank = 1
ORDER BY target_score DESC limit 10""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:
    #st.dataframe(df)
        fig = px.bar(df, x="year", y="target_score", color="chasing_team",  
        title="Highest Successfull Run Chase", 
        labels={"value": "target_score", "variable": "chasing_team"},
        barmode="stack", color_discrete_sequence=["#9370DB", "#708090", "#FFDB58"])
        fig.update_layout(
        title_x=0.3,  
        width=1200,   
        height=500,   
        margin=dict(l=100, r=50, t=50, b=50) )
        fig.update_layout(title_x=0.3)
        st.plotly_chart(fig)
    
if Qry18:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 18. Find the Teams with the Most Wins in Each Format
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""(SELECT 'ODI' AS format, winner, COUNT(*) AS wins
 FROM ODI
 GROUP BY winner
 ORDER BY wins DESC
 LIMIT 1)

UNION ALL

(SELECT 'T20' AS format, winner, COUNT(*) AS wins
 FROM T20
 GROUP BY winner
 ORDER BY wins DESC
 LIMIT 1)
""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:
        fig = px.bar(df, x="winner", y="wins", 
        text="wins", 
        color_discrete_sequence=["#9370DB"]) 
        st.plotly_chart(fig)

    
if Qry19:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 19. Best Batting Strike Rate in ODI & T20 (Min 500 Runs)
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    cur.execute("""select batter,strike_rate from ((SELECT 'ODI' AS format, batter, 
        SUM(runs_scored) AS total_runs, 
        SUM(balls_faced) AS total_balls,
        ROUND((SUM(runs_scored) * 100.0) / SUM(balls_faced), 2) AS strike_rate
 FROM ODI
 GROUP BY batter
 HAVING total_runs > 500
 ORDER BY strike_rate DESC
 LIMIT 5)

UNION ALL

(SELECT 'T20' AS format, batter, 
        SUM(runs_scored) AS total_runs, 
        SUM(balls_faced) AS total_balls,
        ROUND((SUM(runs_scored) * 100.0) / SUM(balls_faced), 2) AS strike_rate
 FROM T20
 GROUP BY batter
 HAVING total_runs > 500
 ORDER BY strike_rate DESC
 LIMIT 5));
""")
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:
        st.markdown("<h3><center>Batting Strike Rate</center></h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True) 
        st.line_chart(df,x="batter",y="strike_rate")

if Qry20:
    st.markdown(
    """<h5 style="color:white; background-color:#008080; padding:10px; border-radius:5px; text-align:left;">
    ✅ 20. Find the most ODI centuries scored in each year
    </h5>""",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3> Find the most ODI centuries scored in each year</h3>", unsafe_allow_html=True)
    cur.execute("""SELECT year, COUNT(*) AS total_centuries
    FROM ODI
    WHERE runs_scored >= 100
    GROUP BY year
    ORDER BY year desc limit 10
    """)
    res=cur.fetchall()
    columns=[j[0] for j in cur.description]
    df=pd.DataFrame(res,columns=columns)
    col1, col2 = st.columns([2, 3]) 
    with col1:
        st.dataframe(df) 
    with col2:    
        fig = px.bar(df, x="year", y="total_centuries", 
        text="total_centuries", 
        color_discrete_sequence=["#A0522D"]) 
        st.plotly_chart(fig)