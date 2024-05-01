import pandas as pd
import numpy as np

df = pd.read_csv("bank_marketing.csv")

client_df = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]

# Replace dots in job and education columns with underscores
client_df["job"] = client_df["job"].str.replace(".", "_")
client_df["education"] = client_df["education"].str.replace(".", "_")
client_df["education"] = client_df["education"].replace("unknown", np.NaN)

# Convert credit_default and mortgage columns to boolean
client_df["credit_default"] = (client_df["credit_default"] == "yes").astype(bool)
client_df["mortgage"] = (client_df["mortgage"] == "yes").astype(bool)

# Save client df to client.csv
client_df.to_csv("client.csv", index=False)
#-------------------------------

# Cleaning for campaign.csv
campaign_df = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]

# Convert previous_outcome and campaign_outcome columns to boolean
campaign_df["previous_outcome"] = (campaign_df["previous_outcome"] == "success").astype(bool)
campaign_df["campaign_outcome"] = (campaign_df["campaign_outcome"] == "yes").astype(bool)

# Create last_contact_date column from day and month
campaign_df["last_contact_date"] = pd.to_datetime(
    df["day"].astype(str) + " " + df["month"] + " 2022",
    format="%d %b %Y"
).dt.date

# Save campaign df to campaign.csv
campaign_df.to_csv("campaign.csv", index=False)
#-------------------------------

# Cleaning for economics.csv
economics_df = df[["client_id", "cons_price_idx", "euribor_three_months"]]

# Save economics df to economics.csv
economics_df.to_csv("economics.csv", index=False)