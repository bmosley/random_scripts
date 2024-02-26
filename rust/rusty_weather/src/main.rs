use std::collections::HashMap;

use  serde::Deserialize;

// Constants

const API_BASE: &str = "http://api.openweathermap.org";
const API_KEY: &str  = "482662e6bbc18c0e6ebc7f180ecc64d8";

// Data structures

#[derive(Deserialize, Debug)]
struct CurrentWeather {
    current: CurrentWeatherData
}

#[derive(Deserialize, Debug)]
struct CurrentWeatherData {
    temp: f64,
    humidity: f64,
}

#[derive(Deserialize, Debug)]
struct GeoCoordinates {
    name: String,
    lat: f64,
    lon: f64
}


// #[derive(Deserialize, Debug)]
// pub struct GeoError {
//     error: String,
// }

// #[derive(Deserialize, Debug)]
// pub enum GeoCoordinatesOrError {
//     Geo(GeoCoordinates),
//     Error(GeoError),
// }

#[tokio::main]
async fn main() {
    let data = get_weather_data().await;

    match data {
        Ok(val) => {
            println!("fact = {:#?}", val);
            let temp = val.current.temp;
            let humidity = val.current.humidity;
            print!("Current temp = {temp}, humidity = {humidity}\n")
        },
        Err(err) => {
            println!("Whoops, something went wrong. {err}")
        }
    }

    let mut coord = get_geo("Campbell".to_string(), None, None, None).await;
    println!("fact = {:#?}", coord);
    match coord {
        Ok(coord_val) => {

            // HANDLE GeoCoordinatesOrError



            // let lat = coord_val.lat;
            // let lon = coord_val.lon;
            // print!("Lat = {lat}, Lon = {lon}\n")
        },
        Err(coord_err) => {
            println!("Whoops, something went wrong. {coord_err}")
        }
    }
}

async fn get_weather_data() -> Result<CurrentWeather, Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();

    let lat = 37.2870626;
    let lon= -121.9448818;

    let url = format!("{API_BASE}/data/2.5/onecall?exclude=minutely,hourly,alerts&units=metric&lat={lat}&lon={lon}&appid={API_KEY}");

    let body: CurrentWeather = client.get(url).send()
        .await?
        .json::<CurrentWeather>()
        .await?;

    Ok(body)
}

async fn get_geo(city_name: String, state_code: Option<&str>, country_code: Option<&str>, limit: Option<i32>) -> Result<GeoCoordinates, Box<dyn std::error::Error>>  {
    let state_code = state_code.unwrap_or("US");
    let country_code = country_code.unwrap_or("CA");
    let limit = limit.unwrap_or(1);
    
    let client = reqwest::Client::new();
    let url = format!("{API_BASE}/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}");

    let body: GeoCoordinates = client.get(url).send()
    .await?
    .json::<GeoCoordinates>()
    .await?;

    Ok(body)
}
