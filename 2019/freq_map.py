def reverse(Pattern):
    print (Pattern, len(Pattern))
    reverse=""
    for i in range(len(Pattern)-1,-1,-1):
        print (i)
        reverse=reverse+Pattern[i]
    return reverse

Text="AAAACCCGGT"

print (reverse(Text))
#ligne ajouté a hennebont (entrainement git)