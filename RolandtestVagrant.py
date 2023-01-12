def subscribe(budget):
    subscribe = {
	"Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
        "TOI": [3, 3, 3, 3, 3, 5, 6],
        "HT": [2, 2, 2, 2, 2, 4, 4],
        "ET": [4, 4, 4, 4, 4, 4, 10],
        "BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    }
    result=[]
    total = {
        "TOI": sum(subscribe["TOI"]),
         "HT": sum(subscribe["HT"]),
        "Hindu": sum(subscribe["Hindu"]),
        "ET": sum(subscribe["ET"]),
        "BM": sum(subscribe["BM"]),
       
    }
    total = dict(sorted(total.items(), key=lambda item: item[1]))
    final_result = []
    for i in range(0,len(total)):
      for j in range(i+1, len(total)):
        if total[list(total)[i]] + total[list(total)[j]] <= budget:
          final_result.append([list(total)[i], list(total)[j]])
        else :
          break
    print (final_result)
subscribe(35)