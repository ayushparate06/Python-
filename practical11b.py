import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("recruitment.csv")

# a) Bar Chart
plt.figure()
plt.bar(df['Company'], df['Recruitments'])
plt.title("New Recruitments in Companies")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()


# b) Pie Chart
plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()


# c) Customized Pie Chart
plt.figure()
explode = [0.1 if company == 'Amazon' else 0 for company in df['Company']]  # highlight Amazon

plt.pie(df['Recruitments'],
        labels=df['Company'],
        autopct='%1.1f%%',
        explode=explode,
        shadow=True,
        startangle=140)

plt.title("Customized Recruitment Pie Chart")
plt.show()


# d) Doughnut Chart
plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart of Recruitments")
plt.show()


# e) Compare IBM & Amdocs
compare_df = df[df['Company'].isin(['IBM', 'Amdocs'])]

plt.figure()
plt.bar(compare_df['Company'], compare_df['Recruitments'])
plt.title("Comparison: IBM vs Amdocs Recruitments")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.show()