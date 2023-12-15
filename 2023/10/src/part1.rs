use std::{
    collections::HashMap,
    fs::File,
    io::Read,
    ops,
};
use anyhow::Result;
use itertools::Itertools;

#[derive(PartialEq)]
enum Direction {
    North,
    South,
    East,
    West,
}

static mut WIDTH: usize = 0;
static mut HEIGHT: usize = 0;

#[derive(PartialEq, Eq, Hash, Clone, Copy)]
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

#[derive(PartialEq)]
struct Pipe {
    coordinates: Point,
    endpoints: Vec<Point>,
}

impl Pipe {
    fn new(coordinates: Point, directions: &Vec<Direction>) -> Self {
        Pipe {
            coordinates,
            endpoints: directions
                .iter()
                .filter_map(|el| &coordinates + el)
                .collect_vec()
        }
    }

    fn connectable_to(&self, endpoint: &Point) -> bool {
        self.endpoints.contains(endpoint)
    }
}

pub fn run() -> Result<u32> {
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
                let pipe = Pipe::new(Point{x, y}, char_map.get(&el).unwrap());
                
                if pipe.endpoints.len() == 4 {
                    start = Point{x, y};
                }
                
                if pipe.endpoints.len() >= 2 {
                    grid.insert(Point{x, y}, pipe);
                }
            });
    }
    
    let mut current_loc = Some(start.clone());
    let mut steps = 1;
    loop {
        let pipe = match grid.remove(&current_loc.unwrap()) {
            Some(value) => value,
            None => break
        };

        for endpoint in pipe.endpoints.iter() {
            let connection = match grid.get(endpoint) {
                Some(other) => match other.connectable_to(&pipe.coordinates) {
                    true => Some(endpoint.clone()),
                    false => None
                },
                None => None
            };

            if let Some(conn) = connection {
                current_loc = Some(conn);
                break;
            }
        }

        steps += 1;

    }

    Ok(steps / 2)
}