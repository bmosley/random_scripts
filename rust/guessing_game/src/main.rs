use std::{io, ops::AddAssign};

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");

    guess = guess.trim().to_string();

    let mut my_num: i32 = guess.parse::<i32>().unwrap();
    //my_num += 1;
    
    my_num.add_assign(1);


    println!("But the answer was {my_num}, sorry.")
}
