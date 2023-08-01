def ordenador_bubble_sort(seq):
    n = len(seq)
    h = len(seq)
    while n !=0:
        n -= 1
        for i in range (1,h):
            if seq[i] < seq[i-1]:
                x = seq [i]
                y = seq [i-1]
                seq [i] = y
                seq [i-1] = x
    if crescente(seq):
        return seq

def crescente(seq):
    for i in range(len(seq)):
        if i == 0:
            if seq[i]<=seq[i+1]:
                return True
            else: 
                return False
        elif i == len(seq):
            if seq[i]>=seq[i-1]:
                return True
            else:
                return False
        else:
            if seq[i]>=seq[i-1] and seq[i]<=seq[i+1]:
                return True
            else:
                False
