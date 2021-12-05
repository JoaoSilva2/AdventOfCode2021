#include <iostream>
#include <fstream> 
#include <string> 

int countNumIncreases(std::ifstream& file) {
    int num_increases = 0;

    std::string previous_value("");
    std::string current_value("");

    std::getline(file, previous_value);

    while(std::getline(file, current_value)) {
        if(std::stoi(current_value) > std::stoi(previous_value)) {
            num_increases++;
        }
        previous_value = current_value;
    }
    return num_increases;
}

int countNumIncreases2(std::ifstream& file) {
    int num_increases = 0;

    std::string current_value("");
    std::string next_value_1("");
    std::string next_value_2("");
    std::string temp("");

    std::getline(file, current_value);
    std::getline(file, next_value_1);
    std::getline(file, next_value_2);

    int previous_sum = std::stoi(current_value) + std::stoi(next_value_1) +
                       std::stoi(next_value_2); 

    while(std::getline(file, temp)) {
        current_value = next_value_1;
        next_value_1 = next_value_2;
        next_value_2 = temp;

        int current_sum = std::stoi(current_value) + std::stoi(next_value_1) +
                          std::stoi(next_value_2);    

        if(current_sum > previous_sum) {
            num_increases++;
        }
        previous_sum = current_sum;
    }
    return num_increases;
}

int main(int argc, char* argv[]) {
    std::ifstream file(argv[1]);  
    printf("Part1: %d\n", countNumIncreases(file)); //1752
    //Reset file cursor
    file.clear();
    file.seekg(0);
    //-----------------
    printf("Part2: %d\n", countNumIncreases2(file)); //1781
    file.close();
    return 0;
}
