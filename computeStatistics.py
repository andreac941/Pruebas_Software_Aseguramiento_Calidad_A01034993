{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXWaKtP8rgy0SS83XkkeVL",
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
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 140
        },
        "id": "SzFzMmsyP_B8",
        "outputId": "ebcf4b26-4bd1-4131-e5e9-a7c0682644da"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: python computeStatistics.py TC1.txt\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "SystemExit",
          "evalue": "1",
          "traceback": [
            "An exception has occurred, use %tb to see the full traceback.\n",
            "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
          ]
        }
      ],
      "source": [
        "import sys\n",
        "import time\n",
        "import statistics\n",
        "\n",
        "def read_file(file_path):\n",
        "    try:\n",
        "        with open(file_path, 'r') as file:\n",
        "            data = [float(line.strip()) for line in file]\n",
        "        return data\n",
        "    except Exception as e:\n",
        "        print(f\"Error reading file: {e}\")\n",
        "        return None\n",
        "\n",
        "def calculate_statistics(data):\n",
        "    if data is not None:\n",
        "        start_time = time.time()\n",
        "\n",
        "        mean_value = sum(data) / len(data)\n",
        "        median_value = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2\n",
        "        mode_value = max(set(data), key=data.count)\n",
        "        variance_value = sum((x - mean_value) ** 2 for x in data) / len(data)\n",
        "        std_deviation_value = variance_value ** 0.5\n",
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
        "if __name__ == \"__main__\":\n",
        "    if len(sys.argv) != 2:\n",
        "        print(\"Usage: python computeStatistics.py TC1.txt\")\n",
        "        sys.exit(1)\n",
        "\n",
        "    input_file_path = sys.argv[1]\n",
        "\n",
        "    data = read_file(input_file_path)\n",
        "\n",
        "    if data is not None:\n",
        "        mean, median, mode, variance, std_deviation, elapsed_time = calculate_statistics(data)\n",
        "\n",
        "        print_results(mean, median, mode, variance, std_deviation, elapsed_time)\n",
        "\n",
        "        write_results_to_file(\"StatisticsResults.txt\", mean, median, mode, variance, std_deviation, elapsed_time)"
      ]
    }
  ]
}