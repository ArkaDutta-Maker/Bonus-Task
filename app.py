import pandas as pd
df1 = pd.read_csv('anon_data1.csv')
df2 = pd.read_csv('anon_data2.csv') 

df = pd.DataFrame()

df['Participant Name'] = df2["Candidate's Name"]
df['Team Name'] = df2["Team Name"]
df['Participant Type'] = df2["Candidate Type"]
df['Participant Phone Number'] = df2["Candidate's Mobile"]
df["Participant Email"] = df2["Candidate's Email"]

df_new = pd.DataFrame(columns = df.columns)

TeamName = []
ParticipantType =[]
ParticipantPhoneNumber=[]
ParticipantEmail		=[]
ParticipantName=[]
for cnt, i in enumerate(df1["Team Name"]):
    if i not in df["Team Name"].values:
        row = df1.iloc[cnt]
        TeamName.append(row["Team Name"])
        ParticipantType.append("team leader")
        ParticipantPhoneNumber.append(row["Leader Phone"])
        ParticipantEmail.append(row["Leader Email"])
        ParticipantName.append(row["Leader Name"])

df_new["Team Name"] = TeamName
df_new["Participant Type"] = ParticipantType
df_new["Participant Phone Number"] = ParticipantPhoneNumber
df_new["Participant Email"] = ParticipantEmail
df_new["Participant Name"] = ParticipantName

df = pd.concat([df, df_new]).drop_duplicates(subset="Participant Email", keep="first")
df.to_csv('final_data.csv', index=False)