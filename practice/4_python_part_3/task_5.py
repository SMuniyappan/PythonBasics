"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
import os
import json
import xml.etree.ElementTree as ET

def calculate_statistics(city_data):
    temperatures = [hour['temp'] for hour in city_data]
    wind_speeds = [hour['wind_speed'] for hour in city_data]

    mean_temp = round(sum(temperatures) / len(temperatures), 2)
    max_temp = round(max(temperatures), 2)
    min_temp = round(min(temperatures), 2)

    mean_wind_speed = round(sum(wind_speeds) / len(wind_speeds), 2)
    max_wind_speed = round(max(wind_speeds), 2)
    min_wind_speed = round(min(wind_speeds), 2)

    return mean_temp, max_temp, min_temp, mean_wind_speed, max_wind_speed, min_wind_speed

def process_city(city_name, city_data):
    mean_temp, max_temp, min_temp, mean_wind_speed, max_wind_speed, min_wind_speed = calculate_statistics(city_data)

    city_element = ET.Element(city_name)
    city_element.set('mean_temp', str(mean_temp))
    city_element.set('max_temp', str(max_temp))
    city_element.set('min_temp', str(min_temp))
    city_element.set('mean_wind_speed', str(mean_wind_speed))
    city_element.set('max_wind_speed', str(max_wind_speed))
    city_element.set('min_wind_speed', str(min_wind_speed))

    return city_element, mean_temp, mean_wind_speed

def process_dataset(dataset_path):
    country_data = []

    for city_folder in os.listdir(dataset_path):
        city_path = os.path.join(dataset_path, city_folder)
        if os.path.isdir(city_path):
            with open(os.path.join(city_path, '2021-09-25.json'), 'r') as file:
                city_data = json.load(file)['hourly']
                city_element, mean_temp, mean_wind_speed = process_city(city_folder, city_data)
                country_data.append((city_folder, mean_temp, mean_wind_speed))

    country_mean_temp = round(sum([data[1] for data in country_data]) / len(country_data), 2)
    country_mean_wind_speed = round(sum([data[2] for data in country_data]) / len(country_data), 2)

    coldest_city, warmest_city, windiest_city = min(country_data, key=lambda x: x[1]), \
        max(country_data, key=lambda x: x[1]), \
        max(country_data, key=lambda x: x[2])

    return country_mean_temp, country_mean_wind_speed, coldest_city, warmest_city, windiest_city

def build_xml(country_mean_temp, country_mean_wind_speed, coldest_city, warmest_city, windiest_city, cities_data):
    root = ET.Element('weather', country='Spain', date='2021-09-25')

    summary = ET.SubElement(root, 'summary')
    summary.set('mean_temp', str(country_mean_temp))
    summary.set('mean_wind_speed', str(country_mean_wind_speed))
    summary.set('coldest_place', coldest_city[0])
    summary.set('warmest_place', warmest_city[0])
    summary.set('windiest_place', windiest_city[0])

    cities = ET.SubElement(root, 'cities')

    for city_name, mean_temp, max_temp, min_temp, mean_wind_speed, max_wind_speed, min_wind_speed in cities_data:
        city_element = ET.SubElement(cities, city_name)
        city_element.set('mean_temp', str(mean_temp))
        city_element.set('max_temp', str(max_temp))
        city_element.set('min_temp', str(min_temp))
        city_element.set('mean_wind_speed', str(mean_wind_speed))
        city_element.set('max_wind_speed', str(max_wind_speed))
        city_element.set('min_wind_speed', str(min_wind_speed))

    tree = ET.ElementTree(root)
    tree.write('weather_spain.xml')

def main():
    dataset_path = 'path/to/your/dataset'

    country_mean_temp, country_mean_wind_speed, coldest_city, warmest_city, windiest_city = process_dataset(dataset_path)

    cities_data = []
    for city_folder, _, _ in os.walk(dataset_path):
        if city_folder != dataset_path:
            with open(os.path.join(city_folder, '2021-09-25.json'), 'r') as file:
                city_data = json.load(file)['hourly']
                mean_temp, max_temp, min_temp, mean_wind_speed, max_wind_speed, min_wind_speed = calculate_statistics(city_data)
                cities_data.append((os.path.basename(city_folder), mean_temp, max_temp, min_temp,
                                    mean_wind_speed, max_wind_speed, min_wind_speed))

    build_xml(country_mean_temp, country_mean_wind_speed, coldest_city, warmest_city, windiest_city, cities_data)

if __name__ == '__main__':
    main()




"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
