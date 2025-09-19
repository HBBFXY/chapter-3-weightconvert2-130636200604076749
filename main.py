initial_weight=60
print("年份\t地球体重(kg)\t月球体重(kg)")
for year in range(1, 11):
    earth_weight = initial_weight + 0.5 * year
    moon_weight = earth_weight * 0.165
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
