{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPY4zBLZT3D0uzi4rFOT9lC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/andreac941/Pruebas_Software_Aseguramiento_Calidad_A01034993/blob/main/computeStatistics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "import statistics\n",
        "import re\n",
        "\n",
        "def contains_valid_data(line):\n",
        "    # Check if a line contains valid data (numeric or string)\n",
        "    for part in line.split():\n",
        "        try:\n",
        "            float(part)\n",
        "        except ValueError:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "def extract_numbers_from_string(s):\n",
        "    # Extract numeric parts from a string and return them as a list of strings\n",
        "    return re.findall(r'-?\\d+\\.?\\d*', s)\n",
        "\n",
        "def convert_to_float(num_str, line_num):\n",
        "    try:\n",
        "        return float(num_str)\n",
        "    except ValueError as e:\n",
        "        print(f\"Error in line {line_num}: {e}. Skipping this part of the line: {num_str}\")\n",
        "        return None\n",
        "\n",
        "def read_file(file_content):\n",
        "    data = []\n",
        "    lines = file_content.split('\\n')\n",
        "    for line_num, line in enumerate(lines, start=1):\n",
        "        if contains_valid_data(line):\n",
        "            extracted_numbers = extract_numbers_from_string(line)\n",
        "            for num_str in extracted_numbers:\n",
        "                num_float = convert_to_float(num_str, line_num)\n",
        "                if num_float is not None:\n",
        "                    data.append(num_float)\n",
        "        else:\n",
        "            print(f\"Error in line {line_num}: Contains non-numeric or invalid data: {line}. Skipping this line.\")\n",
        "\n",
        "    if not data:\n",
        "        print(\"No valid numeric data found in the file.\")\n",
        "\n",
        "    return data\n",
        "\n",
        "def calculate_mode(data):\n",
        "    frequency_dict = {}\n",
        "    for num in data:\n",
        "        frequency_dict[num] = frequency_dict.get(num, 0) + 1\n",
        "\n",
        "    max_frequency = max(frequency_dict.values())\n",
        "    mode = [key for key, value in frequency_dict.items() if value == max_frequency]\n",
        "\n",
        "    return mode[0] if mode else None\n",
        "\n",
        "def calculate_statistics(data):\n",
        "    if data is not None:\n",
        "        start_time = time.time()\n",
        "\n",
        "        #if len(data)%2  == 0:\n",
        "        #len(data)/2\n",
        "        mean_value = sum(data) / len(data)\n",
        "        median_value = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2\n",
        "        mode_value = calculate_mode(data) #max(set(data), key=data.count) # sort(data)\n",
        "        variance_value = (sum((x - mean_value) ** 2 for x in data) / (len(data)-1))  #sum((x - mean_value) ** 2 for x in data) / len(data)\n",
        "        std_deviation_value = (sum((x - mean_value) ** 2 for x in data) / len(data)) ** 0.5 # variance_value ** 0.5\n",
        "\n",
        "        end_time = time.time()\n",
        "        elapsed_time = end_time - start_time\n",
        "\n",
        "        return mean_value, median_value, mode_value, variance_value, std_deviation_value, elapsed_time\n",
        "    else:\n",
        "        return None\n",
        "\n",
        "def print_results(mean, median, mode, variance, std_deviation, elapsed_time):\n",
        "    print(f\"Mean: {mean}\")\n",
        "    print(f\"Median: {median}\")\n",
        "    print(f\"Mode: {mode}\")\n",
        "    print(f\"Variance: {variance}\")\n",
        "    print(f\"Standard Deviation: {std_deviation}\")\n",
        "    print(f\"Time Elapsed: {elapsed_time} seconds\")\n",
        "\n",
        "def write_results_to_file(file_path, mean, median, mode, variance, std_deviation, elapsed_time):\n",
        "    with open(file_path, 'w') as result_file:\n",
        "        result_file.write(f\"Mean: {mean}\\n\")\n",
        "        result_file.write(f\"Median: {median}\\n\")\n",
        "        result_file.write(f\"Mode: {mode}\\n\")\n",
        "        result_file.write(f\"Variance: {variance}\\n\")\n",
        "        result_file.write(f\"Standard Deviation: {std_deviation}\\n\")\n",
        "        result_file.write(f\"Time Elapsed: {elapsed_time} seconds\\n\")\n",
        "\n",
        "# Simulating command-line argument\n",
        "your_file_content = \"\"\"1.2\n",
        "2.5\n",
        "3.8\n",
        "4.1\n",
        "5.4\n",
        "invalid1\n",
        "invalid2\n",
        "\"\"\"\n",
        "\n",
        "with open(\"TC7.txt\", \"r\") as file: #NO APLICA PARA CONSOLA PYTHON\n",
        "    your_file_content = file.read()\n",
        "data = read_file(your_file_content)\n",
        "\n",
        "if data:\n",
        "    mean, median, mode, variance, std_deviation, elapsed_time = calculate_statistics(data)\n",
        "\n",
        "    print_results(mean, median, mode, variance, std_deviation, elapsed_time)\n",
        "\n",
        "    write_results_to_file(\"StatisticsResults.txt\", mean, median, mode, variance, std_deviation, elapsed_time)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WH3FHKLBwywR",
        "outputId": "be657a5c-20f2-45b3-b4f7-1559e5f9c01b"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error in line 183: Contains non-numeric or invalid data: ABBA. Skipping this line.\n",
            "Error in line 229: Contains non-numeric or invalid data: ERROR. Skipping this line.\n",
            "Mean: 2.474673954997149e+20\n",
            "Median: 2.4664097307429e+20\n",
            "Mode: 1.57638329490099e+20\n",
            "Variance: 2.091243115380632e+40\n",
            "Standard Deviation: 1.4460564700984703e+20\n",
            "Time Elapsed: 0.012381553649902344 seconds\n"
          ]
        }
      ]
    }
  ]
}