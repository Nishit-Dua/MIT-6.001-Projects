annual_salary = int(input('Enter the starting salary:​ '))

total_cost = 1000000  # Million
portion_down_payment = .25*total_cost
r = 0.04
semi_annual_raise = 0.07
DONT = True

months_ftw = 36
current_savings = 0
low = 0
integer_accuracy = high = 10000
accuracy = .001
itteration = 0

while not ((1 - accuracy)*portion_down_payment <=
           current_savings <= (1 + accuracy)*portion_down_payment):

    current_savings = 0
    months = 0
    itteration += 1
    montlh_salary = (annual_salary/12)
    portion_saved = (low + high) / (2*integer_accuracy)

    for x in range(months_ftw):
        current_savings += current_savings*r/12
        current_savings += portion_saved*montlh_salary
        months += 1
        if months % 6 == 0:
            montlh_salary += montlh_salary*semi_annual_raise

    if current_savings < portion_down_payment:
        low = portion_saved*integer_accuracy
    elif current_savings > portion_down_payment:
        high = portion_saved*integer_accuracy

    # print(portion_saved, high, low, current_savings)

    if portion_saved > .98:
        print('\nIt is not possible to pay the down payment in three years.')
        DONT = False
        break

if DONT:
    print(f'\nBest savings rate:​ {portion_saved: .5f}')
    print(f'Steps in bisection search:​ {itteration}')
