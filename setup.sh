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

# Обновляем систему и устанавливаем необходимые пакеты
echo "Обновляем систему и устанавливаем зависимости..."
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip
sudo apt install coreutils -y

# Создаём виртуальную среду
echo "Создаём виртуальную среду..."
python3 -m venv myenv

# Активируем виртуальную среду
echo "Активируем виртуальную среду..."
source myenv/bin/activate

# Устанавливаем зависимости из requirements.txt
echo "Устанавливаем зависимости..."
pip install --upgrade pip
pip install -r requirements.txt
echo "После запуска введите свой API и можете входить в аккаунт"
python3 remain.py

clear
echo "Все успешно установленно и созданно!"

