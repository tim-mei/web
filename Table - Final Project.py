#Takes a list generated from Final_Lists

#The list that is used was a randomly generated one from the program. You may
#change this to see how the graphs differ.

Rate_1 = ['10000,0.16,1']
Rate_2 = ['10000,0.15,1']
model = [[10000.0, 11600.0, 13455.999999999998, 15608.959999999995, 18106.393599999996, 21003.416575999992, 24363.96322815999, 28262.197344665587, 32784.148919812076, 38029.612746982006, 44114.350786499126, 51172.64691233898, 59360.270418313215, 68857.91368524331, 79875.17987488225, 92655.20865486341, 107480.04203964154, 124676.84876598419, 144625.14456854164, 167765.16769950828], [10000.0, 11500.0, 13224.999999999998, 15208.749999999998, 17490.062499999993, 20113.571874999994, 23130.60765624999, 26600.198804687487, 30590.228625390606, 35178.762919199195, 40455.57735707907, 46523.91396064092, 53502.50105473706, 61527.876212947616, 70757.05764488975, 81370.61629162321, 93576.20873536667, 107612.64004567168, 123754.53605252241, 142317.71646040076]]

def make_table(a):
    x = 0
    s = '''<table>
            <thead>
                <tr>
                    <th>Initial Value</th>
                    <th>Rate</th>
                    <th>Compoundings</th>
                    <th>Years Since First Compound</th>
                    <th>Value</th>
                    <th>Initial Value</th>
                    <th>Rate</th>
                    <th>Compoundings</th>
                    <th>Years Since First Compound</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>\n'''
    while x < len(a[0]):
        s+= '<tr>\n'
        s+= '<td>' + str(10000) + '</td>\n'
        s+= '<td>' + str('0.16%') + '</td>\n'
        s+= '<td>' + str(1) + '</td>\n'
        s+= '<td>' + str(x) + '</td>\n'
        s+= '<td>' + str(a[0][x]) + '</td>\n'
        s+= '<td>' + str(10000) + '</td>\n'
        s+= '<td>' + str('0.15%') + '</td>\n'
        s+= '<td>' + str(1) + '</td>\n'
        s+= '<td>' + str(x) + '</td>\n'
        s+= '<td>' + str(a[1][x]) + '</td>\n'
        s+= '</tr>\n'
        x += 1
    s+= '</tbody></table>'
    return s
print(make_table(model))


