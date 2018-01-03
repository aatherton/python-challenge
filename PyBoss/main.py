# declare variables
fileLocations = ["employee_data1.csv", "employee_data2.csv"]
outbox = "outbox.csv"
stateswap = {
	'Alabama': 'AL',
	'Alaska': 'AK',
	'Arizona': 'AZ',
	'Arkansas': 'AR',
	'California': 'CA',
	'Colorado': 'CO',
	'Connecticut': 'CT',
	'Delaware': 'DE',
	'Florida': 'FL',
	'Georgia': 'GA',
	'Hawaii': 'HI',
	'Idaho': 'ID',
	'Illinois': 'IL',
	'Indiana': 'IN',
	'Iowa': 'IA',
	'Kansas': 'KS',
	'Kentucky': 'KY',
	'Louisiana': 'LA',
	'Maine': 'ME',
	'Maryland': 'MD',
	'Massachusetts': 'MA',
	'Michigan': 'MI',
	'Minnesota': 'MN',
	'Mississippi': 'MS',
	'Missouri': 'MO',
	'Montana': 'MT',
	'Nebraska': 'NE',
	'Nevada': 'NV',
	'New Hampshire': 'NH',
	'New Jersey': 'NJ',
	'New Mexico': 'NM',
	'New York': 'NY',
	'North Carolina': 'NC',
	'North Dakota': 'ND',
	'Ohio': 'OH',
	'Oklahoma': 'OK',
	'Oregon': 'OR',
	'Pennsylvania': 'PA',
	'Rhode Island': 'RI',
	'South Carolina': 'SC',
	'South Dakota': 'SD',
	'Tennessee': 'TN',
	'Texas': 'TX',
	'Utah': 'UT',
	'Vermont': 'VT',
	'Virginia': 'VA',
	'Washington': 'WA',
	'West Virginia': 'WV',
	'Wisconsin': 'WI',
	'Wyoming': 'WY',
}
# set up output file
with open(outbox, "w") as ball:
	ball.write("Emp ID,First Name,Last Name,DOB,SSN,State")
# open input file
for inbox in fileLocations:
	with open(inbox, "r") as openedbox:
		# skip header
		next(openedbox)
		# for each line
		for each in openedbox:
			# separate it by comma
			line = each.split(",")
			# set result as the first entry plus a comma
			result = str(line[1]) + ","
			# separate second entry by space
			line[1] = line[1].split(" ")
			# append [0],[1], to result
			result += str(line[1][0]) + "," + str(line[1][1]) + ","
			# separate third entry by -
			line[2] = line[2].split("-")
			# append [1]/[2]/[0], to result
			result += str(line[2][1]) + "/" + str(line[2][2]) + "/" + str(line[2][0]) + ","
			# separate fourth entry by -
			line[3] = line[3].split("-")
			# append ***-**-[2], to result
			result += "***-**-" + str(line[3][2]) + ","
			# append fifth entry's associated value to result
			result += str(stateswap[line[4][:-1]]) + ","
			# the -1 is because this part of the line has the newline character. that bit cuts it
			# write result to output file
			with open(outbox, "a") as ball:
				ball.write("\n" + result)