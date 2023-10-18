import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
data = pd.read_csv('police_project.csv', sep=',')

# Задача 1: Перевірте, білих чи темношкірих людей частіше зупиняє поліція
race_counts = data['human_race'].value_counts()
print("Частота зупинок за расою:")
print(race_counts)

# Задача 2: З’ясуйте, як частота зупинок через наркотики залежить від часу доби
drug_stops = data[data['violation_reason'] == 'drugs']
drug_stops['stop_time'] = pd.to_datetime(drug_stops['stop_time'], format='%H:%M')
drug_stops['hour'] = drug_stops['stop_time'].dt.hour
hourly_counts = drug_stops['hour'].value_counts().sort_index()
hourly_counts.plot(kind='bar', title='Частота зупинок через наркотики за годинами')
plt.xlabel('Година доби')
plt.ylabel('Кількість зупинок')
plt.show()


# Задача 3: Чи правда, що більшість зупинок водіїв трапляється вночі?
data['stop_time'] = pd.to_datetime(data['stop_time'], format='%H:%M')
data['hour'] = data['stop_time'].dt.hour

plt.hist(data['hour'], bins=24, rwidth=0.8, alpha=0.7, color='blue')
plt.title('Розподіл кількості зупинок за годинами')
plt.xlabel('Година доби')
plt.ylabel('Кількість зупинок')
plt.xticks(range(24))
plt.show()

# Задача 4: Виявіть хибні дані в стовпці 'stop_duration' та замініть їх на NaN
data['stop_duration'] = pd.to_numeric(data['stop_duration'], errors='coerce')

# Задача 5: Визначте середній час зупинки для кожної з причин зупинки
violation_avg_duration = data.groupby('violation_raw')['stop_duration'].mean()
violation_avg_duration.plot(kind='bar', title='Середній час зупинки за причиною зупинки')
plt.xlabel('Причина зупинки')
plt.ylabel('Середній час зупинки (хв)')
plt.xticks(rotation=90)
plt.show()