#!/bin/bash

# Выводим красивую надпись "Made by Voterol"
echo "
#     #                                                                                         
##   ##   ##   #####  ######    #####  #   #    #    #  ####  ##### ###### #####   ####  #      
# # # #  #  #  #    # #         #    #  # #     #    # #    #   #   #      #    # #    # #      
#  #  # #    # #    # #####     #####    #      #    # #    #   #   #####  #    # #    # #      
#     # ###### #    # #         #    #   #      #    # #    #   #   #      #####  #    # #      
#     # #    # #    # #         #    #   #       #  #  #    #   #   #      #   #  #    # #      
#     # #    # #####  ######    #####    #        ##    ####    #   ###### #    #  ####  ######                                                                         
"

# Устанавливаем Python 3 и pip
echo "Устанавливаем Python 3 и pip..."
sudo apt update
sudo apt install -y python3 python3-pip

# Устанавливаем зависимости из requirements.txt
echo "Устанавливаем зависимости из requirements.txt..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Скрипт завершен. Установлены зависимости и выведена надпись!"
