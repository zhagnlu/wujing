#chuandong module
# -*- coding: utf-8 -*-
def make_pidai_product(file_path, write_mode='w'):
    T_L_pairs = {
        "C" : {1700, 1829, 1880, 1900, 1930, 1956, 1981, 2007, 2083, 2100,
               2210, 2235, 2286, 2311, 2337, 2362, 2413, 2438, 2464, 2500, 
               2540, 2565, 2591, 2616, 2650, 2667, 2700, 2718, 2750, 2800,
               2819, 2850, 2870, 2900, 2921, 2950, 2997, 3023, 3048, 3099,
               3124, 3150, 3200, 3226, 3250, 3300, 3350, 3378, 3400, 3450,
               3500, 3550, 3600, 3650, 3700, 3750, 3800, 3861, 3900, 3950, 
               4000, 4064, 4100, 4200, 4250, 4300, 4394, 4450, 4500, 4600},
        "D" : { 2900, 2997, 3048, 3150, 3200, 3250, 3300, 3350, 3400, 3450,
                3500, 3550, 3600, 3650, 3700, 3750, 3800, 3900, 4000, 4050, 
                4100, 4200, 4300, 4500, 4600, 4650, 4900, 5000, 5200, 5300, 
                5400, 5500}
    }
    try: 
        with open(file_path, mode=write_mode, encoding="utf-8") as file:
                # for m, lens in M_L_pair.items():
                #     for l in lens:
                for m in sorted(T_L_pairs.keys()):
                    for l in T_L_pairs[m]:
                        file.write("传动类")
                        file.write(",")
                        file.write("皮带")
                        file.write(',')
                        file.write("皮带{}*{}".format(m, l))
                        file.write("\n")
        print("文件已成功写入: {}".format(file_path))
    except Exception as e:
        print("写入文件时发生错误: {}".format(e))
    
