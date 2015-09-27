import sqlite3
import pprint

conn = sqlite3.connect('./kayak.sqlite')
c = conn.cursor()

visits_by_month = {}
query = "select * from visits"
for row in c.execute(query):
	bits = row[0].split('-')
	key = bits[0] + '-' + bits[1]
	if key not in visits_by_month:
		visits_by_month[key] = 0
	visits_by_month[key] += row[3]


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(visits_by_month)