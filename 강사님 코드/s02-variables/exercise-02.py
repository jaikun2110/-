# [문제3]
# 한 달 급여가 400만원이다.
# 분기별 보너스는 월급여의 30%가 지급된다.
# 세금은 월급여의 3%이다.
# 보너스에 대한 세금은 없다.
# 월세후 수령액은 얼마인가?
# 연 총세금은 얼마인가?
# 세후 연수령액은 얼마인가?

#%%
# 한 달 급여가 400만원이다.
salary = 4000000
print("급여:", salary)

#%%
# 분기별 보너스는 월급여의 30%가 지급된다.
bonus = salary * 0.3
print("보너스(분기별):", bonus)

#%%
# 세금은 월급여의 3%이다.
tax = salary * 0.03
print("세금:", tax)

#%%
# 월 세후 수령액은 얼마인가?
pay = salary - tax
print("월급여(세후):", pay)

#%%

# 총연봉
total = salary * 12
total += bonus * 4
print("총연봉:", total)

#%%
# 연 총세금은 얼마인가?
total_tax = tax * 12
print("총세금:", total_tax)

#%%
# 세후 연수령액은 얼마인가?
year_salary = pay * 12
year_salary += bonus * 4
print("연수령:", year_salary)
print("연수령:", total - total_tax, '검산액')
