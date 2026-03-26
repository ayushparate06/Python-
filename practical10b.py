import pandas as pd

data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Karnataka', 'Tamil Nadu'],
    'Area': [307713, 196244, 342239, 191791, 130058],
    'Population': [124000000, 70000000, 81000000, 68000000, 78000000]
}

df = pd.DataFrame(data)

print("\n--- Complete State Information ---")
print(df)

# Largest Area
print("\nState with Largest Area:", df.loc[df['Area'].idxmax()]['State'])

# Largest Population
print("\nState with Largest Population:", df.loc[df['Population'].idxmax()]['State'])

# Population Density
df['Density'] = df['Population'] / df['Area']
print("\n--- Population Density ---")
print(df[['State', 'Density']])

# Highest Density
print("\nState with Highest Population Density:", df.loc[df['Density'].idxmax()]['State'])