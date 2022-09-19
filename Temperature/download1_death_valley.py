import csv
from datetime import date, datetime

import matplotlib.pyplot as plt


filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, low_temp = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # конвертируем даты в столбике 2
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing DATA for {current_date}")
        else:    
            dates.append(current_date)
            highs.append(high)
            low_temp.append(low)
"""гр-ик температур"""
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6) # добавляем DATES, ALPHA - насыщенность
ax.plot(dates, low_temp, c='blue', alpha=0.6) # НИЗКИЕ ТЕМПЕРАТУРЫ
plt.fill_between(dates, highs, low_temp, facecolor='black', alpha=0.2) # цвет фона между линиями
"""отформатируем гр-ик"""
plt.title("Table temperature Death Valley 2018", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate() #метод, чтобы ДАТЫ ВНИЗУ гр-ка НЕ СЛИПАЛИСЬ
plt.ylabel("Temperature, F", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()