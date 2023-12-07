use anyhow::Result;
use std::{
    fs::File,
    io::Read,
    collections::HashMap,
    ops::Range
};

struct Mapping {
    destination: u64,
    source: u64,
    range: u64
}

struct AlmanacMap {
    maps: Vec<Mapping>
}

impl AlmanacMap {
    fn new() -> Self {
        AlmanacMap { maps: Vec::new() }
    }

    fn add_map(&mut self, destination: u64, source: u64, range: u64) {
        self.maps.push(Mapping{ destination, source, range })
    }

    fn get(&self, key: u64) -> u64 {
        for mapping in self.maps.iter() {
            let start = mapping.destination;
            let end = mapping.destination + mapping.range;
            if key >= start && key < end {
                if mapping.source >= mapping.destination {
                    return key + (mapping.source - mapping.destination);
                } else {
                    return key - (mapping.destination - mapping.source);
                }                
            }
        }
        key
    }
}

fn main() -> Result<()> {
    let mut byte_contents: Vec<u8> = Vec::new();
    let mut _file = File::open("seed_almanac.txt")?.read_to_end(&mut byte_contents)?;
    let contents = String::from_utf8_lossy(&byte_contents);

    let mut current_map = "";
    let mut maps: HashMap<&str, AlmanacMap> = HashMap::new();
    let mut order: Vec<&str> = Vec::new();

    let mut seeds: Vec<Range<u64>> = Vec::new();

    for line in contents.lines() {
        if line.starts_with("seeds: ") {
            let nbrs: Vec<u64> = line
                .strip_prefix("seeds: ")
                .unwrap()
                .split(" ")
                .map(|el| el.parse::<u64>().unwrap())
                .collect();

            for seed_and_range in nbrs.chunks(2) {
                seeds.push(Range {
                    start: seed_and_range[0],
                    end: seed_and_range[0] + seed_and_range[1]
                });
            }

        } else if line == "" {
            continue;
        } else if line.ends_with("map:") {
            current_map = line.strip_suffix(" map:").unwrap();
            order.push(current_map);
            maps.insert(current_map, AlmanacMap::new());
        } else {
            let [destination, source, range]: [u64; 3] = line
                .split(" ")
                .map(|el| el.parse::<u64>().unwrap())
                .collect::<Vec<u64>>()
                .try_into()
                .unwrap();

            let almanac = maps.get_mut(current_map).unwrap();
            almanac.add_map(destination, source, range);
        }
    }

    let mut location = 0;
    let mut keep_looking = true;
    while keep_looking {
        let mut seed = location;
        for mapping in order.iter().rev() {
            seed = maps.get(mapping).unwrap().get(seed);
        }

        for seed_range in seeds.iter() {
            if seed_range.contains(&seed) {
                keep_looking = false;
                break;
            }
        }

        if keep_looking{
            location += 1;
        }
    }

    println!("{:?}", location);

    Ok(())
}