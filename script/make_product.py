
# -*- coding: utf-8 -*-
import os
import luosi
import chuandong
import dianpian


if __name__ == "__main__":
    luosi.make_neiliujiao_product("all_product.csv", 'w')
    luosi.make_daopianluosi_product("all_product.csv", 'a')
    luosi.make_neipinbei_product("all_product.csv", 'a')
    chuandong.make_pidai_product("all_product.csv", 'a')
    dianpian.make_pindian_product("all_product.csv", 'a')
    dianpian.make_tandian_product("all_product.csv", 'a')


                
