import pandas as pd
import operator
import math 
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_colwidth', -1)

def get_data():
    book_data = pd.read_csv('dataset/booksRatingAvg.csv')
    return book_data

def Similarity(bookId1, bookId2):
    booksRatingAvg = get_data()
    a = booksRatingAvg.loc[(booksRatingAvg.ISBN == bookId1),:]
    b = booksRatingAvg.loc[(booksRatingAvg.ISBN == bookId2),:]
    
    yearA = a['yearOfPublication']
    yearB = b['yearOfPublication']
    
    yearDistance = int(math.pow((int(math.pow (yearA, 2)) - int(math.pow (yearB, 2))),2))
    
    authorA = a['bookAuthor']
    authorB = b['bookAuthor']
    if authorA is authorB:
      authorDistance = 0
    else:
      authorDistance = 1
    #print(authorDistance)

    return math.sqrt(yearDistance+authorDistance)

def predict_score(ISBN):
    booksRatingAvg = get_data()
    new_book = booksRatingAvg[booksRatingAvg['ISBN'].str.contains(ISBN)].iloc[0].to_frame().T
    def getNeighbors(baseBook, K):
        distances = []
        
        for index, book in booksRatingAvg.iterrows():
            if index != baseBook.index.values[0]:
                dist = Similarity(baseBook['ISBN'].values[0], book['ISBN'])
                distances.append((index, dist))
    
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
    
        for x in range(K):
            neighbors.append(distances[x])
        print(neighbors)
        return neighbors
    
    K = 5
    avgRating = 0
    neighbors = getNeighbors(new_book, K)
    listRec = []
    print('\nRecommended Books: \n')
    for neighbor in neighbors:
        avgRating = avgRating+booksRatingAvg.loc[neighbor[0]]['Book-Rating_y']  
        print( str(booksRatingAvg.loc[neighbor[0]]['bookTitle']) +" | Rating: "+str(booksRatingAvg.loc[neighbor[0]]['Book-Rating_y']))
        listRec.append(booksRatingAvg.loc[neighbor[0]]['bookTitle'])
    return listRec