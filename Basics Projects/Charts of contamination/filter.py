def population_by_country(data):
    f_data = list(filter(lambda item : item['Country'] == 'Global',data))
    f_year = list(filter(lambda f: f['Year'] >= '2015', f_data))
    return f_year

