import sqlite3
import pprint

conn = sqlite3.connect('./kayak.sqlite')
c = conn.cursor()

visits_by_month = {}

# {
# 	2015-08: {
# 		de: 0,
# 		es: 0
# 	}
# }

query = "select * from visits"
for row in c.execute(query):
	bits = row[0].split('-')
	key = bits[0] + '-' + bits[1]

	if key not in visits_by_month:
		visits_by_month[key] = {}

	key_country = row[1]
	if key_country not in visits_by_month[key]:
		visits_by_month[key][key_country] = 0

	visits_by_month[key][key_country] += row[3]


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(visits_by_month)