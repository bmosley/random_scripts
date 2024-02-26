use std::io;
use std::io::Write;
use serde::Deserialize;

// Constants

const API_BASE: &str = "http://api.openweathermap.org";
const API_KEY: &str  = "";

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

async fn get_weather_data(lat: f64, lon: f64) -> Result<CurrentWeather, Box<dyn std::error::Error>> {
    let url = format!("{API_BASE}/data/2.5/onecall?exclude=minutely,hourly,alerts&units=metric&lat={lat}&lon={lon}&appid={API_KEY}");
    let client = reqwest::Client::new();
    let body: CurrentWeather = client.get(url).send()
        .await?
        .json::<CurrentWeather>()
        .await?;

    Ok(body)
}

async fn get_geo(city_name: &str, state_code: Option<&str>, country_code: Option<&str>, limit: Option<i32>) -> Result<Vec<GeoCoordinates>, Box<dyn std::error::Error>>  {
    let state_code = state_code.unwrap_or("CA");
    let country_code = country_code.unwrap_or("US");
    let limit = limit.unwrap_or(1);
    
    let client = reqwest::Client::new();
    let url = format!("{API_BASE}/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}");

    let body: Vec<GeoCoordinates> = client
                            .get(&url).send()
                            .await?
                            .json::<Vec<GeoCoordinates>>()
                            .await?;

    Ok(body)
}

fn prompt(name:&str) -> String {
    let mut line = String::new();
    print!("{}", name);
    std::io::stdout().flush().unwrap();
    std::io::stdin().read_line(&mut line).expect("Error: Could not read a line");
 
    return line.trim().to_string()
}

#[tokio::main]
async fn main() -> io::Result<()> {

    //let mut user_input = String::new();
    let input = prompt("City Name: ");

    //let city_name = "Campbell";    
    let city_name = &input;
    let mut lat: f64 = 0.0;
    let mut lon: f64 = 0.0;
    let mut temp: f64 = 0.0;
    let mut humidity: f64 = 0.0;

    let coord = get_geo(city_name, None, None, None).await;

    match coord {
        Ok(coord_val) => {
            //println!("fact = {:#?}", coord_val);
            for i in coord_val {
                if i.name == city_name.to_string() {
                    lat = i.lat;
                    lon = i.lon;
                    break;
                }
            }
        },
        Err(coord_err) => {
            println!("{coord_err}")
        }
    }

    if lat == 0.0 || lon == 0.0 {
        println!("No results found for {city_name}.");
        return Ok(());
    }

    let data = get_weather_data(lat, lon).await;

    match data {
        Ok(val) => {
            //println!("fact = {:#?}", val);
            temp = val.current.temp;
            humidity = val.current.humidity;
        },
        Err(err) => {
            println!("Whoops, something went wrong. {err}")
        }
    }

    // make the string capitalized if it's not already
    let mut s = city_name.to_string();
    let capitalized_city = s.remove(0).to_uppercase().to_string() + &s;

    print!("Weather in {capitalized_city}: Current temp = {temp}, humidity = {humidity}\n");
    Ok(())
}