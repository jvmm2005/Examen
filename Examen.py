# Definición de temperaturas para tres semanas diferentes
Week1 = [22, 24, 19, 21, 25, 23, 20]
Week2 = [20, 22, 21, 23, 24, 22, 21]
Week3 = [23, 21, 20, 22, 24, 25, 23]

# Función para verificar si todas las temperaturas en una semana son suaves (entre 20 y 25 grados)
def is_mild_week(week):
    return all(20 <= temperature <= 25 for temperature in week)

# Función para calcular las fluctuaciones diarias de temperatura en una semana
def daily_temperature_fluctuations(week):
    fluctuations = [week[i] - week[i - 1] if i > 0 else 0 for i in range(len(week))]
    return fluctuations

# Función para calcular la temperatura promedio de una semana
def Average_Temperature(week):

    total_temperatures = sum(week)
    average_temperature = total_temperatures / len(week)
    return round(average_temperature)

# Calcular la temperatura promedio para cada semana
Temperature1 = Average_Temperature(Week1)
Temperature2 = Average_Temperature(Week2)
Temperature3 = Average_Temperature(Week3)

# Determinar el día más caluroso de cada semana
hottest_day1 = Week1.index(max(Week1)) + 1
hottest_day2 = Week2.index(max(Week2)) + 1
hottest_day3 = Week3.index(max(Week3)) + 1


# Mostrar la temperatura promedio, temperatura máxima y día más caluroso para cada semana
print ("Media", Temperature1, Temperature2, Temperature3)
print ("Max temperature", max(Week1), max(Week2), max(Week3))
print ("Max temperatures","\nWeek 1 Day", hottest_day1,"\nWeek 2 Day",hottest_day2,"\nWeek 3 Day",hottest_day3)

# Determinar si cada semana fue consistentemente suave o no
mild_weeks = [
    ("Week1", is_mild_week(Week1)),
    ("Week2", is_mild_week(Week2)),
    ("Week3", is_mild_week(Week3))
]


# Mostrar la información de temperatura para cada semana
print("Week  | Average Temperature | Max Temperature | Hottest Day | Consistently Mild")
print("---------------------------------------------------------------------------")
print("Week1 | {:<19} | {:<15} | Day {} | {}".format(Temperature1, max(Week1), hottest_day1, mild_weeks[0][1]))
print("Week2 | {:<19} | {:<15} | Day {} | {}".format(Temperature2, max(Week2), hottest_day2, mild_weeks[1][1]))
print("Week3 | {:<19} | {:<15} | Day {} | {}".format(Temperature3, max(Week3), hottest_day3, mild_weeks[2][1]))

# Mostrar las semanas consistentemente suaves
print("\nConsistently Mild Weeks:")
for week, is_mild in mild_weeks:
    if is_mild:
        print(week)


# Calcular y mostrar las fluctuaciones diarias de temperatura para cada semana
fluctuations_week1 = daily_temperature_fluctuations(Week1)
fluctuations_week2 = daily_temperature_fluctuations(Week2)
fluctuations_week3 = daily_temperature_fluctuations(Week3)

# Formatear la salida para las fluctuaciones diarias
print("Week  | Average Temperature | Max Temperature | Hottest Day | Fluctuations")
print("------------------------------------------------------------------------")
print("Week1 | {:<19} | {:<15} | Day {} | {}".format(Temperature1, max(Week1), hottest_day1, fluctuations_week1))
print("Week2 | {:<19} | {:<15} | Day {} | {}".format(Temperature2, max(Week2), hottest_day2, fluctuations_week2))
print("Week3 | {:<19} | {:<15} | Day {} | {}".format(Temperature3, max(Week3), hottest_day3, fluctuations_week3))