from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Load dataset
df = pd.read_csv('cleaned_traffic_accidents.csv')

date_column = 'crash_date'
if date_column in df.columns:
    df[date_column] = pd.to_datetime(df[date_column])
else:
    raise ValueError(f"Column '{date_column}' not found in the CSV file.")

# Crash_hour to integer
df['crash_hour'] = df['crash_hour'].astype(int)

def generate_plot(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return image_base64

@app.route('/')
def index():
    
    total_accidents = len(df)
    most_common_cause = df['prim_contributory_cause'].mode()[0]
    most_frequent_weather = df['weather_condition'].mode()[0]
    peak_hour = df['crash_hour'].mode()[0]
    
    day_map = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
               5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    df['day_name'] = df['crash_day_of_week'].map(day_map)
    most_frequent_day = df['day_name'].mode()[0]
    
    average_damage = df['damage'].value_counts().idxmax()

    # Visualization 1: Accidents by Hour of Day
    plt.figure(figsize=(14, 7))
    sns.histplot(data=df, x='crash_hour', bins=24, kde=True, color='#1f77b4')
    plt.title('Accident Distribution by Hour of Day', fontsize=16, pad=20)
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Number of Accidents', fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plot1 = generate_plot(plt.gcf())
    plt.clf()

    # Visualization 2: Top 10 Contributory Causes
    plt.figure(figsize=(14, 8))
    cause_counts = df['prim_contributory_cause'].value_counts().nlargest(10)
    sns.barplot(x=cause_counts.values, y=cause_counts.index, palette='viridis')
    plt.title('Top 10 Primary Contributory Causes', fontsize=16, pad=20)
    plt.xlabel('Number of Accidents', fontsize=12)
    plt.ylabel('')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plot2 = generate_plot(plt.gcf())
    plt.clf()

    # Visualization 3: Weather Condition Distribution
    threshold = 0.02
    weather_counts = df['weather_condition'].value_counts(normalize=True)
    small_categories = weather_counts[weather_counts < threshold].index
    df['weather_condition_combined'] = df['weather_condition'].replace(small_categories, 'OTHER')
    weather_counts_combined = df['weather_condition_combined'].value_counts()
    explode = [0.1 if w == 'CLEAR' else 0 for w in weather_counts_combined.index]
    colors = sns.color_palette('pastel')[0:len(weather_counts_combined)]
    plt.pie(weather_counts_combined, labels=None, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True, pctdistance=0.85)
    plt.legend(weather_counts_combined.index, title="Weather Conditions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Accident Distribution by Weather Conditions', fontsize=16, pad=20)
    plt.tight_layout()
    plot3 = generate_plot(plt.gcf())
    plt.clf()

    # Visualization 4: Accidents by Day of Week
    plt.figure(figsize=(14, 7))
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sns.countplot(data=df, x='day_name', order=day_order, palette='coolwarm')
    plt.title('Accidents by Day of Week', fontsize=16, pad=20)
    plt.xlabel('')
    plt.ylabel('Number of Accidents', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plot4 = generate_plot(plt.gcf())
    plt.clf()

    # Visualization 5: Heatmap: Accidents by Hour and Day
    plt.figure(figsize=(16, 9))
    heatmap_data = df.pivot_table(index='day_name', columns='crash_hour', 
                                  values='crash_date', aggfunc='count', fill_value=0)
    heatmap_data = heatmap_data.reindex(day_order)
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False, fmt='d')
    plt.title('Accident Hotspots: Hour vs Day of Week', fontsize=16, pad=20)
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Day of Week', fontsize=12)
    plt.tight_layout()
    plot5 = generate_plot(plt.gcf())
    plt.clf()

    # Visualization 6: Damage Cost Distribution
    plt.figure(figsize=(14, 7))
    damage_order = ['$500 OR LESS', '$501 - $1,500', 'OVER $1,500']
    sns.countplot(data=df, y='damage', order=damage_order, palette='rocket_r')
    plt.title('Accident Severity by Damage Cost', fontsize=16, pad=20)
    plt.xlabel('Number of Accidents', fontsize=12)
    plt.ylabel('Damage Range', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plot6 = generate_plot(plt.gcf())
    plt.clf()

    return render_template('index.html', 
                           plot1=plot1, plot2=plot2, plot3=plot3, plot4=plot4,
                           plot5=plot5, plot6=plot6,
                           total_accidents=total_accidents,
                           most_common_cause=most_common_cause,
                           most_frequent_weather=most_frequent_weather,
                           peak_hour=peak_hour,
                           most_frequent_day=most_frequent_day,
                           average_damage=average_damage)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
