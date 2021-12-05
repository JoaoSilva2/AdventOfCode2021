#include <iostream>
#include <fstream> 
#include <string> 
#include <utility> 
#include <map>

using namespace std;

pair<string, string> split(string original, string delimiter) {
    size_t index = original.find(delimiter);
    string token_1 = original.substr(0, index);
    string token_2 = original.substr(index + delimiter.length(), original.length()-1);
    return pair<string, string>(token_1, token_2);
} 

int line_intersection(ifstream& file, bool diagonals) {
    int intersections = 0;

    map<pair<int, int>, int> line_map;
    string line("");
    while(getline(file, line)) {
        pair<string, string> start_finish = split(line, " -> ");
        pair<string, string> start_str = split(start_finish.first, ",");
        pair<string, string> finish_str = split(start_finish.second, ",");

        int x1 = stoi(start_str.first);
        int y1 = stoi(start_str.second);
        int x2 = stoi(finish_str.first);
        int y2 = stoi(finish_str.second);

        int step_y = (y2-y1)/max(abs(y2-y1), 1);
        int step_x = (x2-x1)/max(abs(x2-x1), 1);

        if(x1 == x2 || y1 == y2) {
            for(int i = y1; i != y2+step_y; i+=step_y) {
                auto it = line_map.find(make_pair(x1, i)); 
                if (it == line_map.end()) {
                    line_map.insert(make_pair(make_pair(x1, i), 1));
                } else {
                    it->second++; 
                }
            }

            for(int i = x1; i != x2+step_x; i+=step_x) {
                auto it = line_map.find(make_pair(i, y1)); 
                if (it == line_map.end()) {
                    line_map.insert(make_pair(make_pair(i, y1), 1));
                } else {
                    it->second++; 
                }
            }
        } else if(diagonals) {
            for(int i = x1; i != x2+step_x; i+=step_x) {
                auto it = line_map.find(make_pair(i, y1)); 
                if (it == line_map.end()) {
                    line_map.insert(make_pair(make_pair(i, y1), 1));
                } else {
                    it->second++; 
                }
                y1+=step_y;
            }
        }
    }
    map<pair<int, int>, int>::iterator it;
    for(it = line_map.begin(); it != line_map.end(); it++) {
        if(it->second > 1) intersections++;
    }
    
    return intersections;
}

int main(int argc, char* argv[]) {
    ifstream file(argv[1]);  
    printf("Part1: %d\n", line_intersection(file, false));
    //Reset file cursor
    file.clear();
    file.seekg(0);
    //-----------------
    printf("Part2: %d\n", line_intersection(file, true));
    file.close();
    return 0;
}
