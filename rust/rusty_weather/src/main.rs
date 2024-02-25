//use std::io::Read;


// fn main() {
//     // let pattern = std::env::args().nth(1).expect("no pattern given");
//     // let path = std::env::args().nth(2).expect("no path given");

//     // println!("pattern: {:?}, path: {:?}", pattern, path)

//     // 37.2870626 -121.9448818
//     let mut lat = 37.2870626;
//     let mut lon = -121.9448818;
//     let api_base: &str = "http://api.openweathermap.org";
//     let api_key: &str = "482662e6bbc18c0e6ebc7f180ecc64d8";
//     let url: String = format!("{api_base}/data/2.5/onecall?exclude=minutely,hourly,alerts&units=metric&lat={lat}&lon={lon}&appid={api_key}");


// }

// fn request_result() -> Result<()> {
//     let mut res = reqwest::blocking::get("http://httpbin.org/get")?;
//     let mut body = String::new();
//     res.read_to_string(&mut body)?;

//     println!("Status: {}", res.status());
//     println!("Headers:\n{:#?}", res.headers());
//     println!("Body:\n{}", body);

//     Ok(())
// }

#[tokio::main]
async fn main() {
    let fact = get_cat_fact().await;

    println!("fact = {:#?}", fact);
}

async fn get_cat_fact() -> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();
    let body = client.get("https://catfact.ninja/fact").send()
        .await?
        .text()
        .await?;

    Ok(body)
}