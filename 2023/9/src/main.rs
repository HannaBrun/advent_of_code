mod part1;
mod part2;
use anyhow::Result;

fn main() -> Result<()> {
    let res1 = part1::run()?;
    let res2 = part2::run()?;

    println!("Part 1: {}", res1);
    println!("Part 2: {}", res2);
    Ok(())
}