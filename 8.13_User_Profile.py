def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v 
    return profile

def main():
    myself = build_profile('Ken', 'Nguyen', location = 'HCM', age = 5, sex = 'male')
    print(myself)

if __name__ == '__main__':
    main()