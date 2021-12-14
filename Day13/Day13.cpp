#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <sstream>
#include <tuple>
 
struct Coord{ 
    int x; int y; 
    Coord(int x, int y) {
        this->x = x;
        this->y = y;
    }

    bool operator< (const Coord& c) const {
        return std::tie(x, y) < std::tie(c.x, c.y);
    }
};

class my_string {
    std::string content;
public:
    my_string(std::string content) {
        this->content = content;
    }

    std::vector<my_string> split(char* delimiter) {
        std::vector<my_string> tokens;
        char* token = strtok((char*) this->content.data(), delimiter);
        while(token != NULL) {
            tokens.push_back(my_string(std::string(token)));
            token = strtok(NULL, delimiter);
        }
        return tokens;
    }

    std::string get_content() {
        return this->content;
    }

    int parse_to_int() {
        try {
            return stoi(this->content);
        }
        catch (const std::invalid_argument&) {
            int ascii = 0;
            for(auto chr: this->content) {
                ascii += (int) chr;
            }
            return ascii;
        }
        
    }
};

typedef std::vector<my_string> string_vec; 

std::set<Coord> parse_input(std::ifstream& file, std::vector<string_vec>& folds){
    std::set<Coord> paper;
    std::string line;
    for(std::getline(file, line) ; line != ""; std::getline(file, line)) {
        my_string aux(line);
        std::vector<my_string> coordinate = aux.split((char*) ",");
        int x = coordinate.at(0).parse_to_int(); 
        int y = coordinate.at(1).parse_to_int();
        paper.insert(Coord(x, y));
    }
    while(std::getline(file, line)) {
        my_string aux(line);
        std::vector<my_string> coordinate = aux.split((char*) " ");
        std::vector<my_string> fold = coordinate.at(2).split((char*) "=");
        folds.push_back(fold);
    }

    return paper;
}

void fold_paper(std::set<Coord> paper, std::vector<string_vec> folds, int n_folds) {
    int lim_x = INT32_MAX, lim_y = INT32_MAX;
    for(int i = 0; i < n_folds; i++) {
        if(i == 1) std::cout << "Part1: " << paper.size() << std::endl;
        std::vector<my_string> fold = folds.at(i);
        int axis_value = fold.at(1).parse_to_int();
        switch(fold.at(0).parse_to_int()) {
            //x
            case 120:
                {
                if(axis_value < lim_x) lim_x = axis_value; 
                auto it = paper.begin();
                while(it != paper.end()) {
                    if( it->x > axis_value ) {
                        int new_x = -it->x + 2*axis_value;
                        if(new_x >= 0){
                            paper.insert(Coord(new_x, it->y));
                        }
                        it = paper.erase(it);
                    }
                    else {
                        it++; 
                    } 
                }
                break;
                }
            //y
            case 121:
                {
                if(axis_value < lim_y) lim_y = axis_value; 
                auto it = paper.begin();
                while(it != paper.end()) {
                    if( it->y > axis_value ) {
                        int new_y = -it->y + 2*axis_value;
                        if(new_y >= 0){
                            paper.insert(Coord(it->x, new_y));
                        }
                        it = paper.erase(it);
                    } 
                    else{
                        it++;
                    } 
                }
                break;
                }
            default:
                printf("Error, invalid argument!\n");
        }
    }

    std::cout << "Part2: " << std::endl;
    for(int y = 0; y < lim_y; y++){
        for(int x = 0; x < lim_x; x++) {
            if(paper.find(Coord(x, y)) != paper.end()) {
                std::cout << "#";
            }
            else std::cout << ".";
        }
        std::cout << std::endl;
    }
}

int main(int argc, char* argv[]) {
    std::ifstream file(argv[1]);
    std::vector<std::vector<my_string>> folds;
    std::set<Coord> paper = parse_input(file, folds);
    fold_paper(paper, folds, folds.size());
    file.close();
    return 0;
}
