from collections import defaultdict
import argparse

def trieconstruct(queries):
    #initialize the trie
    trie = defaultdict(list)
    trie["root"] = [[False, ""]]
    #prepare name of the nodes
    count = 0
    
    
    for q in queries:
        
        currnode = "root"
        
        for i in range(len(q)):
            char = q[i]
            
            nextnode = None
            
            for edge in trie[currnode]:
                #if the element is the endstring marker, skip it
                if type(edge[0]) == bool:
                    continue
                
                #check if there exists an edge with the current character of the query string
                if (edge[0] == char):
                    nextnode = edge[1] 
            
            #if there is no edge with current character, create a new edge
            if nextnode == None:
                count += 1
                newnode = "n" + str(count)
                trie[newnode] = [[False, ""]]
                trie[currnode].append([char, newnode])
                nextnode = newnode
            
            currnode = nextnode
            
            #update the end string marker if we are at the end of a query string
            if i == len(q)-1:
                trie[currnode][0][0] = True
                trie[currnode][0][1] = q
                        
    return trie


def triesearch(trie, data, queries):
    dictionary = defaultdict()
        
    lines = [line.rstrip() for line in open(queries)]

    for line in lines:
            dictionary[line] = 0


    l = 0
    c = 0
    v = "root"
    
    data = data[l:]
    
    minimum = len(min(dictionary, key=len))
    
    while not (l > len(data)-minimum):
        char = data[c]
        
        Success = False
        
        for edge in trie[v]:
            #if the element is the endstring marker, skip it
            if type(edge[0]) == bool:
                continue
                
            #check if there exists an edge with the current character 
            if (edge[0] == char):
                c += 1
                v = edge[1]
                Success = True
                break
        
        if Success == False:
            l += 1
            c = l
            v = "root"
        
        #check if we arrive at an end node and if True update the dictionary
        if trie[v][0][0] == True:
            dictionary[trie[v][0][1]] += 1
    
    dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

    with open("result" + queries, "w") as file:
                for query in dictionary:
                    file.write(query + " " + str(dictionary[query]) + "\n")
                    
    return dictionary


def main():
    parser = argparse.ArgumentParser(description='search query in database')
    parser.add_argument('query', metavar = 'QUERY', type=str,
                        help='path to the query file')
    parser.add_argument('file', metavar='FILE', type=str,
                        help='path to the input database file')
    
    args = parser.parse_args()
    
    stuff = vars(args)

    queries = [line.rstrip() for line in open(stuff["query"])]

    #construct trie
    trie = trieconstruct(queries)

    #get data
    with open(stuff["file"]) as d:
        lines = [line.rstrip() for line in d][1:]
        string = "".join(lines)

    #run the search
    triesearch(trie, string, stuff["query"])


if __name__ == '__main__':
    main()