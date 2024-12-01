mod part2;
use anyhow::Result;

fn main() -> Result<()> {
    let res2 = part2::run()?;

    println!("Part 2: {}", res2);
    Ok(())
}