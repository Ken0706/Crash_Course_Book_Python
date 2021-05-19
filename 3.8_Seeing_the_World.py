def fix_font(place):
	for i, v in enumerate(place):
		if i == (len(place) - 1):
			print(f"{v.title()}", end = ".")
			break
		print(f"{v.title()}", end = ", ")
def raw_list(place):
	print("\n5 điểm đến của bạn là (Original) : ", end = "")
	fix_font(place)
def sorted_list(place):
	print("\n5 điểm đến của bạn là (sorted) : ", end = "")
	tmp = sorted(place)
	fix_font(tmp)
def sorted_rev_list(place):
	tmp = sorted(place, reverse = True)
	print("\n5 điểm đến của bạn là (sorted_reversed) : ", end = "")
	fix_font(tmp)
def rev_list(place):
	place.reverse()
	print("\n5 điểm đến của bạn là (reverse) : ", end = "")
	fix_font(place)
def sort_list(place):
	place.sort()
	print("\n5 điểm đến của bạn sau khi sắp xếp là (A - Z): ", end = "")
	fix_font(place)
def sort_rev_list(place):
	place.sort(reverse = True)
	print("\n5 điểm đến của bạn sau khi sắp xếp là (Z - A): ", end = "")
	fix_font(place)
def main():
	place = ["vịnh hạ long", "hà nội", "pháp", "anh", "đức"]
	raw_list(place)
	sorted_list(place)
	raw_list(place)
	sorted_rev_list(place)
	raw_list(place)
	rev_list(place)
	rev_list(place)
	sort_list(place)
	sort_rev_list(place)
if __name__ == "__main__":
	main()



