import path
import charts
import filter

def run():
    data = path.read_csv('Digital Portfolio/Project_2.py/data_p.csv')
    f_data = filter.population_by_country(data)

    if  len(f_data) > 0:
        c_year = list(map(lambda x: x['Year'], f_data))
        c_emission = list(map(lambda x: x['Total'], f_data))
        labels = list(map(lambda x: int(x), c_year))
        values = list(map(lambda x: float(x), c_emission))
        charts.generate_bar_chart(labels,values)


if __name__ == '__main__': 
    run()
