def average(salary: list[int]):
    """
    You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
    Return the average salary of employees excluding the minimum and maximum salary.
    Answers within 10-5 of the actual answer will be accepted.
    """
    max_el, min_el = max(salary), min(salary)
    summa = counter = 0
    for i in salary:
        if i not in (max_el, min_el):
            summa += i
            counter += 1
    return summa / counter


print(average([4000, 3000, 1000, 2000]))
print(average([1000, 2000, 3000]))
