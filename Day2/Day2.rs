use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("day2.txt").unwrap();
    let reader = BufReader::new(file);

    let mut horizontal_depth = 0;
    let mut depth = 0;
    let mut aim = 0;
    let mut aim_depth = 0;

    //part 1 and 2 -----------------------
    for line in reader.lines() {
        let line_str = line.unwrap();
        let split = line_str.split(" ");
        let values = split.collect::<Vec<&str>>();
        match values[0] {
            "forward" => {
                            horizontal_depth += values[1].parse::<i32>().unwrap();
                            aim_depth += aim*values[1].parse::<i32>().unwrap();
                         }
            "down" =>    {
                            depth += values[1].parse::<i32>().unwrap();
                            aim += values[1].parse::<i32>().unwrap();
                         }
            "up" =>      {
                            depth -= values[1].parse::<i32>().unwrap();
                            aim -= values[1].parse::<i32>().unwrap();
                         }
            _ => println!("unkown"),
        }
    }

    println!("part1: {}", horizontal_depth*depth);
    println!("part2: {}", aim_depth*horizontal_depth);
}
