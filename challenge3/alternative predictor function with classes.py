import math, json

class teamResults:
	def __init__(self, ccwm1, ccwm2, ccwm3, wins1, wins2, wins3, losses1, losses2, losses3):
		# Initiates teamResults instance
		self.ccwm1 = ccwm1
		self.ccwm2 = ccwm2
		self.ccwm3 = ccwm3
		self.wins1 = wins1
		self.wins2 = wins2
		self.wins3 = wins3
		self.losses1 = losses1
		self.losses2 = losses2
		self.losses3 = losses3
		if self.losses1 != 0:
			self.wl1 = self.wins1 / self.losses1
		else:
			self.lossesBeingZero = True
		if self.losses2 != 0:
			self.wl2 = self.wins2 / self.losses2
		else:
			self.lossesBeingZero = True
		if self.losses3 != 0:
			self.wl3 = self.wins3 / self.losses3
		else:
			self.lossesBeingZero = True
		# These conditionals above find win-loss ratios and modify the self.lossesBeingZero variable in the case of a zero amount of losses

	def findVictoriesAmount(self):
		# Finds predicted victories probability for team executing function
		if self.lossesBeingZero = True:
			# If any of the losses values are zero, returns zero to signify impossible functions
			return 0
		else:
			exponentValue = self.ccwm1 + 35 * math.log(self.wl1) + self.ccwm2 + 35 * math.log(self.wl2) + self.ccwm3 + 35 * math.log(self.wl3)
			return 1.01 ** exponentValue

resultsInstance = teamResults(1, 1, 1, 1, 1, 1, 1, 1, 1)
# Test instance

print resultsInstance.findVictoriesAmount()
# Prints out probability of test instance