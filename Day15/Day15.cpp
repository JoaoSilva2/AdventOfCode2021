#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <map>

class Coordinate {
private:
    int x;
    int y;
public:
    Coordinate(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int get_x() {
        return x;
    }

    int get_y() {
        return y;
    }

    bool operator<(const Coordinate& c) const {
        return x < c.x || (x == c.x && y < c.y);
    }

    bool operator==(const Coordinate& c) const {
        return x == c.x && y == c.y;
    }
};

class QueueElement {
private:
    Coordinate content;
public:
    int priority;
    QueueElement(Coordinate content, int priority): content(content) {
        this->priority = priority;
    }

    Coordinate get_content() {
        return content;
    }

    bool operator<(const QueueElement& qe) const {
        return priority > qe.priority;
    }
};

std::vector<std::vector<int>> parse_input(std::ifstream& file, int& dimension) {
    std::vector<std::vector<int>> cave_map;
    std::string line;
    while(std::getline(file, line)) {
        std::vector<int> row;
        for(auto chr: line) {
            if(chr != '\n') {
                row.push_back((int) chr - (int) '0');
            }
        }
        dimension++;
        cave_map.push_back(row);
    }
    return cave_map;
}

std::vector<Coordinate> get_adj(Coordinate origin, int dimension) {
    std::vector<Coordinate> adj;
    int x = origin.get_x(), y = origin.get_y();
    if(x+1 >= 0 and x+1 < dimension) {
        adj.push_back(Coordinate(x+1, y));
    }
    if(x-1 >= 0 and x-1 < dimension) {
        adj.push_back(Coordinate(x-1, y));
    }
    if(y+1 >= 0 and y+1 < dimension) {
        adj.push_back(Coordinate(x, y+1));
    }
    if(y-1 >= 0 and y-1 < dimension) {
        adj.push_back(Coordinate(x, y-1));
    }
    return adj;
}

int least_cost_path(std::vector<std::vector<int>> cave_map, int dimension) {
    std::priority_queue<QueueElement> queue;
    std::map<Coordinate, int> distances;
    std::map<Coordinate, int> visited;
    for(int y = 0; y <= dimension; y++) {
        for(int x = 0; x <= dimension; x++) {
            if(x == 0 && y == 0) {
                distances.insert(std::pair<Coordinate,int>(Coordinate(x,y), 0));
            }
            else {
                distances.insert(std::pair<Coordinate,int>(Coordinate(x,y), INT16_MAX));
            }
        }    
    }
    
    queue.push(QueueElement(Coordinate(0,0), 0));
    while(!queue.empty()) {
        QueueElement qe = queue.top();
        queue.pop();
        if(qe.get_content() == Coordinate(dimension-1, dimension-1)) {
            return distances[qe.get_content()];
        }
        visited.insert(std::pair<Coordinate,int>(qe.get_content(), 1));
        std::vector<Coordinate> adj = get_adj(qe.get_content(), dimension);
        for(auto coord: adj) {
            if(visited.find(coord) != visited.end()) {
                continue;
            }
            int new_dist = distances[qe.get_content()] + cave_map[coord.get_y()][coord.get_x()];
            if(new_dist < distances[coord]) {
                distances[coord] = new_dist;
                queue.push(QueueElement(coord, new_dist));
            }
        }
    }

    return 0;
}

int main(int argc, char* argv[]) {
    std::ifstream file(argv[1]);
    std::vector<std::vector<int>> cave_map;
    int dimension = 0;
    cave_map = parse_input(file, dimension);
    printf("%d\n", least_cost_path(cave_map, dimension));

    std::vector<std::vector<int>> increased_cave;
    for(int i = 0; i < 5; i++) {
        for(auto row: cave_map){
            std::vector<int> new_row;
            for(int j = 0; j < 5; j++) {
                for(auto value: row) {
                    int new_value = value + i + j;
                    if(new_value >= 10) {
                        new_value = new_value - 10 + 1;
                    }
                    new_row.push_back(new_value);
                }

            }
            increased_cave.push_back(new_row);
        }
    }
    printf("%d\n", least_cost_path(increased_cave, dimension*5));

    file.close();
    return 0;
}
