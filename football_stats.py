#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 9 Football stock """


from bs4 import BeautifulSoup
import urllib2
import csv

url = "http://www.cbssports.com/nfl/stats/playersort/nfl/year-2014-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


ths = soup.find_all('th')
datatable = None
tables = soup.find_all('table')
for table in tables:
	tableclass = str(table.get('class'))
	if(tableclass == 'data'):
		datatable = table
			
		
	
trs = table.find_all('tr')
i = 0
for tr in trs:
        try:
                if i < 20:
                        tds = tr.find_all('td')
                        name = str(tds[0].get_text())
			pos = str(tds[1].get_text())
			team = str(tds[2].get_text())
			touchdowns = str(tds[6].get_text())
			print "Player: %s \t Position: %s \t Team: %s \t Touchdowns: %s" % (name,pos,team,touchdowns)
			i = i + 1
		else:
                        break

         except:
                 continue