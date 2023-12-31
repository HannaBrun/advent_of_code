use std::{
    fs::File,
    io::Read,
};
use anyhow::Result;
use itertools::Itertools;

fn predict(nbrs: &Vec<i32>) -> i32 {
    let diffs = nbrs
        .iter()
        .tuple_windows()
        .map(|(first, second)| second - first)
        .collect_vec();

    let last_nbr = nbrs.last().unwrap();
    let last_derivative = diffs.last().unwrap();

    if diffs.iter().all(|el| el == last_derivative) {
        return last_derivative + last_nbr;
    }
    predict(&diffs) + last_nbr
}

pub fn run() -> Result<i32> {
    let mut buf = String::new();
    File::open("histories.txt")?.read_to_string(&mut buf)?;

    let mut sum = 0;
    for line in buf.lines() {
        let nbr_series = line
            .split_ascii_whitespace()
            .map(|el| el.parse().unwrap())
            .collect_vec();

        sum += predict(&nbr_series);
    }

    Ok(sum)
}