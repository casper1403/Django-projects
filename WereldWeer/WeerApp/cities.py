from datapackage import Package
from data import get_weather_data
import json

package = Package('https://datahub.io/core/world-cities/datapackage.json')

# print list of all resources:

citylist = []
# # print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        for i,city in enumerate(resource.read()):
            citylist.append({"model":"WeerApp.City",
                            "pk":i,
                            "fields":{
                                "name":city[0],
                                "country":city[1],
                                "subcountry":city[2],
                                "geonameid":city[3]
                              }
                            })

with open(r"cities.json", 'w', encoding='utf8') as fout:
    json.dump(citylist,fout,ensure_ascii=False)
