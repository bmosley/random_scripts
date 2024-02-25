use  serde::{Deserialize};

#[derive(Deserialize, Debug)]
struct CatFact {
    fact: String,
    length: i32,
}


#[tokio::main]
async fn main() {
    let fact = get_cat_fact().await;
    // println!("fact = {:#?}", fact);

    // if it's FOR SURE, use unwrap:
    // let new_thing = val.unwrap();

    // otherwise, pattern match
    match fact {
        Ok(val) => {
            // Use val here....
            println!("fact = {:#?}", val);

            let new_fact = val.fact;
            let new_len = val.length;
            
            println!("{new_fact} (len = {new_len})");
        },
        Err(err) => {
            // Do something with the error if you want
            println!("Whoops, something went wrong. {err}")
        }
    }

    // If you are going to handle only one variant, you can also use if let statement like this
    // if let Some(val) = fact {
    //     // Do something with val
    //     println!("{val}")
    // }

}

// FOR STRING
// async fn get_cat_fact() -> Result<String, Box<dyn std::error::Error>> {
//     let client: reqwest::Client = reqwest::Client::new();
//     let body: String = client.get("https://catfact.ninja/fact").send()
//         .await?
//         .text()
//         .await?;

//     Ok(body)
// }

// FOR JSON
async fn get_cat_fact() -> Result<CatFact, Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();

    let body = client
        .get("https://catfact.ninja/fact")
        .send()
        .await?
        .json::<CatFact>()
        .await?;

    Ok(body)
}
