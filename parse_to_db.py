import csv
import sqlite3

conn = sqlite3.connect('./kayak.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE channel(name text, site text, description text)')


i = 0

with open('channel_descriptions.csv', 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		if i > 0:
			query = "INSERT INTO channel VALUES ('%s','%s','%s')" % (row[0], row[1], row[2])
			c.execute(query)
		i += 1


c.execute('CREATE TABLE visits(date text, country_code text, channel text, user_visits integer)')
i = 0

with open('visits.csv', 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		if i > 0:
			query = "INSERT INTO visits VALUES ('%s','%s','%s', '%s')" % (row[0], row[1], row[2], row[3])
			c.execute(query)
		i += 1


c.execute('CREATE TABLE conversions(date text, country_code text, channel text, conversions integer)')
i = 0

with open('conversions.csv', 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		if i > 0:
			query = "INSERT INTO conversions VALUES ('%s','%s','%s', '%s')" % (row[0], row[1], row[2], row[3])
			c.execute(query)
		i += 1

conn.commit()
conn.close()
