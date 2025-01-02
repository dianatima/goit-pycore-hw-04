def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1     
            average = int(total / count)
        return total, average
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0 

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")