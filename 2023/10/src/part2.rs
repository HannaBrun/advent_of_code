use std::{
    collections::HashMap,
    fs::File,
    io::Read,
    ops,
};
use anyhow::Result;
use itertools::Itertools;

#[derive(PartialEq, Clone, Debug)]
enum Direction {
    North,
    South,
    East,
    West,
}

static mut WIDTH: usize = 0;
static mut HEIGHT: usize = 0;

#[derive(PartialEq, Eq, Hash, Clone, Copy, Debug)]
struct Point {
    x: usize,
    y: usize
}

impl ops::Add<&Direction> for &Point {
    type Output = Option<Point>;

    fn add(self, _rhs: &Direction) -> Option<Point> {
        unsafe {
            if (self.x == 0 && _rhs == &Direction::West)
                || (self.x == WIDTH && _rhs == &Direction::East)
                || (self.y == 0 && _rhs == &Direction::North)
                || (self.y == HEIGHT && _rhs == &Direction::South) {
                return None;
            }
        }

        match _rhs {
            Direction::North => Some(Point { x: self.x, y: self.y - 1 }),
            Direction::South => Some(Point { x: self.x, y: self.y + 1 }),
            Direction::East => Some(Point { x: self.x + 1, y: self.y }),
            Direction::West => Some(Point { x: self.x - 1, y: self.y }),
        }
    }

}

#[derive(PartialEq, Clone, Debug)]
enum Placement {
    Loop,
    Unknown,
}

#[derive(PartialEq)]
struct Pipe {
    coordinates: Point,
    character: char,
    endpoints: Vec<Point>,
    placement: Placement,
}

impl Pipe {
    fn new(coordinates: Point, directions: &Vec<Direction>, character: char) -> Self {
        Pipe {
            coordinates,
            character,
            endpoints: directions
                .iter()
                .filter_map(|el| &coordinates + el)
                .collect_vec(),
            placement: Placement::Unknown,
        }
    }

    fn connectable_to(&self, endpoint: &Point) -> bool {
        self.endpoints.contains(endpoint)
    }
}

pub fn run() -> Result<usize> {
    let char_map = HashMap::from([
        ('|', vec![Direction::North, Direction::South]),
        ('J', vec![Direction::North, Direction::West]),
        ('L', vec![Direction::North, Direction::East]),
        ('7', vec![Direction::South, Direction::West]),
        ('F', vec![Direction::South, Direction::East]),
        ('-', vec![Direction::East, Direction::West]),
        ('S', vec![Direction::North, Direction::East, Direction::South, Direction::West]),
        ('.', vec![]),
    ]);
    let mut grid: HashMap<Point, Pipe> = HashMap::new();
    
    let mut buf = String::new();
    File::open("maze.txt")?.read_to_string(&mut buf)?;

    unsafe {
        WIDTH = buf.lines().collect_vec()[0].len() - 1;
        HEIGHT = buf.lines().collect_vec().len() - 1;
    }

    let mut start = Point {x: 0, y: 0 };

    for (y, line) in buf.lines().enumerate() {
        line.char_indices()
            .for_each(|(x, el)| {
                let pipe = Pipe::new(Point{x, y}, char_map.get(&el).unwrap(), el.clone());
                
                if pipe.endpoints.len() == 4 {
                    start = Point{x, y};
                }
                grid.insert(Point{x, y}, pipe);
            });
    }
    
    let mut current_loc = Some(start.clone());
    let mut previous_loc = current_loc.unwrap();
    loop {
        match grid.get_mut(&current_loc.unwrap()) {
            Some(value) => {
                if value.placement == Placement::Loop {
                    for (key, value) in char_map.iter() {
                        if key == &'S' || key == &'.' {
                            continue;
                        }
                        let other_point_0 = (&grid.get(&start).unwrap().coordinates + &value[0]).unwrap();
                        let other_point_1 = (&grid.get(&start).unwrap().coordinates + &value[1]).unwrap();
                        if grid.get(&other_point_0).unwrap().connectable_to(&grid.get(&start).unwrap().coordinates) 
                            && grid.get(&other_point_1).unwrap().connectable_to(&grid.get(&start).unwrap().coordinates) {
                                grid.get_mut(&start).unwrap().character = key.clone().to_owned();
                        }
                    }
                    break;
                } else {
                    value.placement = Placement::Loop;
                }
            },
            None => break
        };

        let pipe = grid.get(&current_loc.unwrap()).unwrap();

        for endpoint in pipe.endpoints.iter() {
            if endpoint == &previous_loc {
                continue;
            }
            let connection = match grid.get(endpoint) {
                Some(other) => match other.connectable_to(&pipe.coordinates) {
                    true => Some(endpoint.clone()),
                    false => None
                },
                None => None
            };

            if let Some(conn) = connection {
                previous_loc = current_loc.unwrap();
                current_loc = Some(conn);
                break;
            }
        }
    }

    let mut inner = 0;
    for y in 0..140 {
        let mut inside = false;
        for x in 0..140 {
            let pipe = grid.get(&Point{ x, y }).unwrap();
            if inside && pipe.placement != Placement::Loop {
                inner += 1;
            }
            if (pipe.character == '|' || pipe.character == 'J' || pipe.character == 'L') && pipe.placement == Placement::Loop {
                inside = !inside;
            }
        }
    }

    Ok(inner)
}