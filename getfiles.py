import datetime
def getDateList(start, end, user):

	def returnDates():
		daysInMonth = range(1, 32)
	
		months = range(1, 13)
		years = [2014, 2015, 2016, 2017]
	
		dateList = []
	
		for year in years:
			for month in months:
				for day in daysInMonth:
					try:
						thedate = datetime.date(year, month, day)
						dateList.append(thedate)
					except ValueError as e:
						pass

		return dateList

	def appendStrings(start, end, user):
		dates = returnDates()
	
		main = 'https://www.twitter.com'
		#first = '/search?l=&q=bitcoin' + "%" + "20since%3A"
		first = '/search?l=&q=from' + "%" + "3A" 
		second = "%" + "20" + "since%3A"
		third = "%" + "20until%3A"
		fourth = "&src=typd&lang=en"
	
		final = []
		
		startArray = start.split('-')
		endArray = end.split('-')

		startDate = datetime.date(int(startArray[0]), int(startArray[1]), int(startArray[2]))
		endDate = datetime.date(int(endArray[0]), int(endArray[1]), int(endArray[2]))


		newArray = []

		go = False
		for date in dates:
			if(date == startDate):
				go = True
			if(date == endDate):
				go = False
			if(go == True):
				newArray.append(date)

		dateLength = len(newArray)
		inc = 0
		while(inc < dateLength):
			try:
				newdate = main + first + user + second + newArray[inc].strftime('%Y-%m-%d') + third + newArray[inc + 1].strftime('%Y-%m-%d') + fourth
				final.append(newdate)
				inc += 1
			except IndexError as e:
				inc += 1
				pass
			except ValueError as e:
				inc += 1
				print(e)
				pass

		return final

	finalurls = appendStrings(start, end, user)
	return finalurls


####
# getDateList() returns a list of all dates - change the array of years to change the timeframe
searchStartDate = '2014-01-01'
searchEndDate = '2017-01-01'
searchUser = 'calvin_choe'

dateList = getDateList(searchStartDate, searchEndDate, searchUser)


