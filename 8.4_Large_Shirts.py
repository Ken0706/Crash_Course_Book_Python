def make_shirt(size = 'Large', text = 'I love Python'):
    print(f"Size : {size} || Text : {text}")
def main():
    make_shirt()
    make_shirt(size = 'Medium')
    make_shirt("Small", "I love Java")
if __name__ == '__main__':
    main()