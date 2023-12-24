import game
import copy
DEPTH=1
def go(s):
    if game.isHumTurn(s):
        return abmin(s,DEPTH,float("-inf"),float("inf"))[1]
    else:
        return abmax(s,DEPTH,float("-inf"),float("inf"))[1]

#s = the state (max's turn)
#d = max. depth of search
#a,b = alpha and beta
#returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmax(s,d,a,b):
    if d==0 or game.isFinished(s):
        return [game.value(s),0]
    v=float("-inf")
    ns=game.getNext(s)
    bestMove=0
    for i in ns:
        tmp=abmin(copy.deepcopy(i),d-1,a,b)
        if tmp[0]>v:
            v=tmp[0]
            bestMove=i
        if v>=b:
            return [v,i]
        if v>a:
            a=v
    return [v,bestMove]

#s = the state (min's turn)
#d = max. depth of search
#a,b = alpha and beta
#returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmin(s,d,a,b):
    if d==0 or game.isFinished(s):
        return [game.value(s),0]
    v=float("inf")
    ns = game.getNext(s)
    bestMove=0
    for i in ns:
        tmp = abmax(copy.deepcopy(i), d - 1, a, b)
        if tmp[0]<v:
            v = tmp[0]
            bestMove = i
        if v <=a:
            return [v,i]
        if v <b:
            b = v
    return [v, bestMove]
