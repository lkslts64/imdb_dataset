# imdb_dataset


Requirements:
  -Beatuiful Soup (bs4)
  -python3

Collects data from IMDb using web-scraping (with pauses between requests) for 5500 movies .It collects genre,IMDb rating,runtime,
metascore,title and year of the movie.After collecting ,a new rating is constructed from both IMDb rating and metascore.
In particular: new_rating=(10*9*IMDb_rating+metascore)/10 .The programm collects data from movies that have >5 IMDb rating,featured
after 1990-1-1 and have runtime>85 minutes.Of course,there could have been more than 5500 movies selected, but I chose to select 
the ones with higher number of votes. After collecting all the data, a csv file is created to store the results.
