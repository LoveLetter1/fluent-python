dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States')
]
country_dial = {
    country: code for code, country in dial_codes
}
print(country_dial)
# 字典推导式
country_dial_new = {
    code: country.upper() for country, code in sorted(country_dial.items()) if code < 70
}
print(country_dial_new)


# 映射拆包
def dump(**kwargs):
    return kwargs


print(dump(**{'x': 1}, y=2, **{'z': 3}))
# 合并映射
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1 | d2)
