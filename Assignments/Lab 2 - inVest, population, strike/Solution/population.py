#!/usr/bin/env python3

#----------------------------------------------------------------------
# population.py
# Dave Reed
# 08/28/2012
#----------------------------------------------------------------------

def main():

	years = eval(input('Enter number of years: '))
	# 365.25 days in a year, 24 hours in a day, 3600 seconds in an hour
	seconds = years * 365.25 * 24 * 60 * 60
	
	# birth every 8 seconds
	births = seconds / 8
	# death every 14 seconds
	deaths = seconds / 14
	# immigrant every 46 seconds
	immigrants = seconds / 46
	
	# assume current population is 314,254,374
	population = int(round(314254374 + births - deaths + immigrants))
	print('The estimated population in', years, 'years is', population)

#----------------------------------------------------------------------

main()
