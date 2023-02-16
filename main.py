stocks_dict = {
  "NKE": "23.23",
  "UA": "30.30",
  "MSGE": "33.33",
  "MGM": "10.23",
  "FL": "3.99",
  "TTWO": "2.11",
  "PUMSY": "23.05",
  "CCOEF": "2.02",
  "ADS": "3.03",
  "ROX": ".97",
}
x = input("Please enter your stock symbol:")

z = stocks_dict.get(x, "Ticker Not Found")
print (z)
