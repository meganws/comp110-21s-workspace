"""testing some int and str stuff"""

gme: float = 20.0
print("01/11: " + str(gme))
fund_short: float = gme
reddit_share: float = gme

gme = gme + 130.0
print("01/26: " + str(gme))
print("fund: " + str(fund_short - gme))
print("reddit: " + str(gme-reddit_share))

gme = 200.0 + gme
print("01/27: " + str(gme))
print("fund: " + str(fund_short - gme))
print("reddit: " + str(gme-reddit_share))
