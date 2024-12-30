#dianpian module
def make_tandian_product(file_path, write_mode='w'):
    types = ["发黑弹垫", "镀彩锌弹垫"]
    M_list = [3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 48]
    try: 
        with open(file_path, mode=write_mode, encoding="utf-8") as file:
            for main_type in types:
                for m in M_list:
                    file.write("垫圈类")
                    file.write(",")
                    file.write("弹垫")
                    file.write(',')
                    file.write("{}M{}".format(main_type, m))
                    file.write("\n")
        print("文件已成功写入: {}".format(file_path))
    except Exception as e:
        print("写入文件时发生错误: {}".format(e))

def make_pindian_product(file_path, write_mode='w'):
    types = ["发黑平垫", "镀白锌平垫"]
    M_list = [3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 48]
    try: 
        with open(file_path, mode=write_mode, encoding="utf-8") as file:
            for main_type in types:
                for m in M_list:
                    file.write("垫圈类")
                    file.write(",")
                    file.write("平垫")
                    file.write(',')
                    file.write("{}M{}".format(main_type, m))
                    file.write("\n")
        print("文件已成功写入: {}".format(file_path))
    except Exception as e:
        print("写入文件时发生错误: {}".format(e))