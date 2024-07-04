def run():
  
  ones = [
    0,
    len("one"),
    len("two"),
    len("three"),
    len("four"),
    len("five"),
    len("six"),
    len("seven"),
    len("eight"),
    len("nine")
  ]
  
  teens = [
    0,
    len("ten"),
    len("eleven"),
    len("twelve"),
    len("thirteen"),
    len("fourteen"),
    len("fifteen"),
    len("sixteen"),
    len("seventeen"),
    len("eighteen"),
    len("nineteen"),
  ]
  
  tens = [
    0,
    len("ten"),
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety")
  ]
  
  hundred = len("hundred")
  thousand = len("thousand")
  
  and_ = len("and")
  
  total = 0
  
  for i in range(1,1000+1):
    number = 0
    if i == 1000:
      number = ones[1] + thousand
    else:
      if i % 100 < 20 and i % 100 >= 10:
        number = teens[(i % 100)-9]
      else:
        if i % 10 != 0:
          number = ones[i % 10]
        if i > 10 and i % 100 != 0:
          number = number + tens[(i // 10) % 10]
  
      if i >= 100:
        if number > 0:
          number = number + and_
  
        number = number + hundred
      number = number + ones[i // 100]
  
    print(i, number)
    total = total + number
  
  print(total)