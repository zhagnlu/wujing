
# -*- coding: utf-8 -*-
import os


def make_neiliujiao_product(file_path):
    types = ['8.8级镀锌内六角螺丝', '8.8级发黑内六角螺丝', '12.9级内六角螺丝']
    M_L_pair = { 3: {5, 6, 8, 10, 12, 14, 16, 18, 20, 25, 28, 30, 32, 35, 40},
                 4: {5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40,
                    45, 50},
                 5: {8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45,
                    50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100},
                 6: {8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45,
                    50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115,
                    120, 125, 130, 140, 150},
                 8: {10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50,
                    55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120,
                    125, 130, 140, 150, 160, 170, 180, 190, 200},
                 10: {12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50,  
                     55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120,
                     125, 130, 140, 150, 160, 170, 180, 190, 200},
                 12: {16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50,  
                     55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120,
                     125, 130, 140, 150, 160, 170, 180, 190, 200},
                 14: {25, 28, 30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200},
                 16: {25, 28, 30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300},
                 18: {30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 20: {30, 32, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 22: {50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 24: {50, 55, 60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 27: {60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 30: {60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                 36: {60, 65, 70, 75, 80, 85, 
                     90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170,
                     180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,300},
                }
    
    try: 
        with open(file_path, mode="w", encoding="utf-8") as file:
            for main_type in types:
                for m, lens in M_L_pair.items():
                    for l in lens:
                        file.write("螺丝")
                        file.write(",")
                        file.write("内六角螺丝")
                        file.write(',')
                        file.write("{}M{}*{}".format(main_type, m, l))
                        file.write("\n")
        print("文件已成功写入: {}".format(file_path))
    except Exception as e:
        print("写入文件时发生错误: {}".format(e))


if __name__ == "__main__":
    make_neiliujiao_product("neiliujiap.csv")
                