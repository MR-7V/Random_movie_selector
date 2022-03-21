import random
import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/"

def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.ratingColumn.imdbRating')

    actors = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]

    def get_year(movietag):
        moviesplit=movietag.text.split()
        year=moviesplit[-1]
        return year
    years = [get_year(tag) for tag in movietags]

    def get_rating(ratingtag):
        ratingsplit = ratingtag.text
        return float(ratingsplit[1:4])
    ratings=[get_rating(x) for x in ratingtags]

    """rating_tags = soup.select('td.posterColumn span[name=ir]')
    ratings = [float(x['data-value']) for x in rating_tags]"""
    
    n_movies = len(titles)
    while(True):
        idx = random.randrange(0,n_movies)
        print(f'{titles[idx]} {years[idx]}, rating:{ratings[idx]:.1f}, starring: {actors[idx]}')
        user_input = input("Do u want another movie [y/n]")
        if user_input == 'n':
            break
        print("\n")

    
if __name__ == '__main__':
    main()