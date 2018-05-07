import lexer

_words = ["tvseries", "tvseason", "seasons", "showid", "season", "rating", "showtitle", "200x200", "creator", "startdate", "premiered", "00", "show", "liked", "parents", "documentary", "2ftv", "e2", "subtext", "related", "aggregaterating", "bestrating", "released", "clips", "airdate", "sharer", "itemtype", "itemscope", "person", "actor", "worstrating", "overview", "frameborder", "quicklink", "ribbon", "ratingvalue", "php", "previews", "scripted", "characters", "actions", "replies", "subscribed", "sl", "2fwww", "border", "480x270", "eps", "6px", "reviewcount", "attribute", "tvshow", "viewaction", "popularity", "quick", "panther", "disney", "2px", "cb496569481", "da29", "thetvdb", "918330772", "quicklinksection", "76ed5oqex2yanfg8lppzaesf", "seasonlist", "#seasons", "seasonitem", "49e6c", "titledetailswidget", "cd9e4221190c", "2264473254", "46x22", "9ea0", "titlereviewsandpopularitywidget", "divided", "btn2", "titlereviewbar", "titlereviewbaritem", "mgqez0dycxeavrbbdqtojuzgtqoptmisyqokfjzbwl0qarumxlsmaqqe", "titleplotandcreditsummarywidget", "fullcast", "ff26", "plg", "4f9b", "68e34f43", "quicklinksectioncolumn", "messagewidget", "tvob", "unsuitable", "specs", "quicklinkgroup", "adsystem", "marginwidth", "numberofepisodes", "movieconnections", "rcm", "full", "o", "end", "shows"]
_setws = set()
_dicws = {}

for i, w in enumerate(_words):
    _dicws[w] = i
    _setws.add(w)

def process(data):
    data = lexer.preprocess(data)
    vector = [0] * 100
    for w in data:
        if w in _setws:
            vector[_dicws[w]] = 1
    return vector

def vectorize(data):
    vector = [0] * 100
    for w in data:
        if w in _setws:
            vector[_dicws[w]] = 1
    return vector