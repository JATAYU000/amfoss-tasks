use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }

    for i in 2..num {
        if num % i == 0 {
            return false;
        }
    }

    true
}

fn main() {
    println!("Enter a number (n) to find prime numbers up to n:");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let n: u32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a valid number.");
            return;
        }
    };

    println!("Prime numbers up to {}:", n);

    for i in 2..=n {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}