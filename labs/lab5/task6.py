def exp_filt(mass, numb):
    output_data = [mass[0]]
    for i in range(1, len(mass)):
        output_data.append(numb * mass[i] + (1 - numb) * output_data[i-1])
    return output_data


print(exp_filt([2, 3, 4, 5, 6], 0.1))