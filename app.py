from datetime import date 

minha_data = date(2023, 2, 24)

print(minha_data)

print(minha_data.year)
print(minha_data.month)
print(minha_data.day)

outra_data = date(2022, 12, 31)

diferenca = minha_data - outra_data 

print(diferenca.days)