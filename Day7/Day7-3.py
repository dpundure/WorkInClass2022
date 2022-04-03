def get_city_year (p0, perc, delta, p, years=1):
    population = p0 * (1 + (perc /100)) + delta
    if p0 > population:
        return -1
    if population >= p:
        return years
    else:
        return get_city_year(population, perc, delta, p, years +1)

print(get_city_year(1000, 2, 50, 1200))