with open ("Файл 1") as f:
  date = f.readlines()
  a = len(date)
  c = "Файл 1, 2"
with open ("Файл 2") as f:
  date_1 = f.readlines()
  b = len(date_1)
  d = "Файл 2, 1"
with open ("Файл 3", "w") as document:
  if a > b:
    e = " ".join(date)
    document.write(c)
    document.write(e)
  else:
    k = " ".join(date_1)
    document.write(d)
    document.write(date_1)
with open ("Файл 3") as f:
  date_2 = f.read()
  print(date_2)