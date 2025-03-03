A = {"a", "g", "b", "d", "f", "c" }
B = {"l", "m", "o", "b", "c", "h"}
C = {"c", "d","f","h","k", "j", "i"}

#a. How many elements are there in set A and B
A_B_intersection = A & B
print(f"(a) Number of elements in both A and B: {len(A_B_intersection)}")
#b. How many elements are there in B that is not part of A and C
B_only = B - (A | C)
print(f"(b) Number of elements in B but not in A or C: {len(B_only)}")
print('press enter')

x = input()
set = {
    "i": (B.intersection(C) - A | C - (A|B)), #[h, i, j, k]
    "ii": (A & B & C | (A & C) - B),  #[c, d, f]
    "iii": (B.intersection(A) | B.intersection(C)),  #[b, c, h]
    "iv": ((A & C) - B),  #[d, f]
    "v": (A & B & C),  #[c]
    "vi": ((A | B | C) - C - A)  # [l, m, o]
}
while True:
    print('i:   iv:')
    print('ii:  v:')
    print('iii: vi')
    choice = input("choose: ").strip().lower()

    if choice in set:
        print(f"{choice}. {set[choice]}")
        print('')
        
    else:
        print("Invalid choice. Please try again.")


