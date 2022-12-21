![Bikeshare](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.fDtZzHprAXoAXBIUtTj0JgHaEo%26pid%3DApi&f=1&ipt=a16385f55e6470f2ee9211f77222c6ad74d7ed85cc10b20c004ee1d778d66f27&ipo=images)

Title: Bike Share Data exploration

Programming language: Python

Background: Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent/borrow a bike from point A and return it at point.By accessing access a dock within the system to unlock or return bicycles. This service provides a wealth of data that can be used to explore how these bike-sharing systems are used.

Objective: To uncover bike share usage patterns in three large cities: Chicago, New York City, and Washington, DC.

Dataset: Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)
- The Chicago and New York City files also have the following two columns:
    - Gender
    - Birth Year

Questions investigated:

- 1 Popular times of travel (i.e., occurs most often in the start time)
    - most common month
    - most common day of week
    - most common hour of day

- 2 Popular stations and trip
   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)

- 3 Trip duration
   - total travel time
   - average travel time

- 4 User info
  - counts of each user type
  - counts of each gender (only available for NYC and Chicago)
  - earliest, most recent, most common year of birth (only available for NYC and Chicago)
