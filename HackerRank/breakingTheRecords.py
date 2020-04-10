def breakingRecords(scores):
    max_el=min_el=scores[0]
    maxCount=0
    minCount=0
    for score in scores:
        if score< min_el:
            min_el=score
            minCount+=1
        if score>max_el:
            max_el=score
            maxCount+=1
    return [maxCount, minCount]