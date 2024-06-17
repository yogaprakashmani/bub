import pandas as pd
import streamlit as st


df=pd.read_csv("ipl2024.csv")



st.write('<p style="font-size:28px; color:#AD3B3B;font-weight: bold;">Cricket Player Analyser</p>', unsafe_allow_html=True)
st.write('<p style="font-size:28px; color:#AD3B3B;font-weight: bold;">Select the player to compare from list</p>', unsafe_allow_html=True)
col1, col2,col3 =st.columns(3)


with col1:
     st.text( ' ')
     st.text( ' ')
     st.markdown(f"<span style='color: #AD3B3B;font-size: 24px;font-weight: bold;'>Name</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#AD3B3B;font-size: 24px;font-weight: bold;'>Run</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#AD3B3B;font-size: 24px;font-weight: bold;'>Match played</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#AD3B3B;font-size: 24px;font-weight: bold;'>Batting Average</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#AD3B3B;font-size: 24px;font-weight: bold;'>Wickets</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#AD3B3B;font-size: 24px;font-weight: bold;'>Bowl Average</span>", unsafe_allow_html=True)
     


player1=col2.selectbox("Select Player1",df["Name"])

count1 = df.loc[(df["Name"] == player1) , 'Run'].iloc[0]
count2 = df.loc[(df["Name"] == player1) , 'Match Played'].iloc[0]
count3 = df.loc[(df["Name"] == player1) , 'Bat Avg'].iloc[0]
count4 = df.loc[(df["Name"] == player1) , 'Wickets'].iloc[0]
count5 = df.loc[(df["Name"] == player1) , 'Bowl Avg'].iloc[0]

with col2:
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count1}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count2}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count3}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count4}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count5}</span>", unsafe_allow_html=True)




player2=col3.selectbox("Select Player2",df["Name"])


count1 = df.loc[(df["Name"] == player2) , 'Run'].iloc[0]
count2 = df.loc[(df["Name"] == player2) , 'Match Played'].iloc[0]
count3 = df.loc[(df["Name"] == player2) , 'Bat Avg'].iloc[0]
count4 = df.loc[(df["Name"] == player2) , 'Wickets'].iloc[0]
count5 = df.loc[(df["Name"] == player2) , 'Bowl Avg'].iloc[0]



with col3:
    
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count1}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color:#181717;font-size: 24px;font-weight: bold;'>{count2}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count3}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count4}</span>", unsafe_allow_html=True)
     st.markdown(f"<span style='color: #181717;font-size: 24px;font-weight: bold;'>{count5}</span>", unsafe_allow_html=True)




hide_st_style = """
          <style>
          footer {visibility: hidden;}
          header {visibility: hidden;}
          </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)







