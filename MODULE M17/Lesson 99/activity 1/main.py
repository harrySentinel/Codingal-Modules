p_rain = 0.4
p_traffic_given_rain = 0.8
p_traffic_given_no_rain = 0.3

p_no_rain = 1 - p_rain
p_traffic = (p_traffic_given_rain * p_rain) + (p_traffic_given_no_rain * p_no_rain)

print("Conditional Probability Example")
print()
print("P(Rain)                  =", p_rain)
print("P(Traffic | Rain)        =", p_traffic_given_rain)
print("P(Traffic | No Rain)     =", p_traffic_given_no_rain)
print()
print("P(Traffic) =", round(p_traffic, 2))
print()

p_rain_given_traffic = (p_traffic_given_rain * p_rain) / p_traffic
print("P(Rain | Traffic) =", round(p_rain_given_traffic, 2))
print("If there's traffic, probability it rained =", round(p_rain_given_traffic * 100, 1), "%")
