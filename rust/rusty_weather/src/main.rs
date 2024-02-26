use  serde::Deserialize;

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

#[tokio::main]
async fn main() {

    let city_name = "Campbell";    
    let mut lat: f64 = 0.0;
    let mut lon: f64 = 0.0;
    let mut temp: f64 = 0.0;
    let mut humidity: f64 = 0.0;

    let coord = get_geo(city_name, None, None, None).await;

    match coord {
        Ok(coord_val) => {
            //println!("fact = {:#?}", coord_val);
            for i in coord_val {
                if i.name == city_name {
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

    print!("Weather in {city_name}: Current temp = {temp}, humidity = {humidity}\n")
}