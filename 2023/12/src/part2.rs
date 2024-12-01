use std::{
    fs::File,
    io::Read, fmt::Binary, borrow::BorrowMut,
};
use anyhow::Result;
use itertools::Itertools;

fn parse() {

}

pub fn run() -> Result<u32> {
    let mut buf = String::new();
    File::open("condition.txt")?.read_to_string(&mut buf)?;

    for line in buf.lines() {
        let parsed_line: (&str, &str) = line.split_ascii_whitespace().collect_tuple().unwrap();
        let springs = parsed_line.0;
        let schema: Vec<&str> = parsed_line.1.split(",").collect();

        let mut ext_springs = String::new();
        let mut ext_schema: Vec<&str> = Vec::new();
        for i in 0..5 {
            ext_springs += springs;
            ext_schema.extend_from_slice(&schema);
            if i < 4 {
                ext_springs += "?";
            }
        }

        let spring_groups: Vec<&str> = ext_springs.split(".").filter(|el| *el != "").collect();
        println!("{:?}", spring_groups);
        let mut list_of_combos: Vec<Vec<String>> = Vec::new();
        for group in spring_groups.iter() {
            let unknowns = group.replace("#", "").len() as u32;
            let unknown_combos = 2_u32.pow(unknowns);

            let mut combos: Vec<String> = Vec::new();
            for combo in 0..unknown_combos {
                combos.push(format!("{:0fill$b}", combo, fill = unknowns as usize))
            }
            let mut idx = 0;
            for character in group.chars() {
                if character == '#' {
                    combos.iter_mut().map(|el| el.insert(idx, '1')).collect_vec();
                    idx += 1;
                }
            }
            list_of_combos.push(combos);
            // [bin(combo)[2:].zfill(unknowns) for combo in range(unknown_combos)]
        }

        println!("{:?}", list_of_combos);
        let mut output: Vec<Vec<Vec<usize>>> = Vec::new();
        for possibility in list_of_combos{
            let mut output2: Vec<Vec<usize>> = Vec::new();
            for spring_group in possibility {
                let mut output3: Vec<usize> = Vec::new();
                for springs_in_a_row in spring_group.split("0") {
                    if springs_in_a_row == "" {
                        continue;
                    }
                    output3.push(springs_in_a_row.len());
                }
                if output3.len() == 0 {
                    continue;
                }
                output2.push(output3);
            }
            output.push(output2);
        }
        println!("{:?}", output);
        println!("{:?}", schema);
        break;
    }
    Ok(100)
}