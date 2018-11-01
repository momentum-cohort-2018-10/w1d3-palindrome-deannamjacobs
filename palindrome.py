user_text = input("Enter a phrase or one or more sentences to determine if it is a palindrome.")

def clean_text(new_text):
    new_text = ""
    for char in user_text:
        if char.isalpha():
            new_text = new_text + char
            return new_text

user_text = clean_text(user_text)

length_of_text = len(user_text)
midline_of_text = length_of_text / 2

counter = 0       

while midline_of_text > counter:
    counter = counter + 1
    left_to_right = user_text[counter] 
    right_to_left = user_text[length_of_text - counter - 1]
    
    if left_to_right != right_to_left:
        print("is not a palindrome")

    if left_to_right == right_to_left:
        print("is a palindrome")







