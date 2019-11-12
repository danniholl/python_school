# paint_1 = {'color': 'green', 'sheen': 'matte'}

# print(paint_1['sheen'])

paint_keys = ['color', 'sheen', 'grade', 'type']
paint_3_list = ['orange', 'semigloss', 'low', 'oil']

paint_3 = {}

for i in range(len(paint_keys)):
    paint_3[paint_keys[i]] = paint_3_list[i]
print(paint_3)

paint_5 = dict(color='pink', sheen='gloss', grade='high')
print(paint_5)