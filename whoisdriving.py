name1 = input()
score1 = int(input())
name2 = input()
score2 = int(input())
name3 = input()
score3 = int(input())

st_place = ""
st_score = 0
nd_place = ""
nd_score = 0
rd_place = ""
rd_score = 0

if (score1 < score2):
    st_place = name1
    st_score = score1
    nd_place = name2
    nd_score = score2
elif (score2 < score1):
     st_place = name2
     st_score = score2
     nd_place = name1
     nd_score = score1
else:
    if(name1 < name2):
        st_place = name1
        st_score = score1
        nd_place = name2
        nd_score = score2
    elif (name2 < name1):
        st_place = name2
        st_score = score2
        nd_place = name1
        nd_score = score1

if (score3 < nd_score):
        rd_place = nd_place
        rd_score = nd_score
        if (score3 < st_score):
            nd_place = st_place
            nd_score = st_score
            st_place = name3
            st_score = score3
        elif (score3 > st_score):
            nd_place = name3
            nd_score = score3
        else:
            if(name3 < st_place):
                nd_place = st_place
                nd_score = st_place
                st_place = name3
                st_score = score3
            elif (st_place < name3):
                nd_place = name3
                nd_score = score3
elif (score3 > nd_score):
    rd_place = name3
    rd_score = score3
elif (score3 == nd_score):
    if(name3 < nd_place):
         rd_place = nd_place
         rd_score = nd_score   
         if (score3 <= st_score and name3 < st_place):
             nd_place = st_place
             nd_score = st_score
             st_place = name3
             st_score = score3
         else:
             nd_place = name3
             nd_score = score3
    elif (nd_place < name3):
        rd_place = name3
        rd_score = score3



print(f"{st_place} {st_score}")
print(f"{nd_place} {nd_score}")
print(f"{rd_place} {rd_score}")
