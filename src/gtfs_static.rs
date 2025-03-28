// -------- BEGIN MODULE CODE -------- //

//! GTFS_STATIC
//!
//! A library for fetching and analyzing GTFS Static data from a transit feed.

pub mod get {
    use crate::gtfs_static::{Agency, Calendar, CalendarDates, Routes, StopTimes, Stops, Trips};
    use std::io::Error;

    pub fn agency(file_path: String) -> Result<Vec<Agency>, Error> {
        let mut agency: Vec<Agency> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("agency.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: Agency = result?;
            agency.push(record);
        }

        Ok(agency)
    }

    pub fn calendardates(file_path: String) -> Result<Vec<CalendarDates>, Error> {
        let mut calendardates: Vec<CalendarDates> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("calendar_dates.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: CalendarDates = result?;
            calendardates.push(record);
        }

        Ok(calendardates)
    }

    pub fn calendar(file_path: String) -> Result<Vec<Calendar>, Error> {
        let mut calendar: Vec<Calendar> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("calendar.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: Calendar = result?;
            calendar.push(record);
        }

        Ok(calendar)
    }

    pub fn routes(file_path: String) -> Result<Vec<Routes>, Error> {
        let mut routes: Vec<Routes> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("routes.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: Routes = result?;
            routes.push(record);
        }

        Ok(routes)
    }

    pub fn stops(file_path: String) -> Result<Vec<Stops>, Error> {
        let mut stops: Vec<Stops> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("stops.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: Stops = result?;
            stops.push(record);
        }

        Ok(stops)
    }

    pub fn stoptimes(file_path: String) -> Result<Vec<StopTimes>, Error> {
        let mut stoptimes: Vec<StopTimes> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("stop_times.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: StopTimes = result?;
            stoptimes.push(record);
        }

        Ok(stoptimes)
    }

    pub fn trips(file_path: String) -> Result<Vec<Trips>, Error> {
        let mut trips: Vec<Trips> = Vec::new(); // Initializes the mutable data.
        let mut path: String = file_path.clone(); // Getting the file path and
        path.push_str("trips.txt");
        let mut rdr = csv::ReaderBuilder::new().from_path(path)?;
        for result in rdr.deserialize() {
            let record: Trips = result?;
            trips.push(record);
        }

        Ok(trips)
    }

    #[cfg(test)]
    mod test {
        use super::*;

        #[test]
        fn agency_prints() {
            let path = "src/static/pittsburgh/prt/";
            let agency = agency(path.to_string());
            println!("{:?}", agency);
        }

        #[test]
        fn calendar_prints() {
            let path = "src/static/pittsburgh/prt/";
            let calendar = calendar(path.to_string());
            println!("{:?}", calendar);
        }

        #[test]
        fn calendardates_prints() {
            let path = "src/static/pittsburgh/prt/";
            let calendardates = calendardates(path.to_string());
            println!("{:?}", calendardates);
        }

        #[test]
        fn routes_prints() {
            let path = "src/static/pittsburgh/prt/";
            let routes = routes(path.to_string());
            println!("{:?}", routes);
        }

        #[test]
        fn stops_prints() {
            let path = "src/static/pittsburgh/prt/";
            let stops = stops(path.to_string());
            println!("{:?}", stops);
        }

        #[test]
        fn stoptimes_prints() {
            let path = "src/static/pittsburgh/prt/";
            let stoptimes = stoptimes(path.to_string());
            println!("{:?}", stoptimes);
        }

        #[test]
        fn trips_prints() {
            let path = "src/static/pittsburgh/prt/";
            let trips = trips(path.to_string());
            println!("{:?}", trips);
        }
    }
}

// -------- END MODULE DATA -------- //
// -------- BEGIN MODULE STRUCTS -------- //

#[derive(Debug, serde::Deserialize)]
pub struct Agency {
    pub agency_id: Option<String>,
    pub agency_name: String,
    pub agency_url: String,
    pub agency_timezone: String,
    pub agency_lang: Option<String>,
    pub agency_phone: Option<String>,
    pub agency_fare_url: Option<String>,
    pub agency_email: Option<String>,
}

#[derive(Debug, serde::Deserialize)]
pub struct Calendar {
    pub service_id: String,
    pub monday: String,
    pub tuesday: String,
    pub wednesday: String,
    pub thursday: String,
    pub friday: String,
    pub saturday: String,
    pub sunday: String,
    pub start_date: String,
    pub end_date: String,
}

#[derive(Debug, serde::Deserialize)]
pub struct CalendarDates {
    pub service_id: String,
    pub date: String,
    pub exception_type: String,
}

#[derive(Debug, serde::Deserialize)]
pub struct Routes {
    pub route_id: String,
    pub agency_id: Option<String>,
    pub route_short_name: Option<String>,
    pub route_long_name: Option<String>,
    pub route_desc: Option<String>,
    pub route_type: String,
    pub route_url: Option<String>,
    pub route_color: Option<String>,
    pub route_text_color: Option<String>,
    pub route_sort_order: Option<String>, // Change to u32 eventually.
    pub continuous_pickup: Option<String>,
    pub continuous_dropoff: Option<String>,
    pub network_id: Option<String>,
}

#[derive(Debug, serde::Deserialize)]
pub struct Shapes {
    pub id: String,
    pub pt_lat: String,
    pub pt_lon: String,
    pub pt_sequence: String,
    pub dist_traveled: Option<f32>,
}

#[derive(Debug, serde::Deserialize)]
pub struct Stops {
    pub stop_id: String,
    pub stop_code: Option<String>,
    pub stop_name: Option<String>,
    pub tts_stop_name: Option<String>,
    pub stop_desc: Option<String>,
    pub stop_lat: Option<String>,
    pub stop_lon: Option<String>,
}

#[derive(Debug, serde::Deserialize)]
pub struct StopTimes {
    pub trip_id: String,
    pub arrival_time: Option<String>,
    pub departure_time: Option<String>,
    pub stop_id: Option<String>,
    pub location_group_id: Option<String>,
    pub location_id: Option<String>,
    pub stop_sequence: String,
    pub stop_headsign: Option<String>,
    pub start_pickup_drop_off_window: Option<String>,
    pub end_pickup_drop_off_window: Option<String>,
    pub pickup_type: Option<String>,
    pub dropoff_type: Option<String>,
    pub continuous_pickup: Option<String>,
    pub continuous_dropoff: Option<String>,
    pub shape_dist_traveled: Option<String>,
    pub timepoint: Option<String>,
    pub pickup_booking_rule_id: Option<String>,
    pub drop_off_booking_rule_id: Option<String>,
}

#[derive(Debug, serde::Deserialize)]
pub struct Trips {
    pub route_id: String,
    pub service_id: String,
    pub trip_id: String,
    pub trip_headsign: Option<String>,
    pub trip_short_name: String,
    pub direction_id: Option<String>,
    pub block_id: Option<String>,
    pub shape_id: Option<String>,
    pub wheelchair_accessible: Option<String>,
    pub bikes_allowed: Option<String>,
}

// -------- END MODULE STRUCTS -------- //
