#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

long array_sum(long* array, int size) {
    long sum = 0;
    for(int i = 0; i <= size; i++) {
        sum += (long) array[i];
    }
    return sum;
}

long simulate(std::string line, int n_days) {
    long generation[9] =  {0};
    for(std::string::iterator it = line.begin(); it != line.end(); it++) {
        if(*it != ',') {
            generation[(long) *it - '0']++;
        } 
    }
    for(int i = 0; i < n_days; i++) {
        long tmp = generation[0];
        for(int j = 1; j <= 8; j++) {
            generation[j-1] += generation[j];
            generation[j] = 0;
        }
        generation[0] -= tmp;
        generation[6] += tmp;
        generation[8] += tmp;
    }

    return array_sum(generation, 8);
}

int main(int argc, char* argv[]) {
    std::ifstream file(argv[1]);
    std::string line("");
    std::getline(file, line);  
    std::cout << "Part1: " << simulate(line, 80) << std::endl;
    std::cout << "Part2: " << simulate(line, 256) << std::endl;
    file.close();
    return 0;
}
