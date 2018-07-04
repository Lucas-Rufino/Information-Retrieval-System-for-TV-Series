from crawler import spider

def main():
    links_domain = [
        # ['https://trakt.tv', '/shows/'],
        # ['http://www.sho.com', '/series'],
        # ['https://www.themoviedb.org', '/tv' ],
        # ['http://www.tvguide.com', '/watchlist/'],
        # ['https://www.rottentomatoes.com', '/browse/tv-list-1/'],
        ['https://www.imdb.com', '/chart/toptv/?ref_=nv_tp_tv250_2']]

    for x in links_domain:
        extractor_links = spider.main(x)
        if(x[0] == 'https://trakt.tv'):
            with open('links/tracktvlink.txt', 'w') as file:
                for x in extractor_links:
                    file.write(str(x)+'\n')
        elif(x[0] == 'https://www.themoviedb.org'):
            with open('links/movidedblink.txt', 'w') as file:
                for x in  extractor_links:
                    file.write(str(x)+'\n')
        elif(x[0] == 'http://www.sho.com'):
            with open('links/showtimelink.txt', 'w') as file:
                for x in  extractor_links:
                    file.write(str(x)+'\n')
        elif(x[0] == 'http://www.tvguide.com'):
            with open('links/tvguidelink.txt', 'w') as file:
                for x in  extractor_links:
                    file.write(str(x)+'\n')
        elif(x[0] == 'https://www.imdb.com'):
            with open('links/imdblink.txt', 'w') as file:
                for x in  extractor_links:
                    file.write(str(x)+'\n')
        else:
            with open('links/rottenlink.txt', 'w') as file:
                for x in  extractor_links:
                    file.write(str(x)+'\n')

if __name__ == '__main__':
    main()
