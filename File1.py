import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_excel('C:\\Users\\Amrita Mukherjee\\OneDrive\\Documents\\Python_lib\\Testdata1.xlsx')

print(data)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))     
sns.barplot(x='Sprint', y='Story', data=data)
plt.xlabel('Sprint')    
plt.ylabel('Story')
plt.title('Sprint vs Story')
plt.show()

#plt.title('Sprint vs Story')